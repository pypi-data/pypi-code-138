from anndata import AnnData
from typing import Optional, Union, Dict, List
import pandas as pd
import matplotlib.pyplot as plt
import scanpy as sc


def kernel_density(
    adata: Union[AnnData, pd.Series, Dict[str, pd.Series]],
    key: Union[str, Dict[str, str]],
    spot_size: Optional[float] = None,
    cmap: Optional[str] = None,
    show: Optional[bool] = True,
    title: Optional[str] = None,
    ax: Optional[plt.Axes] = None
) -> Optional[Union[plt.Figure, plt.Axes]]:
    """Plots the results of :func:`~monkeybread.calc.kernel_density` using :func:`~scanpy.pl.embedding`.

    Parameters
    ----------
    adata
        Annotated data matrix.
    key
        Either a key in `adata.obs` or a mapping of group names to keys in `adata.obs` corresponding
        to density columns.
    spot_size
        The size of spots to plot.
    cmap
        Colormap to use for values 0 to 1
    show
        Whether to show the plot or return it
    title
        Title of the plot
    ax
        An Axes object to add the plot to. Only works if `key` is a single key.

    Returns
    -------
    plot
        If `show = False` returns the current figure (if `key` is a mapping) or the current axes
        (if `key` is a string). If `show = True` returns nothing.
    """
    if type(key) == dict:
        ncols = min(len(key), 4)
        nrows = int(len(key) / ncols) + 1
        for (index, subgroup) in zip(range(len(key)), key.keys()):
            axs = plt.subplot(nrows, ncols, index + 1)
            kernel_density(
                adata,
                key = subgroup,
                spot_size = spot_size,
                cmap = cmap,
                show = False,
                title = title,
                ax = axs,
            )
        plt.subplots_adjust(
            left = 0.1,
            bottom = 0.1,
            right = 0.9,
            top = 0.9,
            wspace = 0.4,
            hspace = 0.4
        )
        if show:
            plt.show()
        else:
            return plt.gcf()
    axs = sc.pl.embedding(
        adata,
        basis = "spatial",
        color = key,
        s = spot_size,
        cmap = cmap,
        show = show,
        title = title,
        ax = ax,
        vmin = 0.0,
        vmax = 1.0
    )
    if not show:
        return axs
