# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/core.ipynb.

# %% auto 0
__all__ = ['HierarchicalReconciliation']

# %% ../nbs/core.ipynb 3
import re
from inspect import signature
from scipy.stats import norm
from typing import Callable, Dict, List, Optional

import numpy as np
import pandas as pd

from .probabilistic_methods import Normality, Bootstrap, PERMBU

# %% ../nbs/core.ipynb 5
def _build_fn_name(fn) -> str:
    fn_name = type(fn).__name__
    func_params = fn.__dict__
    args_to_remove = ['insample']
    if not func_params.get('nonnegative', False):
        args_to_remove += ['nonnegative']
    func_params = [f'{name}-{value}' for name, value in func_params.items() if name not in args_to_remove]
    if func_params:
        fn_name += '_' + '_'.join(func_params)
    return fn_name

# %% ../nbs/core.ipynb 9
class HierarchicalReconciliation:
    """Hierarchical Reconciliation Class.

    The `core.HierarchicalReconciliation` class allows you to efficiently fit multiple 
    HierarchicaForecast methods for a collection of time series and base predictions stored in 
    pandas DataFrames. The `Y_df` dataframe identifies series and datestamps with the unique_id and ds columns while the
    y column denotes the target time series variable. The `Y_h` dataframe stores the base predictions, 
    example ([AutoARIMA](https://nixtla.github.io/statsforecast/models.html#autoarima), [ETS](https://nixtla.github.io/statsforecast/models.html#autoets), etc.).

    **Parameters:**<br>
    `reconcilers`: A list of instantiated classes of the [reconciliation methods](https://nixtla.github.io/hierarchicalforecast/methods.html) module .<br>

    **References:**<br>
    [Rob J. Hyndman and George Athanasopoulos (2018). \"Forecasting principles and practice, Hierarchical and Grouped Series\".](https://otexts.com/fpp3/hierarchical.html)
    """
    def __init__(self,
                 reconcilers: List[Callable]):
        self.reconcilers = reconcilers
        self.insample = any([method.insample for method in reconcilers])

    def reconcile(self, 
                  Y_hat_df: pd.DataFrame,
                  S: pd.DataFrame,
                  tags: Dict[str, np.ndarray],
                  Y_df: Optional[pd.DataFrame] = None,
                  level: Optional[List[int]] = None,
                  intervals_method: str = 'normality'):
        """Hierarchical Reconciliation Method.

        The `reconcile` method is analogous to SKLearn `fit` method, it applies different 
        reconciliation methods instantiated in the `reconcilers` list. 
        
        Most reconciliation methods can be described by the following convenient 
        linear algebra notation:

        $$\\tilde{\mathbf{y}}_{[a,b],\\tau} = \mathbf{S}_{[a,b][b]} \mathbf{P}_{[b][a,b]} \hat{\mathbf{y}}_{[a,b],\\tau}$$
        
        where $a, b$ represent the aggregate and bottom levels, $\mathbf{S}_{[a,b][b]}$ contains
        the hierarchical aggregation constraints, and $\mathbf{P}_{[b][a,b]}$ varies across 
        reconciliation methods. The reconciled predictions are $\\tilde{\mathbf{y}}_{[a,b],\\tau}$, and the 
        base predictions $\hat{\mathbf{y}}_{[a,b],\\tau}$.

        **Parameters:**<br>
        `Y_hat_df`: pd.DataFrame, base forecasts with columns `ds` and models to reconcile indexed by `unique_id`.<br>
        `Y_df`: pd.DataFrame, training set of base time series with columns `['ds', 'y']` indexed by `unique_id`.
        If a class of `self.reconciles` receives `y_hat_insample`, `Y_df` must include them as columns.<br>
        `S`: pd.DataFrame with summing matrix of size `(base, bottom)`, see [aggregate method](https://nixtla.github.io/hierarchicalforecast/utils.html#aggregate).<br>
        `tags`: Each key is a level and its value contains tags associated to that level.<br>
        `level`: float list 0-100, confidence levels for prediction intervals.<br>
        `intervals_method`: str, method used to calculate prediction intervals, one of `normality`, `bootstrap`, `permbu`.<br>
         
        **Returns:**<br>
        `y_tilde`: pd.DataFrame, with reconciled predictions.        
        """
        #----------------------------- Preliminary Wrangling/Protections -----------------------------#
        # Check input's validity
        if intervals_method not in ['normality', 'bootstrap', 'permbu']:
            raise ValueError(f'Unkwon interval method: {intervals_method}')

        if self.insample or (intervals_method in ['bootstrap', 'permbu']):
            if Y_df is None:
                raise Exception('you need to pass `Y_df`')            

        # Declare output names
        drop_cols = ['ds', 'y'] if 'y' in Y_hat_df.columns else ['ds']
        model_names = Y_hat_df.drop(columns=drop_cols, axis=1).columns.to_list()
        pi_model_names = [name for name in model_names if ('-lo' in name or '-hi' in name)]
        model_names = [name for name in model_names if name not in pi_model_names]

        uids = Y_hat_df.index.unique()

        # Check Y_hat_df\S_df series difference
        S_diff  = len(S.index.difference(uids))
        Y_hat_diff = len(Y_hat_df.index.difference(S.index.unique()))
        if S_diff > 0 or Y_hat_diff > 0:
            raise Exception(f'Check `S_df`, `Y_hat_df` series difference, S\Y_hat={S_diff}, Y_hat\S={Y_hat_diff}')

        if Y_df is not None:
            # Check Y_hat_df\Y_df series difference
            Y_diff  = len(Y_df.index.difference(uids))
            Y_hat_diff = len(Y_hat_df.index.difference(Y_df.index.unique()))
            if Y_diff > 0 or  Y_hat_diff > 0:
                raise Exception(f'Check `Y_hat_df`, `Y_df` series difference, Y_hat\Y={Y_hat_diff}, Y\Y_hat={Y_diff}')

        # Same Y_hat_df/S_df/Y_df's unique_id order to prevent errors
        S_ = S.loc[uids]
    

        #---------------------------------------- Predictions ----------------------------------------#
        # Initialize reconciler arguments
        reconciler_args = dict(
            S=S_.values.astype(np.float32),
            idx_bottom=S_.index.get_indexer(S.columns),
            tags={key: S_.index.get_indexer(val) for key, val in tags.items()}
        )
        if Y_df is not None:
            reconciler_args['y_insample'] = Y_df.pivot(columns='ds', values='y').loc[uids].values.astype(np.float32)

        fcsts = Y_hat_df.copy()
        for reconcile_fn in self.reconcilers:
            reconcile_fn_name = _build_fn_name(reconcile_fn)
            has_fitted = 'y_hat_insample' in signature(reconcile_fn).parameters
            has_level = 'level' in signature(reconcile_fn).parameters
            for model_name in model_names:
                # should we calculate prediction intervals?
                pi_model_name = [pi_name for pi_name in pi_model_names if model_name in pi_name]
                pi = len(pi_model_name) > 0
                # Remember: pivot sorts uid
                y_hat_model = Y_hat_df.pivot(columns='ds', values=model_name).loc[uids].values
                if pi and has_level and level is not None and intervals_method in ['normality', 'permbu']:
                    # we need to construct sigmah and add it
                    # to the reconciler_args
                    # to recover sigmah we only need 
                    # one prediction intervals
                    pi_col = pi_model_name[0]
                    sign = -1 if 'lo' in pi_col else 1
                    level_col = re.findall('[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+', pi_col)
                    level_col = float(level_col[0])
                    z = norm.ppf(0.5 + level_col / 200)
                    sigmah = Y_hat_df.pivot(columns='ds', values=pi_col).loc[uids].values
                    sigmah = sign * (sigmah - y_hat_model) / z
                    reconciler_args['level'] = level
                    if intervals_method == 'permbu':
                        y_hat_insample = Y_df.pivot(columns='ds', values=model_name).loc[uids].values
                        y_hat_insample = y_hat_insample.astype(np.float32)
                        reconciler_args['sampler'] = PERMBU(
                            S=reconciler_args['S'],
                            tags=reconciler_args['tags'],
                            y_insample=reconciler_args['y_insample'], 
                            y_hat_insample=y_hat_insample,
                            sigmah=sigmah,
                            n_samples=None
                        )
                    elif intervals_method == 'normality':
                        reconciler_args['sampler'] = Normality(S=reconciler_args['S'], sigmah=sigmah)
                if (self.insample and has_fitted) or (intervals_method in ['bootstrap']):
                    if model_name in Y_df:
                        y_hat_insample = Y_df.pivot(columns='ds', values=model_name).loc[uids].values
                        y_hat_insample = y_hat_insample.astype(np.float32)
                        if has_fitted:
                            reconciler_args['y_hat_insample'] = y_hat_insample 
                        if intervals_method == 'bootstrap' and has_level:
                            reconciler_args['sampler'] = Bootstrap(
                                S=reconciler_args['S'],
                                y_insample=reconciler_args['y_insample'],
                                y_hat_insample=y_hat_insample, 
                                y_hat=y_hat_model, 
                                n_samples=1_000
                            )
                            reconciler_args['level'] = level
                    else:
                        # some methods have the residuals argument
                        # but they don't need them
                        # ej MinTrace(method='ols')
                        reconciler_args['y_hat_insample'] = None

                # Mean reconciliation
                kwargs = [key for key in signature(reconcile_fn).parameters if key in reconciler_args.keys()]
                kwargs = {key: reconciler_args[key] for key in kwargs}
                fcsts_model = reconcile_fn(y_hat=y_hat_model, **kwargs)

                # TODO: instantiate prob reconcilers after mean reconc 
                # and use _prob_reconcile function from probabilistic_methods.py
                # this will greatly simplify code above, and improve its readability
                # this will require outputs of reconcile_fn to include P, W

                fcsts[f'{model_name}/{reconcile_fn_name}'] = fcsts_model['mean'].flatten()
                if (pi and has_level and level is not None) or (intervals_method in ['bootstrap'] and level is not None):
                    for lv in level:
                        fcsts[f'{model_name}/{reconcile_fn_name}-lo-{lv}'] = fcsts_model[f'lo-{lv}'].flatten()
                        fcsts[f'{model_name}/{reconcile_fn_name}-hi-{lv}'] = fcsts_model[f'hi-{lv}'].flatten()
                    del reconciler_args['level']
                    del reconciler_args['sampler']
                if self.insample and has_fitted:
                    del reconciler_args['y_hat_insample']
        return fcsts
