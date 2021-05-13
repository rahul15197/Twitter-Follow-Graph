#! /usr/bin/env python
#  -*- coding: utf-8 -*-
"""Responsible for displaying output of Community detection algorithms
(leiden, surprise, walktrap) and Pagerank for twitter and facebook dataset"""
import pickle
import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import advanced_support

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = tk.Tk()
    advanced_support.set_Tk_var()
    top = Toplevel1(root)
    advanced_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    """Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' ."""
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    advanced_support.set_Tk_var()
    top = Toplevel1(w)
    advanced_support.init(w, top, *args, **kwargs)
    return w, top


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    # based on the dataset selected on main screen and analysis selected on this screen
    # load pickle and create subplots
    def show_analysis(self):
        analysis_name = str(self.TCombobox1.get())
        dataset_file = open('dataset_pickle', 'rb')
        selected_dataset = pickle.load(dataset_file)
        dataset_file.close()
        if selected_dataset == 'Twitter' or selected_dataset == 'Twitter-Ego':
            # for communities formed using leiden algorithm
            if analysis_name == 'Communities (Leiden algo)':
                # load communities pickle
                pickle_file = open('communities.pkl', 'rb')
                communities = pickle.load(pickle_file)
                leiden = communities['leiden']
                # create subplots for each community wordcloud
                n = len(leiden)
                columns = int(np.ceil(n / 2))
                rows = int(np.ceil(n / columns))
                fig, axs = plt.subplots(nrows=rows, ncols=columns)
                row, column = 0, 0
                for i in range(rows):
                    for j in range(columns):
                        axs[i, j].axis('off')
                community_count = 1
                for community in leiden:
                    d = {}
                    for c in community:
                        d[c[0]] = c[1]
                    wordcloud = WordCloud(font_path='C:/Windows/Fonts/msyh.ttc', background_color='white')
                    wordcloud.generate_from_frequencies(frequencies=d)
                    if column == columns:
                        row += 1
                        column = 0
                    axs[row, column].title.set_text(f'Community #{community_count}')
                    community_count += 1
                    axs[row, column].plot()
                    axs[row, column].imshow(wordcloud, interpolation="bilinear")
                    column += 1
                # plot properties
                plt.suptitle(f"{selected_dataset} {analysis_name}", fontsize=20, fontweight='bold')
                # make plot screen fullscreen
                plt.get_current_fig_manager().window.state('zoomed')
                # arrange the subplots in a better way
                fig.tight_layout()
                plt.show()

            # for communities formed using surprise communities
            if analysis_name == 'Communities (Surprise communities)':
                pickle_file = open('communities.pkl', 'rb')
                communities = pickle.load(pickle_file)
                surprise = communities['surprise_communities']
                n = len(surprise)
                columns = int(np.ceil(n / 2))
                rows = int(np.ceil(n / columns))
                fig, axs = plt.subplots(nrows=rows, ncols=columns)
                row, column = 0, 0
                for i in range(rows):
                    for j in range(columns):
                        axs[i, j].axis('off')
                community_count = 1
                for community in surprise:
                    d = {}
                    for c in community:
                        d[c[0]] = c[1]
                    wordcloud = WordCloud(font_path='C:/Windows/Fonts/msyh.ttc', background_color='white')
                    wordcloud.generate_from_frequencies(frequencies=d)
                    if column == columns:
                        row += 1
                        column = 0
                    axs[row, column].title.set_text(f'Community #{community_count}')
                    community_count += 1
                    axs[row, column].plot()
                    axs[row, column].imshow(wordcloud, interpolation="bilinear")
                    column += 1
                plt.suptitle(f"{selected_dataset} {analysis_name}", fontsize=20, fontweight='bold')
                plt.get_current_fig_manager().window.state('zoomed')
                fig.tight_layout()
                plt.show()

            # for communities formed using walktrap algo
            if analysis_name == 'Communities (walktrap)':
                pickle_file = open('communities.pkl', 'rb')
                communities = pickle.load(pickle_file)
                walktrap = communities['walktrap']
                n = len(walktrap)
                columns = int(np.ceil(n / 2))
                rows = int(np.ceil(n / columns))
                fig, axs = plt.subplots(nrows=rows, ncols=columns)
                row, column = 0, 0
                for i in range(rows):
                    for j in range(columns):
                        axs[i, j].axis('off')
                community_count = 1
                for community in walktrap:
                    d = {}
                    for c in community:
                        d[c[0]] = c[1]
                    wordcloud = WordCloud(font_path='C:/Windows/Fonts/msyh.ttc', background_color='white')
                    wordcloud.generate_from_frequencies(frequencies=d)
                    if column == columns:
                        row += 1
                        column = 0
                    axs[row, column].title.set_text(f'Community #{community_count}')
                    community_count += 1
                    axs[row, column].plot()
                    axs[row, column].imshow(wordcloud, interpolation="bilinear")
                    column += 1
                plt.suptitle(f"{selected_dataset} {analysis_name}", fontsize=20, fontweight='bold')
                plt.get_current_fig_manager().window.state('zoomed')
                fig.tight_layout()
                plt.show()

            # page rank output plot
            # contains images, name, followers for each person
            if analysis_name == 'Page Rank (Verified Accounts)':
                pickle_file = open('pagerank.pkl', 'rb')
                pagerank_file = pickle.load(pickle_file)
                pagerank1 = pagerank_file['pagerank'][:6]
                pagerank2 = pagerank_file['pagerank'][6:12]
                pagerank3 = pagerank_file['pagerank'][12:]
                columns = 3
                rows = 2
                fig, axs = plt.subplots(nrows=rows, ncols=columns)
                row, column = 0, 0
                for i in range(rows):
                    for j in range(columns):
                        axs[i, j].axis('off')
                rank_count = 1
                for rank in pagerank1:
                    if column == columns:
                        row += 1
                        column = 0
                    image = Image.open(f'PageRankImages/{rank[0]}.png')
                    axs[row, column].title.set_text(f'Rank #{rank_count}\nName: {rank[0]}\nFollowers: {rank[1]}')
                    axs[row, column].imshow(image, interpolation="bilinear")
                    rank_count += 1
                    column += 1
                plt.suptitle(f"{selected_dataset} {analysis_name}", fontsize=20, fontweight='bold')
                plt.get_current_fig_manager().window.state('zoomed')
                fig.tight_layout()
                plt.show()
                columns = 3
                rows = 2
                fig, axs = plt.subplots(nrows=rows, ncols=columns)
                row, column = 0, 0
                for i in range(rows):
                    for j in range(columns):
                        axs[i, j].axis('off')
                for rank in pagerank2:
                    if column == columns:
                        row += 1
                        column = 0
                    image = Image.open(f'PageRankImages/{rank[0]}.png')
                    axs[row, column].title.set_text(f'Rank #{rank_count}\nName: {rank[0]}\nFollowers: {rank[1]}')
                    axs[row, column].imshow(image, interpolation="bilinear")
                    rank_count += 1
                    column += 1
                plt.suptitle(f"{selected_dataset} {analysis_name}", fontsize=20, fontweight='bold')
                plt.get_current_fig_manager().window.state('zoomed')
                fig.tight_layout()
                plt.show()
                columns = 3
                rows = 2
                fig, axs = plt.subplots(nrows=rows, ncols=columns)
                row, column = 0, 0
                for i in range(rows):
                    for j in range(columns):
                        axs[i, j].axis('off')
                for rank in pagerank3:
                    if column == columns:
                        row += 1
                        column = 0
                    image = Image.open(f'PageRankImages/{rank[0]}.png')
                    axs[row, column].title.set_text(f'Rank #{rank_count}\nName: {rank[0]}\nFollowers: {rank[1]}')
                    axs[row, column].imshow(image, interpolation="bilinear")
                    rank_count += 1
                    column += 1
                plt.suptitle(f"{selected_dataset} {analysis_name}", fontsize=20, fontweight='bold')
                plt.get_current_fig_manager().window.state('zoomed')
                fig.tight_layout()
                plt.show()
        if selected_dataset == 'Facebook':
            if analysis_name == 'Communities (Leiden algo)':
                pickle_file = open('fbcommunities.pkl', 'rb')
                communities = pickle.load(pickle_file)
                leiden = communities['leiden'][:10]
                n = len(leiden)
                columns = int(np.ceil(n / 2))
                rows = int(np.ceil(n / columns))
                fig, axs = plt.subplots(nrows=rows, ncols=columns)
                row, column = 0, 0
                for i in range(rows):
                    for j in range(columns):
                        axs[i, j].axis('off')
                community_count = 1
                for community in leiden:
                    d = {}
                    for c in community:
                        d[c[0]] = c[2]
                    wordcloud = WordCloud(font_path='C:/Windows/Fonts/msyh.ttc', background_color='white')
                    wordcloud.generate_from_frequencies(frequencies=d)
                    if column == columns:
                        row += 1
                        column = 0
                    axs[row, column].title.set_text(f'Community #{community_count}')
                    community_count += 1
                    axs[row, column].plot()
                    axs[row, column].imshow(wordcloud, interpolation="bilinear")
                    column += 1
                plt.suptitle(f"{selected_dataset} {analysis_name}", fontsize=20, fontweight='bold')
                plt.get_current_fig_manager().window.state('zoomed')
                fig.tight_layout()
                plt.show()

            if analysis_name == 'Communities (walktrap)':
                pickle_file = open('fbcommunities.pkl', 'rb')
                communities = pickle.load(pickle_file)
                walktrap = communities['walktrap'][:10]
                n = len(walktrap)
                columns = int(np.ceil(n / 2))
                rows = int(np.ceil(n / columns))
                fig, axs = plt.subplots(nrows=rows, ncols=columns)
                row, column = 0, 0
                for i in range(rows):
                    for j in range(columns):
                        axs[i, j].axis('off')
                community_count = 1
                for community in walktrap:
                    d = {}
                    for c in community:
                        d[c[0]] = c[2]
                    wordcloud = WordCloud(font_path='C:/Windows/Fonts/msyh.ttc', background_color='white')
                    wordcloud.generate_from_frequencies(frequencies=d)
                    if column == columns:
                        row += 1
                        column = 0
                    axs[row, column].title.set_text(f'Community #{community_count}')
                    community_count += 1
                    axs[row, column].plot()
                    axs[row, column].imshow(wordcloud, interpolation="bilinear")
                    column += 1
                plt.suptitle(f"{selected_dataset} {analysis_name}", fontsize=20, fontweight='bold')
                plt.get_current_fig_manager().window.state('zoomed')
                fig.tight_layout()
                plt.show()
            if analysis_name == 'Page Rank':
                pickle_file = open('fbpagerank.pkl', 'rb')
                pagerank_file = pickle.load(pickle_file)
                pagerank1 = pagerank_file['pagerank'][:5]
                pagerank2 = pagerank_file['pagerank'][5:10]
                pagerank3 = pagerank_file['pagerank'][10:]
                columns = 3
                rows = 2
                fig, axs = plt.subplots(nrows=rows, ncols=columns)
                row, column = 0, 0
                for i in range(rows):
                    for j in range(columns):
                        axs[i, j].axis('off')
                rank_count = 1
                for rank in pagerank1:
                    if column == columns:
                        row += 1
                        column = 0
                    image = Image.open(f'FacebookPageRankImages/{rank[0]}.png')
                    axs[row, column].title.set_text(f'Rank #{rank_count}\nName: {rank[0]}\nCategory: {rank[1]}')
                    axs[row, column].imshow(image, interpolation="bilinear")
                    rank_count += 1
                    column += 1
                plt.suptitle(f"{selected_dataset} {analysis_name}", fontsize=20, fontweight='bold')
                plt.get_current_fig_manager().window.state('zoomed')
                fig.tight_layout()
                plt.show()
                columns = 3
                rows = 2
                fig, axs = plt.subplots(nrows=rows, ncols=columns)
                row, column = 0, 0
                for i in range(rows):
                    for j in range(columns):
                        axs[i, j].axis('off')
                for rank in pagerank2:
                    if column == columns:
                        row += 1
                        column = 0
                    image = Image.open(f'FacebookPageRankImages/{rank[0]}.png')
                    axs[row, column].title.set_text(f'Rank #{rank_count}\nName: {rank[0]}\nCategory: {rank[1]}')
                    axs[row, column].imshow(image, interpolation="bilinear")
                    rank_count += 1
                    column += 1
                plt.suptitle(f"{selected_dataset} {analysis_name}", fontsize=20, fontweight='bold')
                plt.get_current_fig_manager().window.state('zoomed')
                fig.tight_layout()
                plt.show()
                columns = 3
                rows = 2
                fig, axs = plt.subplots(nrows=rows, ncols=columns)
                row, column = 0, 0
                for i in range(rows):
                    for j in range(columns):
                        axs[i, j].axis('off')
                for rank in pagerank3:
                    if column == columns:
                        row += 1
                        column = 0
                    image = Image.open(f'FacebookPageRankImages/{rank[0]}.png')
                    axs[row, column].title.set_text(f'Rank #{rank_count}\nName: {rank[0]}\nCategory: {rank[1]}')
                    axs[row, column].imshow(image, interpolation="bilinear")
                    rank_count += 1
                    column += 1
                plt.suptitle(f"{selected_dataset} {analysis_name}", fontsize=20, fontweight='bold')
                plt.get_current_fig_manager().window.state('zoomed')
                fig.tight_layout()
                plt.show()

    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 14 -weight bold"
        font11 = "-family {MS PGothic} -size 14"
        font12 = "-family {Century Gothic} -size 24 -weight bold"
        font14 = "-family {Microsoft YaHei} -size 16"
        font15 = "-family {Microsoft YaHei} -size 16 -weight bold"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1920x1001+650+150")
        top.attributes("-fullscreen", True)
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#CD6155")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.27, rely=0.12, height=46, width=750)
        self.Label1.configure(background="#CD6155")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Community Detection Algorithms & PageRank''')

        dataset_file = open('dataset_pickle', 'rb')
        selected_dataset = pickle.load(dataset_file)
        dataset_file.close()

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.42, rely=0.19, height=30, width=250)
        self.Label2.configure(background="#CD6155")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text=selected_dataset + ''' dataset''')

        if selected_dataset == 'Twitter' or selected_dataset == 'Twitter-Ego':
            analysis_list = ['Communities (Leiden algo)', 'Communities (Surprise communities)',
                             'Communities (walktrap)',
                             'Page Rank (Verified Accounts)']
        else:
            analysis_list = ['Communities (Leiden algo)',
                             'Communities (walktrap)',
                             'Page Rank']
        self.TCombobox1 = ttk.Combobox(top, values=analysis_list, state='readonly')
        self.TCombobox1.place(relx=0.415, rely=0.34, relheight=0.036
                              , relwidth=0.170)
        self.TCombobox1.configure(font=font10)
        self.TCombobox1.configure(textvariable=advanced_support.combobox)
        self.TCombobox1.configure(takefocus="")

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.452, rely=0.27, height=46, width=150)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#CD6155")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {MS PGothic} -size 14 -weight bold")
        self.Label1_1.configure(foreground="#ffffff")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Select analysis''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.468, rely=0.41, height=43, width=108)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#7B241C")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Submit''')
        self.Button1.configure(command=self.show_analysis)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.932, rely=0.03, height=53, width=68)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ea0f46")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font10)
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''X''')
        self.Button2.configure(command=root.destroy)


if __name__ == '__main__':
    vp_start_gui()
