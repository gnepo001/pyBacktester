import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MultipleLocator
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import tkinter as tk
from tkinter import messagebox
from tkinter import Menu

import sys
import numpy as np
import pandas as pd

from indicators import SMA

class Applicaton:
        def __init__(self, root):
                self.root = root
                self.root.title("My Tkinter App")
                self.root.geometry("1200x700")
                self.create_menu(self.root)
                self.loadData()
                self.fig = plt.figure(figsize=(8,6))
                self.plotData()
                self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        def create_menu(self,root):
                self.menubar = Menu(root)

                # Menu
                self.about_menu = Menu(self.menubar, tearoff=0)
                self.about_menu.add_command(label="About", command=self.show_about)
                self.menubar.add_cascade(label="Help", menu=self.about_menu)

                # Attach the menu bar to the root window
                self.root.config(menu=self.menubar)

        def show_about(self):
                # Define the action for the "About" menu item
                about_text = """This is a Python Stock and Crypto Backtester. Developed by Gilbert to analyze the effectiveness of certain testing strategies. Nothing Provided or shown in this Application is trading and/or investing advice. The Creator of this Application is not responsiblefor any losses. Trade at your own Risk!"""
                tk.messagebox.showinfo("About", about_text)

        
        def loadData(self):
                # Fake Data
                self.df = pd.read_csv("BTC-USD.csv")
                self.dates = self.df['Date']
                self.closes = self.df['AdjClose']
                self.volume = self.df['Volume']
                self.x = np.linspace(0,10,100)
                self.y1 = np.sin(self.x)
                self.y2 = np.cos(self.x)
                self.y3 = np.tan(self.x)

                self.sma = SMA(5,self.closes)
                
        def plotData(self):
                #adds height to chart types, aka top chart is tallest
                self.gs = gridspec.GridSpec(3,1,height_ratios=[5,1,1])

                self.axs = [self.fig.add_subplot(self.gs[0])]
                self.axs.append(self.fig.add_subplot(self.gs[1],sharex = self.axs[0]))
                self.axs.append(self.fig.add_subplot(self.gs[2],sharex = self.axs[0]))

                #plots
                self.axs[0].plot(self.dates,self.closes)
                self.axs[0].plot(self.dates,self.sma)
                i = 0
                for i in range(0,len(self.closes)):
                        if self.sma[i]>self.closes[i] and not self.sma[i-1] > self.closes[i-1]:
                                #print(self.dates[i])
                                self.axs[0].plot(self.dates[i],(self.closes[i]), marker="^", color="green")
                        elif self.sma[i]<self.closes[i] and not self.sma[i-1] < self.closes[i-1]:
                                self.axs[0].plot(self.dates[i],(self.closes[i]), marker="v", color="red")
                #self.axs[2].xaxis.set_tick_params(bottom = False)

                self.axs[1].plot(self.dates,self.volume)
                self.axs[1].set_title("Volume")

                self.axs[2].plot(self.dates,self.volume)
                self.axs[2].set_title("MACD")
                self.axs[2].xaxis.set_tick_params(rotation=12)
                self.axs[2].xaxis.set_major_locator(MultipleLocator(25))

                self.axs[-1].set_xlabel("Dates",labelpad=10)

                for ax in self.axs:
                        if ax != self.axs[-1]:
                                ax.get_xaxis().set_visible(False)  # Hide x axis for top graphs


                #Top margin for graphics -gives space not so cramp
                #plt.subplots_adjust(hspace=0.2)
                plt.subplots_adjust(hspace=0.2,bottom=0.2)

                # Create a label
                # self.label = tk.Label(self.root, text="Hello, Tkinter!")
                # self.label.pack()

                #Creating tk canvas and inserting plots within ~ later used for collecting user inputs
                self.canvas = FigureCanvasTkAgg(self.fig,master=self.root)
                self.canvas.draw()
                self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                # Add Matplotlib navigation toolbar
                self.toolbar = NavigationToolbar2Tk(self.canvas, self.root)
                self.toolbar.update()
                self.toolbar.pack(side=tk.LEFT, padx=10, pady=0)  # Pack horizontally

                #Create a button
                self.button = tk.Button(root, text="Click me!", command=self.change_label)
                self.button.pack(side=tk.RIGHT, padx=10, pady=0)

        def change_label(self):
                self.label.config(text="Button clicked!")

        def on_closing(self):
                if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
                        self.root.destroy() # destroys current tkinter instance
                        sys.exit()  # Exit the program

if __name__ == "__main__":
    root = tk.Tk()
    app = Applicaton(root)
    root.mainloop()

