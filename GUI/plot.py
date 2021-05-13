#! /usr/bin/env python
#  -*- coding: utf-8 -*-
"""Displays degree distribution plots based on the dataset
selected at the main screen."""
import pickle
import sys
import matplotlib.pyplot as plt
import plot_support

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
    plot_support.set_Tk_var()
    top = Toplevel1(root)
    plot_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    """Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' ."""
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    plot_support.set_Tk_var()
    top = Toplevel1(w)
    plot_support.init(w, top, *args, **kwargs)
    return w, top


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    # create plot from dictionary values with keys as x values and values as y values
    def create_plot(self, title, dictionary):
        plt.figure(figsize=(8, 5))
        plt.title(title, fontsize=12)
        plt.xlabel("Degree (k)")
        plt.ylabel("Fraction of Nodes")
        plt.scatter(list(dictionary.keys()), list(dictionary.values()), marker='.')
        plt.loglog()

    # based on the selected dataset create plots from corresponding pickle
    def make_plot(self):
        plot_name = str(self.TCombobox1.get())
        dataset_file = open('dataset_pickle', 'rb')
        selected_dataset = pickle.load(dataset_file)
        dataset_file.close()
        if selected_dataset == "LinkedIn":
            if plot_name == 'Degree Distribution':
                # load giant component pickle
                plot_file_giant = open('Linkedin/degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                # giant component degree dist plot
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                # load degree distribution pickle
                plot_file = open('Linkedin/degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                # degree distribution plot
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Cumulative Degree Distribution':
                plot_file_giant = open('Linkedin/cummulative_degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Linkedin/cummulative_degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
        if selected_dataset == "Facebook (Athletes)":
            if plot_name == 'Degree Distribution':
                plot_file_giant = open('Facebook_Athletes/degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Facebook_Athletes/degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Cumulative Degree Distribution':
                plot_file_giant = open('Facebook_Athletes/cummulative_degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Facebook_Athletes/cummulative_degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
        if selected_dataset == "Facebook (Politician)":
            if plot_name == 'Degree Distribution':
                plot_file_giant = open('Facebook_Politician/degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Facebook_Politician/degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Cumulative Degree Distribution':
                plot_file_giant = open('Facebook_Politician/cummulative_degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Facebook_Politician/cummulative_degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
        if selected_dataset == "Facebook (Public Figure)":
            if plot_name == 'Degree Distribution':
                plot_file_giant = open('Facebook_Public_Figure/degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Facebook_Public_Figure/degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Cumulative Degree Distribution':
                plot_file_giant = open('Facebook_Public_Figure/cummulative_degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Facebook_Public_Figure/cummulative_degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
        if selected_dataset == "Twitch (ENGB)":
            if plot_name == 'Degree Distribution':
                plot_file_giant = open('Twitch_ENGB/degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Twitch_ENGB/degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Cumulative Degree Distribution':
                plot_file_giant = open('Twitch_ENGB/cummulative_degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Twitch_ENGB/cummulative_degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
        if selected_dataset == "Twitch (FR)":
            if plot_name == 'Degree Distribution':
                plot_file_giant = open('Twitch_FR/degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Twitch_FR/degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Cumulative Degree Distribution':
                plot_file_giant = open('Twitch_FR/cummulative_degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Twitch_FR/cummulative_degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
        if selected_dataset == "Flickr":
            if plot_name == 'Degree Distribution':
                plot_file_giant = open('Flickr/degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Flickr/degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Cumulative Degree Distribution':
                plot_file_giant = open('Flickr/cummulative_degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Flickr/cummulative_degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
        if selected_dataset == "Facebook":
            if plot_name == 'Degree Distribution':
                plot_file_giant = open('Facebook/degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Facebook/degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Cumulative Degree Distribution':
                plot_file_giant = open('Facebook/cummulative_degree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Facebook/cummulative_degree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
        if selected_dataset == "Twitter":
            if plot_name == 'Cumulative In-Degree Distribution':
                plot_file_giant = open('Twitter/cummulative_indegree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Twitter/cummulative_indegree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Cumulative Out-Degree Distribution':
                plot_file_giant = open('Twitter/cummulative_outdegree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Twitter/cummulative_outdegree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'In-Degree Distribution':
                plot_file_giant = open('Twitter/indegree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Twitter/indegree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Out-Degree Distribution':
                plot_file_giant = open('Twitter/outdegree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Twitter/outdegree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
        if selected_dataset == "Twitter-Ego":
            if plot_name == 'Cumulative In-Degree Distribution':
                plot_file_giant = open('Twitter_Ego/cummulative_indegree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Twitter_Ego/cummulative_indegree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Cumulative Out-Degree Distribution':
                plot_file_giant = open('Twitter_Ego/cummulative_outdegree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Twitter_Ego/cummulative_outdegree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'In-Degree Distribution':
                plot_file_giant = open('Twitter_Ego/indegree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Twitter_Ego/indegree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Out-Degree Distribution':
                plot_file_giant = open('Twitter_Ego/outdegree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Twitter_Ego/outdegree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
        if selected_dataset == "EU Email":
            if plot_name == 'Cumulative In-Degree Distribution':
                plot_file_giant = open('Email/cummulative_indegree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Email/cummulative_indegree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Cumulative Out-Degree Distribution':
                plot_file_giant = open('Email/cummulative_outdegree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Email/cummulative_outdegree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'In-Degree Distribution':
                plot_file_giant = open('Email/indegree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Email/indegree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
                plt.show()
            if plot_name == 'Out-Degree Distribution':
                plot_file_giant = open('Email/outdegree_distribution_giant', 'rb')
                plot_giant = pickle.load(plot_file_giant)
                plot_file_giant.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset) (Giant Component)", plot_giant)
                plot_file = open('Email/outdegree_distribution', 'rb')
                plot = pickle.load(plot_file)
                plot_file.close()
                self.create_plot(f"{plot_name} ({selected_dataset} dataset)", plot)
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
        top.configure(background="#884EA0")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.464, rely=0.12, height=46, width=111)
        self.Label1.configure(background="#884EA0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Plots''')

        dataset_file = open('dataset_pickle', 'rb')
        selected_dataset = pickle.load(dataset_file)
        dataset_file.close()

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.42, rely=0.19, height=30, width=250)
        self.Label2.configure(background="#884EA0")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text=selected_dataset + ''' dataset''')

        if selected_dataset == 'EU Email' or selected_dataset == 'Twitter' or selected_dataset == 'Twitter-Ego':
            plot_list = ['In-Degree Distribution',
                         'Out-Degree Distribution', 'Cumulative In-Degree Distribution',
                         'Cumulative Out-Degree Distribution']
        else:
            plot_list = ['Degree Distribution', 'Cumulative Degree Distribution']
        self.TCombobox1 = ttk.Combobox(top, values=plot_list, state='readonly')
        self.TCombobox1.place(relx=0.415, rely=0.35, relheight=0.036
                              , relwidth=0.170)
        self.TCombobox1.configure(font=font10)
        self.TCombobox1.configure(textvariable=plot_support.combobox)
        self.TCombobox1.configure(takefocus="")

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.464, rely=0.27, height=46, width=111)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#884EA0")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {MS PGothic} -size 14 -weight bold")
        self.Label1_1.configure(foreground="#ffffff")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Select plot''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.464, rely=0.42, height=43, width=108)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#5B2C6F")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Plot''')
        self.Button1.configure(command=self.make_plot)

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
