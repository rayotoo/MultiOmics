#!/usr/bin/env python3

import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from numpy import arange, fabs
from collections import defaultdict
import argparse

colors = ['r', 'g', 'b', 'm', 'c', 'y', 'k']

def read_params(args):
    parser = argparse.ArgumentParser(description='Plot results')
    parser.add_argument('input_file', metavar='INPUT_FILE', type=str, help="tab delimited input file")
    parser.add_argument('output_file', metavar='OUTPUT_FILE', type=str, help="the file for the output image")
    parser.add_argument('--feature_font_size', dest="feature_font_size", type=int, default=7, help="font size of feature labels")
    parser.add_argument('--format', dest="format", choices=["png","svg","pdf"], default='png', type=str, help="the format for the output file")
    parser.add_argument('--dpi', dest="dpi", type=int, default=600)  # Set default DPI to 600
    parser.add_argument('--title', dest="title", type=str, default="")
    parser.add_argument('--title_font_size', dest="title_font_size", type=str, default="12")
    parser.add_argument('--class_legend_font_size', dest="class_legend_font_size", type=str, default="10")
    parser.add_argument('--width', dest="width", type=float, default=7.0)
    parser.add_argument('--height', dest="height", type=float, default=4.0, help="only for vertical histograms")
    parser.add_argument('--left_space', dest="ls", type=float, default=0.2)
    parser.add_argument('--right_space', dest="rs", type=float, default=0.1)
    parser.add_argument('--orientation', dest="orientation", type=str, choices=["h","v"], default="h")
    parser.add_argument('--autoscale', dest="autoscale", type=int, choices=[0,1], default=1)
    parser.add_argument('--background_color', dest="back_color", type=str, choices=["k","w"], default="w", help="set the color of the background")
    parser.add_argument('--subclades', dest="n_scl", type=int, default=1, help="number of label levels to be displayed (starting from the leaves, -1 means all the levels, 1 is default)")
    parser.add_argument('--max_feature_len', dest="max_feature_len", type=int, default=60, help="Maximum length of feature strings (default 60)")
    parser.add_argument('--all_feats', dest="all_feats", type=str, default="")
    parser.add_argument('--otu_only', dest="otu_only", default=False, action='store_true', help="Plot only species resolved OTUs (as opposed to all levels)")
    parser.add_argument('--report_features', dest="report_features", default=False, action='store_true', help="Report important features to STDOUT")
    args = parser.parse_args()
    return vars(args)

def read_data(input_file, otu_only):
    with open(input_file, 'r') as inp:
        if not otu_only:
            rows = [line.strip().split()[:-1] for line in inp.readlines() if len(line.strip().split()) > 3]
        else:
            rows = [line.strip().split()[:-1] for line in inp.readlines() if len(line.strip().split()) > 3 and len(line.strip().split()[0].split('.')) == 8]  # a feature with length 8 will have an OTU id associated with it
    classes = list(set([v[2] for v in rows if len(v) > 2]))
    if len(classes) < 1:
        print("No differentially abundant features found in " + input_file)
        sys.exit()
    data = {'rows': rows, 'cls': classes}
    return data

def plot_histo_hor(path, params, data, bcl, report_features):
    cls2 = []
    if params['all_feats'] != "":
        cls2 = sorted(params['all_feats'].split(":"))
    cls = sorted(data['cls'])
    if bcl:
        data['rows'].sort(key=lambda ab: fabs(float(ab[3])) * (cls.index(ab[2]) * 2 - 1))
    else:
        mmax = max([fabs(float(a)) for a in list(zip(*list(data['rows'])))[3]])
        data['rows'].sort(key=lambda ab: fabs(float(ab[3])) / mmax + (cls.index(ab[2]) + 1))
    pos = arange(len(data['rows']))
    head = 0.75
    tail = 0.5
    ht = head + tail
    ints = max(len(pos) * 0.2, 1.5)
    fig = plt.figure(figsize=(params['width'], ints + ht), edgecolor=params['back_color'], facecolor=params['back_color'])
    ax = fig.add_subplot(111, frame_on=False, facecolor=params['back_color'])
    ls, rs = params['ls'], 1.0 - params['rs']
    plt.subplots_adjust(left=ls, right=rs, top=1 - head * (1.0 - ints / (ints + ht)), bottom=tail * (1.0 - ints / (ints + ht)))

    fig.canvas.manager.set_window_title('LDA results')

    l_align = {'horizontalalignment':'left', 'verticalalignment':'baseline'}
    r_align = {'horizontalalignment':'right', 'verticalalignment':'baseline'}
    added = []
    m = 1 if data['rows'][0][2] == cls[0] else -1
    out_data = defaultdict(list)  # keep track of which OTUs result in the plot
    for i, v in enumerate(data['rows']):
        if report_features:
            otu = v[0].split('.')[7].replace('_', '.')  # string replace retains format New.ReferenceOTUxxx
            score = v[3]
            otu_class = v[2]
            out_data[otu] = [score, otu_class]
        indcl = cls.index(v[2])
        lab = str(v[2]) if str(v[2]) not in added else ""
        added.append(str(v[2]))
        col = colors[indcl % len(colors)]
        if len(cls2) > 0:
            col = colors[cls2.index(v[2]) % len(colors)]
        vv = fabs(float(v[3])) * (m * (indcl * 2 - 1)) if bcl else fabs(float(v[3]))
        ax.barh(pos[i], vv, align='center', color=col, label=lab, height=0.8)
    mv = max([abs(float(v[3])) for v in data['rows']])
    if report_features:
        print('OTU\tLDA_score\tClass')
        for i in out_data:
            print('%s\t%s\t%s' % (i, out_data[i][0], out_data[i][1]))
    for i, r in enumerate(data['rows']):
        indcl = cls.index(data['rows'][i][2])
        if params['n_scl'] < 0:
            rr = r[0]
        else:
            rr = ".".join(r[0].split(".")[-params['n_scl']:])
        if len(rr) > params['max_feature_len']:
            rr = rr[:params['max_feature_len'] // 2 - 2] + " [..]" + rr[-params['max_feature_len'] // 2 + 2:]
        if m * (indcl * 2 - 1) < 0 and bcl:
            ax.text(mv / 40.0, float(i) - 0.3, rr, l_align, size=params['feature_font_size'], color='black')  # Change color to black
        else:
            ax.text(-mv / 40.0, float(i) - 0.3, rr, r_align, size=params['feature_font_size'], color='black')  # Change color to black
    ax.set_title(params['title'], size=params['title_font_size'], y=1.0 + head * (1.0 - ints / (ints + ht)) * 0.8, color='black')  # Change color to black

    ax.set_yticks([])
    ax.set_xlabel("LDA SCORE (log 10)")
    ax.xaxis.grid(True)
    xlim = ax.get_xlim()
    if params['autoscale']:
        ran = arange(0.0001, round(round((abs(xlim[0]) + abs(xlim[1])) / 10, 4) * 100, 0) / 100)
        if len(ran) > 1 and len(ran) < 100:
            ax.set_xticks(arange(xlim[0], xlim[1] + 0.0001, min(xlim[1] + 0.0001, round(round((abs(xlim[0]) + abs(xlim[1])) / 10, 4) * 100, 0) / 100)))
    ax.set_ylim((pos[0] - 0.5, pos[-1] + 0.5))
    ax.axvline(color='black')
    leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=len(cls), fancybox=True, prop={'size':params['class_legend_font_size']})
    leg.get_frame().set_alpha(0.5)
    for label in leg.get_texts():
        label.set_color('black')  # Change legend text color to black
    plt.savefig(path, facecolor=params['back_color'], dpi=params['dpi'], format=params['format'])

if __name__ == "__main__":
    params = read_params(sys.argv)
    data = read_data(params['input_file'], params['otu_only'])
    plot_histo_hor(params['output_file'], params, data, bcl=True, report_features=params['report_features'])
