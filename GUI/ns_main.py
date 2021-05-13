"""This file corresponds to the main screen of the GUI (master screen)
Properties of the datasets and corresponding property images are shown
using this screen. It calls plots and advanced screen based on the dataset selected"""

import pickle
import sys
from tkinter import END, NORMAL
import pandas as pd
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import advanced as ad
import plot as pl

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

import ns_main_support


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = tk.Tk()
    ns_main_support.set_Tk_var()
    top = Toplevel1(root)
    ns_main_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    """Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' ."""
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    ns_main_support.set_Tk_var()
    top = Toplevel1(w)
    ns_main_support.init(w, top, *args, **kwargs)
    return w, top


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    # calls advanced screen (community analysis and page rank)
    def advanced_screen(self):
        # save the selected dataset (used in the corresponding screen)
        selected_dataset = self.dataset_dropdown.get()
        dataset_file = open('dataset_pickle', 'wb')
        pickle.dump(selected_dataset, dataset_file)
        dataset_file.close()
        ad.vp_start_gui()

    # calls plots screen (degree distribution plots)
    def plot_screen(self):
        # save the selected dataset (used in the corresponding screen)
        selected_dataset = self.dataset_dropdown.get()
        dataset_file = open('dataset_pickle', 'wb')
        pickle.dump(selected_dataset, dataset_file)
        dataset_file.close()
        pl.vp_start_gui()

    # all directed network degree distribution comparison plot
    def create_directed_comparison_plot(self, title, dictionary):
        plt.figure(figsize=(8, 5))
        plt.title(title, fontsize=12)
        plt.xlabel("Degree (k)")
        plt.ylabel("Fraction of Nodes")
        for key in dictionary.keys():
            plt.scatter(list(dictionary[key].keys()), list(dictionary[key].values()), marker='.')
            plt.loglog()
        plt.legend(['Email', 'Twitter', 'Twitter-Ego'])

    # all undirected network degree distribution comparison plot
    def create_undirected_comparison_plot(self, title, dictionary):
        plt.figure(figsize=(8, 5))
        plt.title(title, fontsize=12)
        plt.xlabel("Degree (k)")
        plt.ylabel("Fraction of Nodes")
        for key in dictionary.keys():
            plt.scatter(list(dictionary[key].keys()), list(dictionary[key].values()), marker='.')
            plt.loglog()
        plt.legend(['Facebook Athletes', 'Facebook_Politician', 'Facebook Public_Figure',
                    'Flickr', 'Linkedin', 'Twitch (ENGB)', 'Twitch (FR)'])

    # invoked when a value from drop down is selected
    # based on the value selected, logo image is shown on top right,
    # properties in scrolledtextbox and network gephi image in mid right screen
    def callback(self, eventObject):
        # clear scrolledtextbox everytime a new value is selected
        self.Scrolledtext1.configure(state=NORMAL)
        self.Scrolledtext1.delete('1.0', END)
        selected_dataset = self.dataset_dropdown.get()
        directed_graphs_df = pd.read_csv("Directed Graphs Properties.csv")
        undirected_graphs_df = pd.read_csv("Undirected Graphs Properties.csv")

        if selected_dataset == 'Twitter':
            # display top left logo image
            image1 = Image.open("twitter.png")
            image1.putalpha(256)
            test = ImageTk.PhotoImage(image1)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=10, y=10)

            # display mid right gephi network image
            image2 = Image.open("Gephi/Twitter.png")
            dimensions = (470, 420)
            image3 = image2.resize(dimensions)
            test = ImageTk.PhotoImage(image3)
            label2 = tk.Label(image=test)
            label2.image = test
            label2.place(x=1050, y=305)

            # show properties in scrolledtextbox
            dataset = directed_graphs_df.iloc[0]
            self.Scrolledtext1.insert(tk.INSERT, f"\n{selected_dataset} dataset properties\n")
            self.Scrolledtext1.insert(tk.INSERT, f"\n1. Number of Nodes = {int(dataset['Number of Nodes'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n2. Number of Edges = {int(dataset['Number of Edges'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n3. Number of weakly connected components = {int(dataset['Number of weakly connected components'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n4. Size of largest weakly connected component = {int(dataset['Size of largest weakly connected component'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n5. Average Path Length = {dataset['Average Path Length']}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n6. Average Clustering Coeffcient = {dataset['Average Clustering Coeffcient']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n7. Degree Assortativity = {dataset['Degree Assortavity ']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n8. Diameter = {dataset['Diameter']}")
            # make scrolledtextbox read-only
            self.Scrolledtext1.configure(state='disabled')

            self.advanced_button.configure(background="#1222b1")
            self.advanced_button.configure(state='normal')
            self.plots_button.configure(background="#1222b1")
            self.plots_button.configure(state='normal')

        if selected_dataset == 'Twitter-Ego':
            image1 = Image.open("twitter.png")
            image1.putalpha(256)
            test = ImageTk.PhotoImage(image1)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=10, y=10)

            image2 = Image.open("Gephi/Twitter_Ego.png")
            dimensions = (470, 420)
            image3 = image2.resize(dimensions)
            test = ImageTk.PhotoImage(image3)
            label2 = tk.Label(image=test)
            label2.image = test
            label2.place(x=1050, y=305)

            dataset = directed_graphs_df.iloc[1]
            self.Scrolledtext1.insert(tk.INSERT, f"\n{selected_dataset} dataset properties\n")
            self.Scrolledtext1.insert(tk.INSERT, f"\n1. Number of Nodes = {int(dataset['Number of Nodes'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n2. Number of Edges = {int(dataset['Number of Edges'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n3. Average Path Length = {dataset['Average Path Length']}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n4. Average Clustering Coeffcient = {dataset['Average Clustering Coeffcient']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n5. Degree Assortativity = {dataset['Degree Assortavity ']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n6. Diameter = {dataset['Diameter']}")

            self.Scrolledtext1.configure(state='disabled')

            self.advanced_button.configure(background="#1222b1")
            self.advanced_button.configure(state='normal')
            self.plots_button.configure(background="#1222b1")
            self.plots_button.configure(state='normal')

        if selected_dataset == 'Twitch (FR)':
            image1 = Image.open("twitch.jpg")
            image1.putalpha(256)
            test = ImageTk.PhotoImage(image1)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=10, y=10)

            image2 = Image.open("Gephi/Twitch_FR.png")
            dimensions = (470, 420)
            image3 = image2.resize(dimensions)
            test = ImageTk.PhotoImage(image3)
            label2 = tk.Label(image=test)
            label2.image = test
            label2.place(x=1050, y=305)

            dataset = undirected_graphs_df.iloc[0]
            self.Scrolledtext1.insert(tk.INSERT, f"\n{selected_dataset} dataset properties\n")
            self.Scrolledtext1.insert(tk.INSERT, f"\n1. Number of Nodes = {int(dataset['Number of Nodes'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n2. Number of Edges = {int(dataset['Number of Edges'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n3. Number of connected components = {int(dataset['Number of connected components'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n4. Size of largest connected component = {int(dataset['Size of largest connected component'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n5. Average Path Length = {dataset['Average Path Length']}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n6. Average Clustering Coeffcient = {dataset['Average Clustering Coeffcient']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n7. Degree Assortativity = {dataset['Degree Assortavity ']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n8. Diameter = {dataset['Diameter']}")

            self.Scrolledtext1.configure(state='disabled')

            self.advanced_button.configure(background="#D5D8DC")
            self.advanced_button.configure(state='disabled')
            self.plots_button.configure(background="#1222b1")
            self.plots_button.configure(state='normal')

        if selected_dataset == 'Twitch (ENGB)':
            image1 = Image.open("twitch.jpg")
            image1.putalpha(256)
            test = ImageTk.PhotoImage(image1)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=10, y=10)

            image2 = Image.open("Gephi/Twitch_ENGB.png")
            dimensions = (470, 420)
            image3 = image2.resize(dimensions)
            test = ImageTk.PhotoImage(image3)
            label2 = tk.Label(image=test)
            label2.image = test
            label2.place(x=1050, y=305)

            dataset = undirected_graphs_df.iloc[1]
            self.Scrolledtext1.insert(tk.INSERT, f"\n{selected_dataset} dataset properties\n")
            self.Scrolledtext1.insert(tk.INSERT, f"\n1. Number of Nodes = {int(dataset['Number of Nodes'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n2. Number of Edges = {int(dataset['Number of Edges'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n3. Number of connected components = {int(dataset['Number of connected components'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n4. Size of largest connected component = {int(dataset['Size of largest connected component'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n5. Average Path Length = {dataset['Average Path Length']}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n6. Average Clustering Coeffcient = {dataset['Average Clustering Coeffcient']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n7. Degree Assortativity = {dataset['Degree Assortavity ']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n8. Diameter = {dataset['Diameter']}")

            self.Scrolledtext1.configure(state='disabled')

            self.advanced_button.configure(background="#D5D8DC")
            self.advanced_button.configure(state='disabled')
            self.plots_button.configure(background="#1222b1")
            self.plots_button.configure(state='normal')

        if selected_dataset == 'Facebook':
            image1 = Image.open("facebook.jpg")
            image1.putalpha(256)
            test = ImageTk.PhotoImage(image1)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=10, y=10)

            image2 = Image.open("Gephi/Facebook.png")
            dimensions = (470, 420)
            image3 = image2.resize(dimensions)
            test = ImageTk.PhotoImage(image3)
            label2 = tk.Label(image=test)
            label2.image = test
            label2.place(x=1050, y=305)

            dataset = undirected_graphs_df.iloc[7]
            self.Scrolledtext1.insert(tk.INSERT, f"\n{selected_dataset} dataset properties\n")
            self.Scrolledtext1.insert(tk.INSERT, f"\n1. Number of Nodes = {int(dataset['Number of Nodes'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n2. Number of Edges = {int(dataset['Number of Edges'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n3. Number of connected components = {int(dataset['Number of connected components'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n4. Size of largest connected component = {int(dataset['Size of largest connected component'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n5. Average Clustering Coeffcient = {dataset['Average Clustering Coeffcient']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n6. Degree Assortativity = {dataset['Degree Assortavity ']}")

            self.Scrolledtext1.configure(state='disabled')

            self.advanced_button.configure(background="#1222b1")
            self.advanced_button.configure(state='normal')
            self.plots_button.configure(background="#1222b1")
            self.plots_button.configure(state='normal')

        if selected_dataset == 'Facebook (Athletes)':
            image1 = Image.open("facebook.jpg")
            image1.putalpha(256)
            test = ImageTk.PhotoImage(image1)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=10, y=10)

            image2 = Image.open("Gephi/FB_Atheletes.png")
            dimensions = (470, 420)
            image3 = image2.resize(dimensions)
            test = ImageTk.PhotoImage(image3)
            label2 = tk.Label(image=test)
            label2.image = test
            label2.place(x=1050, y=305)

            dataset = undirected_graphs_df.iloc[6]
            self.Scrolledtext1.insert(tk.INSERT, f"\n{selected_dataset} dataset properties\n")
            self.Scrolledtext1.insert(tk.INSERT, f"\n1. Number of Nodes = {int(dataset['Number of Nodes'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n2. Number of Edges = {int(dataset['Number of Edges'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n3. Number of connected components = {int(dataset['Number of connected components'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n4. Size of largest connected component = {int(dataset['Size of largest connected component'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n5. Average Path Length = {dataset['Average Path Length']}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n6. Average Clustering Coeffcient = {dataset['Average Clustering Coeffcient']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n7. Degree Assortativity = {dataset['Degree Assortavity ']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n8. Diameter = {dataset['Diameter']}")

            self.Scrolledtext1.configure(state='disabled')

            self.advanced_button.configure(background="#D5D8DC")
            self.advanced_button.configure(state='disabled')
            self.plots_button.configure(background="#1222b1")
            self.plots_button.configure(state='normal')

        if selected_dataset == 'Facebook (Politician)':
            image1 = Image.open("facebook.jpg")
            image1.putalpha(256)
            test = ImageTk.PhotoImage(image1)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=10, y=10)

            image2 = Image.open("Gephi/Politician.png")
            dimensions = (470, 420)
            image3 = image2.resize(dimensions)
            test = ImageTk.PhotoImage(image3)
            label2 = tk.Label(image=test)
            label2.image = test
            label2.place(x=1050, y=305)

            dataset = undirected_graphs_df.iloc[5]
            self.Scrolledtext1.insert(tk.INSERT, f"\n{selected_dataset} dataset properties\n")
            self.Scrolledtext1.insert(tk.INSERT, f"\n1. Number of Nodes = {int(dataset['Number of Nodes'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n2. Number of Edges = {int(dataset['Number of Edges'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n3. Number of connected components = {int(dataset['Number of connected components'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n4. Size of largest connected component = {int(dataset['Size of largest connected component'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n5. Average Path Length = {dataset['Average Path Length']}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n6. Average Clustering Coeffcient = {dataset['Average Clustering Coeffcient']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n7. Degree Assortativity = {dataset['Degree Assortavity ']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n8. Diameter = {dataset['Diameter']}")

            self.Scrolledtext1.configure(state='disabled')

            self.advanced_button.configure(background="#D5D8DC")
            self.advanced_button.configure(state='disabled')
            self.plots_button.configure(background="#1222b1")
            self.plots_button.configure(state='normal')

        if selected_dataset == 'Facebook (Public Figure)':
            image1 = Image.open("facebook.jpg")
            image1.putalpha(256)
            test = ImageTk.PhotoImage(image1)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=10, y=10)

            image2 = Image.open("Gephi/Public_Figure.png")
            dimensions = (470, 420)
            image3 = image2.resize(dimensions)
            test = ImageTk.PhotoImage(image3)
            label2 = tk.Label(image=test)
            label2.image = test
            label2.place(x=1050, y=305)

            dataset = undirected_graphs_df.iloc[4]
            self.Scrolledtext1.insert(tk.INSERT, f"\n{selected_dataset} dataset properties\n")
            self.Scrolledtext1.insert(tk.INSERT, f"\n1. Number of Nodes = {int(dataset['Number of Nodes'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n2. Number of Edges = {int(dataset['Number of Edges'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n3. Number of connected components = {int(dataset['Number of connected components'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n4. Size of largest connected component = {int(dataset['Size of largest connected component'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n5. Average Path Length = {dataset['Average Path Length']}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n6. Average Clustering Coeffcient = {dataset['Average Clustering Coeffcient']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n7. Degree Assortativity = {dataset['Degree Assortavity ']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n8. Diameter = {dataset['Diameter']}")

            self.Scrolledtext1.configure(state='disabled')

            self.advanced_button.configure(background="#D5D8DC")
            self.advanced_button.configure(state='disabled')
            self.plots_button.configure(background="#1222b1")
            self.plots_button.configure(state='normal')

        if selected_dataset == 'Flickr':
            image1 = Image.open("flickr.jpg")
            image1.putalpha(256)
            test = ImageTk.PhotoImage(image1)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=10, y=10)

            image2 = Image.open("Gephi/Flickr.png")
            dimensions = (470, 420)
            image3 = image2.resize(dimensions)
            test = ImageTk.PhotoImage(image3)
            label2 = tk.Label(image=test)
            label2.image = test
            label2.place(x=1050, y=305)

            dataset = undirected_graphs_df.iloc[3]
            self.Scrolledtext1.insert(tk.INSERT, f"\n{selected_dataset} dataset properties\n")
            self.Scrolledtext1.insert(tk.INSERT, f"\n1. Number of Nodes = {int(dataset['Number of Nodes'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n2. Number of Edges = {int(dataset['Number of Edges'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n3. Number of connected components = {int(dataset['Number of connected components'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n4. Size of largest connected component = {int(dataset['Size of largest connected component'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n5. Average Clustering Coeffcient = {dataset['Average Clustering Coeffcient']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n6. Degree Assortativity = {dataset['Degree Assortavity ']}")

            self.Scrolledtext1.configure(state='disabled')

            self.advanced_button.configure(background="#D5D8DC")
            self.advanced_button.configure(state='disabled')
            self.plots_button.configure(background="#1222b1")
            self.plots_button.configure(state='normal')

        if selected_dataset == 'LinkedIn':
            image1 = Image.open("linkedin.png")
            image1.putalpha(256)
            test = ImageTk.PhotoImage(image1)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=10, y=10)

            image2 = Image.open("Gephi/Linkedin.png")
            dimensions = (470, 420)
            image3 = image2.resize(dimensions)
            test = ImageTk.PhotoImage(image3)
            label2 = tk.Label(image=test)
            label2.image = test
            label2.place(x=1050, y=305)

            dataset = undirected_graphs_df.iloc[2]
            self.Scrolledtext1.insert(tk.INSERT, f"\n{selected_dataset} dataset properties\n")
            self.Scrolledtext1.insert(tk.INSERT, f"\n1. Number of Nodes = {int(dataset['Number of Nodes'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n2. Number of Edges = {int(dataset['Number of Edges'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n3. Number of connected components = {int(dataset['Number of connected components'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n4. Size of largest connected component = {int(dataset['Size of largest connected component'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n5. Average Clustering Coeffcient = {dataset['Average Clustering Coeffcient']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n6. Degree Assortativity = {dataset['Degree Assortavity ']}")

            self.Scrolledtext1.configure(state='disabled')

            self.advanced_button.configure(background="#D5D8DC")
            self.advanced_button.configure(state='disabled')
            self.plots_button.configure(background="#1222b1")
            self.plots_button.configure(state='normal')

        if selected_dataset == 'EU Email':
            image1 = Image.open("eu_email.png")
            image1.putalpha(256)
            test = ImageTk.PhotoImage(image1)
            label1 = tk.Label(image=test)
            label1.image = test
            label1.place(x=10, y=10)

            image2 = Image.open("Gephi/Eu-Email.png")
            dimensions = (470, 420)
            image3 = image2.resize(dimensions)
            test = ImageTk.PhotoImage(image3)
            label2 = tk.Label(image=test)
            label2.image = test
            label2.place(x=1050, y=305)

            dataset = directed_graphs_df.iloc[2]
            self.Scrolledtext1.insert(tk.INSERT, f"\n{selected_dataset} dataset properties\n")
            self.Scrolledtext1.insert(tk.INSERT, f"\n1. Number of Nodes = {int(dataset['Number of Nodes'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n2. Number of Edges = {int(dataset['Number of Edges'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n3. Number of weakly connected components = {int(dataset['Number of weakly connected components'])}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n4. Size of largest weakly connected component = {int(dataset['Size of largest weakly connected component'])}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n5. Average Path Length = {dataset['Average Path Length']}")
            self.Scrolledtext1.insert(tk.INSERT,
                                      f"\n6. Average Clustering Coeffcient = {dataset['Average Clustering Coeffcient']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n7. Degree Assortativity = {dataset['Degree Assortavity ']}")
            self.Scrolledtext1.insert(tk.INSERT, f"\n8. Diameter = {dataset['Diameter']}")

            self.Scrolledtext1.configure(state='disabled')

            self.advanced_button.configure(background="#D5D8DC")
            self.advanced_button.configure(state='disabled')
            self.plots_button.configure(background="#1222b1")
            self.plots_button.configure(state='normal')

        if selected_dataset == 'All Directed Graphs Comparison':
            file = open('overall_directed_indegree.pkl', 'rb')
            plot = pickle.load(file)
            file.close()
            self.create_directed_comparison_plot(f"{selected_dataset} (In-Degree) (Cumulative)", plot)
            file = open('overall_directed_outdegree.pkl', 'rb')
            plot = pickle.load(file)
            file.close()
            self.create_directed_comparison_plot(f"{selected_dataset} (Out-Degree) (Cumulative)", plot)
            plt.show()

            self.advanced_button.configure(background="#D5D8DC")
            self.advanced_button.configure(state='disabled')
            self.plots_button.configure(background="#D5D8DC")
            self.plots_button.configure(state='disabled')

        if selected_dataset == 'All Undirected Graphs Comparison':
            file = open('overall_undirected_degree.pkl', 'rb')
            plot = pickle.load(file)
            file.close()
            self.create_undirected_comparison_plot(f"{selected_dataset} (Cumulative)", plot)
            plt.show()

            self.advanced_button.configure(background="#D5D8DC")
            self.advanced_button.configure(state='disabled')
            self.plots_button.configure(background="#D5D8DC")
            self.plots_button.configure(state='disabled')

    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 24"
        font11 = "-family {Segoe UI} -size 14"
        font12 = "-family {Segoe UI} -size 18"
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
        top.configure(background="#1585c8")
        image = Image.open("network_bg.jpg")
        image.putalpha(128)
        test = ImageTk.PhotoImage(image)

        self.label = tk.Label(image=test)
        self.label.image = test
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

        self.title = tk.Label(top)
        self.title.place(relx=0.295, rely=0.02, height=116, width=612)
        self.title.configure(activebackground="#f0f0f0f0f0f0")
        self.title.configure(background="#1585c8")
        self.title.configure(disabledforeground="#a3a3a3")
        self.title.configure(font=font10)
        self.title.configure(foreground="#ffffff")
        self.title.configure(text='''Twitter Follow Network Analysis''')

        self.dataset_text = tk.Label(top)
        self.dataset_text.place(relx=0.458, rely=0.18, height=66, width=144)
        self.dataset_text.configure(activebackground="#f0f0f0f0f0f0")
        self.dataset_text.configure(activeforeground="black")
        self.dataset_text.configure(background="#1585c8")
        self.dataset_text.configure(cursor="fleur")
        self.dataset_text.configure(disabledforeground="#a3a3a3")
        self.dataset_text.configure(font=font12)
        self.dataset_text.configure(foreground="#ffffff")
        self.dataset_text.configure(highlightbackground="#d9d9d9")
        self.dataset_text.configure(highlightcolor="black")
        self.dataset_text.configure(text='''Dataset''')

        dataset_list = ['Twitter', 'Twitter-Ego', 'Facebook', 'Facebook (Athletes)',
                        'Facebook (Politician)', 'Facebook (Public Figure)',
                        'Twitch (ENGB)', 'Twitch (FR)', 'Flickr', 'LinkedIn', 'EU Email',
                        'All Directed Graphs Comparison', 'All Undirected Graphs Comparison']
        self.dataset_dropdown = ttk.Combobox(top, values=dataset_list, state='readonly')
        self.dataset_dropdown.place(relx=0.412, rely=0.28, relheight=0.036
                                    , relwidth=0.185)
        self.dataset_dropdown.configure(font=font11)
        self.dataset_dropdown.configure(textvariable=ns_main_support.combobox)
        self.dataset_dropdown.configure(takefocus="")
        self.dataset_dropdown.bind("<<ComboboxSelected>>", self.callback)

        self.advanced_button = tk.Button(top)
        self.advanced_button.place(relx=0.505, rely=0.899, height=53, width=152)
        self.advanced_button.configure(activebackground="#ececec")
        self.advanced_button.configure(activeforeground="#000000")
        self.advanced_button.configure(background="#D5D8DC")
        self.advanced_button.configure(disabledforeground="#a3a3a3")
        self.advanced_button.configure(font=font11)
        self.advanced_button.configure(foreground="#ffffff")
        self.advanced_button.configure(highlightbackground="#d9d9d9")
        self.advanced_button.configure(highlightcolor="black")
        self.advanced_button.configure(pady="0")
        self.advanced_button.configure(text='''Advanced''')
        self.advanced_button.configure(state='disabled')
        self.advanced_button.configure(command=self.advanced_screen)

        self.plots_button = tk.Button(top)
        self.plots_button.place(relx=0.401, rely=0.899, height=53, width=152)
        self.plots_button.configure(activebackground="#ececec")
        self.plots_button.configure(activeforeground="#000000")
        self.plots_button.configure(background="#D5D8DC")
        self.plots_button.configure(disabledforeground="#a3a3a3")
        self.plots_button.configure(font="-family {Segoe UI} -size 14")
        self.plots_button.configure(foreground="#ffffff")
        self.plots_button.configure(highlightbackground="#d9d9d9")
        self.plots_button.configure(highlightcolor="black")
        self.plots_button.configure(pady="0")
        self.plots_button.configure(text='''Plots''')
        self.plots_button.configure(state='disabled')
        self.plots_button.configure(command=self.plot_screen)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.922, rely=0.04, height=43, width=66)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#e1031e")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Century Gothic} -size 14 -weight bold")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''X''')
        self.Button1.configure(command=root.destroy)

        self.Scrolledtext1 = ScrolledText(top)
        self.Scrolledtext1.place(relx=0.307, rely=0.34, relheight=0.52
                                 , relwidth=0.37)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font=font11)
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(padx="10")
        self.Scrolledtext1.configure(pady="10")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(wrap="none")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


import platform


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui()
