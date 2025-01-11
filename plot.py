# -*- coding: utf-8 -*-
import matplotlib.cm as cm
import matplotlib.patches as patches
import matplotlib.dates as mdates
import matplotlib.ticker as ticker  # FormatterとLocatorはTickerモジュールが必要
import os
import sys
import pandas as pd
import numpy as np
import shutil

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Agg')

# colors: 0:空色　1: 潤色 2: 若緑　3: 蜂蜜色 4: 浅紫 5: 紅梅色　6: 柳色　7: 萱草色　8: コスモス 9: レタスグリーン
#         10: lightgreen 11: tan 12: ピンク 13: コーラルレッド 14: ウイスタリア 15: ライムライト 16: オパールグリーン 17: ライトブルー 18: 薄葡萄 19: 淡黄
#         20: フロンティホワイト 21: ヒヤシンスブルー 22: ブロンド 23: アスパラガスグリーン 24: カナリヤ 25: アクアグリーン 26: アッシュグレイ 27: ローズグレイ 28: デイドリーム 29: ブルーラベンダー
#         30: クリームイエロー 31: ローズドラジェ
colors = [
    '#89c3eb', '#c8c2be', '#98d98e', '#fddea5', '#c4a3bf',
    '#f2a0a1', '#a8c97f', '#f8b862', '#dc6b9a', '#d1de4c',
    '#90ee90', '#d2b48c', '#f5b2b2', '#ef857d', '#8d93c8',
    '#fff799', '#bee0ce', '#b2cbe4', '#c0a2c7', '#f8e58c',
    '#e6eae6', '#7a99cf', '#f2d58a', '#dbebc4', '#fff462',
    '#88bfbf', '#9fa09e', '#9d8e87', '#a3b9e0', '#a4a8d4',
    '#fff3b8', '#e5c1cd'
]


def make_dir(path):
    dirs = path.split('/')
    c_path = ''
    for dirname in dirs:
        c_path = os.path.join(c_path, dirname)
        if not os.path.exists(c_path):
            os.mkdir(c_path)


def remove_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def init_dir(path):
    remove_dir(path)
    make_dir(path)


def sub_fig(ax, X, regime_list):
    df = pd.DataFrame(X)
    ax.set_xlim(0, len(df))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1000))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(10000))
    ax.set_yticks([])
    df.plot(ax=ax, legend=False)

    ax.tick_params(labelleft=False, direction='in')

    for regime_id, regime in enumerate(regime_list):
        for seg_idx in range(regime.n_seg):
            st = regime.seg_list[seg_idx][0]
            ed = sum(regime.seg_list[seg_idx])

            r = patches.Rectangle(
                xy=(int(st), ax.get_ylim()[0]),
                width=(int(ed) - int(st) + 1),
                height=abs(ax.get_ylim()[0]) +
                ax.get_ylim()[1],
                fc=colors[regime_id],
                ec='black',
                linewidth=int(1),
                fill=True)
            ax.add_patch(r)
    return ax

def make_fig(output_dir, X, regime_list):
    # set xtick to top
    plt.rcParams['xtick.top'] = True
    # make graph
    fig, ax = plt.subplots(
        nrows=1,
        ncols=1,
        figsize=(20, 10),
        constrained_layout=True,
    )
    ax = sub_fig(ax, X, regime_list)  # plot create

    # save fig
    time_series_path = os.path.join(output_dir, 'result.png')
    #plt.show()  # 先显示绘图
    plt.savefig(time_series_path)  # 再保存图像
    plt.close()
    print('saved')


def plot_fig(output_dir, X, regime_list):
    # make dir
    init_dir(output_dir)

    # make figure
    make_fig(output_dir, X, regime_list)

    print(f"finished")
