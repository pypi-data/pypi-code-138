#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Consise wrapper around Plotly/Pandas for quick timeseries
    postprocessing.

    Core functionality in 'auto_plot' function.

    Supports line, scatter and bar charts as well as histograms for N series.
"""


__author__ = 'Ross Bonallo'
__license__ = 'MIT Licence'
__version__ = '1.2.0'


import plotly.graph_objs as go
from plotly import subplots
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.cm


def helper():
    print("""
        from IPython.core.display import display, HTML
        display(HTML("<style>.container { width:100% !important; }</style>"))

        from plotly.offline import init_notebook_mode, iplot

        df = pd.DataFrame([1,2,3],['A','B','C'])

        fig = auto_plot(df)

        iplot(fig)
        """)


def _get_nearest_key(value, kvp):
    if value is np.nan:
        return kvp.get(0.0)
    res_key, res_val = min(kvp.items(), key=lambda x: abs(value-x[0]))
    return res_val


colorscale = dict([
    [0.7777, "rgb(244,109,67)"],
    [0.6666, "rgb(253,174,97)"],
    [0.5555, "rgb(254,224,144)"],
    [0.4444, "rgb(224,243,248)"],
    [0.3333, "rgb(171,217,233)"],
    [0.2222, "rgb(116,173,209)"]])


def _table_plot(df, delta_colors=False, relative_colors=False):
    colors = []

    if delta_colors:
        for c in df:
            try:
                colors.append(
                    df[c].apply(lambda v: 'lightgreen' if v > 0 else 'salmon' if v < 0 else 'white').values.tolist())
            except Exception as e:
                colors.append(['white']*len(df))

    elif relative_colors:
        for c in df:
            try:
                s=df[c] - df[c].min()
                if s.max() > 0:
                    s = s/s.max()
                colors.append(
                    s.apply(lambda v: _get_nearest_key(v, colorscale)).values.tolist())
            except Exception:
                colors.append(['white']*len(df))

    else:
        colors = ['white']

    fig = go.Figure(data=[go.Table(
        header=dict(values=df.columns,
                    line_color='darkslategray',
                    align='left'),
        cells=dict(values=df.T.values, fill_color=colors,
                   line_color='darkslategray',
                   align='left'))
    ])
    fig['layout'] = go.Layout(autosize=False, margin=dict(l=5, r=5, b=20, t=20), width=1000, height=80 + 20 * len(df))
    return fig


def generate_series_colorscale(s):
    if isinstance(s, pd.DataFrame):
        s = s.iloc[:, 0]
    vmin, vmax = s.min(), s.max()
    norm = matplotlib.colors.Normalize(vmin, vmax)
    cmap = matplotlib.cm.get_cmap('winter')
    colors = []
    for y in s.values:
        x = cmap(norm(y))[0:3]
        x = tuple((225*np.array(x)).astype(int))
        s = 'rgb' + str(x)
        colors.append(s)
    return colors


def set_fig_colors(fig, colors):
    fig['data'][0]['marker'] = dict(color=colors)
    return fig


def plot_array(figs, columns, rows, names=[], title='', showlegend=False, extra_layout=None):
    """
    Create single figure of multiple traces.

    Parameters
    ----------
    figs : Plotly Trace array
        Array of plotly traces.
    columns : int
        N columns to have.
    rows : int
        N rows to have.
    names : str list
        Titles for individual charts/traces.
    title : str
        Figure title.
    showlegend : bool
        Enable the legend, as multiple series can be involved, multiple can get messy
    extra_layout : dict
        A dict of KVP's iterated through and merged with layout.

    Returns
    ------
    Plotly Figure

    """

    fig = subplots.make_subplots(rows=rows, cols=columns, subplot_titles=names,
                                 vertical_spacing=0.04, horizontal_spacing=0.02)

    for i in range(rows):
        for j in range(columns):
            if len(figs) < 1:
                break
            traces = figs[0]
            figs = figs[1:]
            for trace in traces:
                fig.add_trace(trace, i+1, j+1)

    fig['layout'].update(height=rows*550, title=title, showlegend=showlegend,
                         paper_bgcolor='white', plot_bgcolor='white',
                         yaxis=dict(gridcolor='lightgrey'),
                         xaxis=dict(gridcolor='lightgrey'))

    for i in range(2, rows*columns):
        fig['layout']['yaxis'+str(i)]['gridcolor'] = 'lightgrey'
        fig['layout']['xaxis'+str(i)]['gridcolor'] = 'lightgrey'

    if extra_layout:
        fig['layout'].update(extra_layout)

    return fig


def auto_plot(df, height=800, width=None, mode='line', text_axis=None, ys=False, as_traces=False,
              showlegend=True, nbinsx=1000, horizontal_bar=False, extra_layout=None, title=None, mini=False,
              xaxis_label=None, yaxis_label=None, colors_override=None, legend_size=None,
              fill=None, opacity=0.7, colorscale='jet_r', delta_colors=False, relative_colors=False):

    """
    Jupyter Notebook plotting function for timeseries as dataframes.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame of N Series to be plotted.
    height : int
        Height of figure.
    width : int
        Width of figure.
    mode : str
        Option of figure mode, relate to plotly modes.
    text_axis : str
        Dunno
    ys : bool
        Enable multiple Y-axis for N Series incl in DataFrame.
    as_traces : bool
        Return figure as array of traces instead of figure.
    showlegend : bool
        Hide legend
    nbinsx : int
        Only for histogram, dictates how many bins in X-axis to use.
    extra_layout : dict
        A dict of KVP's iterated through and merged with layout.
    title : str
        Chart title
    mini : bool
        Enable mini mode for notebook.
    xaxis_label : str
        X-axis label.
    yaxis_label : str
        Y-axis label.
    colors_override : list
        List of string colors to replace default selection.
    legend_size : int
        Legend font size.
    fill : str
        Fill under/over line options.
    opacity : float
        opacity of bar.

    Returns
    ------
    Plotly Figure or Trace
    """

    def _initiate_layout(ys=False, extra_y_axes=7):
        hide_y = not ys
        layout = go.Layout(height=800,
                           paper_bgcolor='white',
                           plot_bgcolor='white',
                           yaxis=dict(showticklabels=hide_y, gridcolor='lightgrey'),
                           xaxis=dict(gridcolor='lightgrey'),
                           yaxis2=dict(anchor='free', overlaying='y',
                                       side='left', showticklabels=hide_y, showgrid=hide_y), bargap=0.1)

        for i in range(3, extra_y_axes+3):
            layout['yaxis' + str(i)] = dict(anchor='free', overlaying='y', side='right',
                                            showticklabels=hide_y, showgrid=hide_y)

        return layout

    _colors = [
        '#1f77b4',  # muted blue
        '#ff7f0e',  # safety orange
        '#2ca02c',  # cooked asparagus green
        '#d62728',  # brick red
        '#9467bd',  # muted purple
        '#8c564b',  # chestnut brown
        '#e377c2',  # raspberry yogurt pink
        '#7f7f7f',  # middle gray
        '#bcbd22',  # curry yellow-green
        '#17becf']  # blue-teal

    if isinstance(df, pd.Series):
        df = pd.DataFrame(df)

    traces = []

    if mini:
        height, width = 500, 1000

    y_index = range(1, len(df.columns) + 1, 1)

    if text_axis == 'x':
        f_text = lambda _df: _df.index
    elif text_axis == 'y':
        f_text = lambda _df: _df.values
    elif text_axis is None:
        f_text = lambda _df: None
    else:
        f_text = lambda _df: _df[text_axis].values

    colors_ext = colors_override if colors_override else _colors
    colors_ext.extend([None] * max([(len(df.columns) - len(colors_ext)), 0]))

    for column, i, color in zip(df.columns, y_index, colors_ext):

        y = 'y' if ys is False else 'y' + str(i)

        if mode == 'line':

            traces.append(go.Scatter(x=df[column].index, y=df[column].values,
                                     text=f_text(df[column]), name=str(column), yaxis=y,
                                     textposition='top center', fill=fill, showlegend=showlegend,
                                     line=dict(color=color, width=1)))

        elif mode == 'scatter':

            traces.append(go.Scatter(x=df[column].index, y=df[column].values, mode='markers',
                                     text=f_text(df[column]), name=str(column), yaxis=y,
                                     textposition='top center', showlegend=showlegend,
                                     marker=dict(color=color)))

        elif mode == 'bar':

            if not horizontal_bar:
                traces.append(go.Bar(x=df[column].index, y=df[column].values,
                                     text=f_text(df[column]), name=str(column), yaxis=y, opacity=opacity,
                                     textposition='outside', showlegend=showlegend,
                                     marker=dict(color=color)))
            else:
                traces.append(go.Bar(y=df[column].index, x=df[column].values, orientation='h',
                                     text=f_text(df[column]), name=str(column), yaxis=y, opacity=opacity,
                                     textposition='outside', showlegend=showlegend,
                                     marker=dict(color=color)))

        elif mode == 'histogram':

            traces.append(go.Histogram(x=df[column].values, nbinsx=nbinsx,
                                       text=f_text(df[column]), name=str(column), yaxis=y, opacity=0.7,
                                       showlegend=showlegend, marker=dict(color=color)))

        elif mode == 'table':
            return _table_plot(df, delta_colors=delta_colors, relative_colors=relative_colors)

        else:
            raise ValueError('Valid modes: [line, scatter, bar, histogram, table]')

    fig = dict(data=traces, layout=_initiate_layout(ys,len(df.columns)))
    fig['layout']['height'] = height
    fig['layout']['width'] = width

    if mode == 'table':
        trace = go.Heatmap(z=df.T.values, x=df.index, y=df.columns, hoverongaps=False,
                           colorscale=colorscale)
        fig = go.Figure(trace)

    if mode == 'bar' and relative_colors:
        colors = generate_series_colorscale(df)
        fig = set_fig_colors(fig, colors)

    if title:
        fig['layout']['title'] = title
    if xaxis_label:
        fig['layout']['xaxis']['title'] = xaxis_label
    if yaxis_label:
        fig['layout']['yaxis']['title'] = yaxis_label
    if legend_size:
        fig['layout']['legend']['font']['size'] = legend_size
    if extra_layout:
        fig['layout'].update(extra_layout)

    if as_traces:
        return traces

    return fig


def save_fig(fig, filename):
    """
    Save figure to png
    """
    import plotly.io as pio
    pio.write_image(fig, format="png", file=filename)
