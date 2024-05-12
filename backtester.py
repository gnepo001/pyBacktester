import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MultipleLocator
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as tk
import numpy as np
import pandas as pd

class Applicaton:
        def __init__(self, root):
                self.root = root
                self.root.title("My Tkinter App")
                self.loadData()
                self.fig = plt.figure(figsize=(8,6))
                self.plotData()
        
        def loadData(self):
                # Fake Data
                self.df = pd.read_csv("BTC-USD.csv")
                self.dates = self.df['Date']
                self.closes = self.df['AdjClose']
                self.x = np.linspace(0,10,100)
                self.y1 = np.sin(self.x)
                self.y2 = np.cos(self.x)
                self.y3 = np.tan(self.x)
                
        def plotData(self):
                #adds height to chart types, aka top chart is tallest
                self.gs = gridspec.GridSpec(3,1,height_ratios=[5,1,1])
                
                self.axs = [self.fig.add_subplot(self.gs[0]),
                        self.fig.add_subplot(self.gs[1]),
                        self.fig.add_subplot(self.gs[2])]

                        #plots
                self.axs[0].plot(self.dates,self.closes)
                self.axs[0].xaxis.set_tick_params(rotation=25)
                self.axs[0].xaxis.set_major_locator(MultipleLocator(25))

                self.axs[1].plot(self.x,self.y2)
                self.axs[1].set_title("Volume")
                self.axs[2].plot(self.x,self.y3)
                self.axs[2].set_title("MACD")

                #Top margin for graphics -gives space not so cramp
                plt.subplots_adjust(hspace=0.5)

                # Create a label
                self.label = tk.Label(self.root, text="Hello, Tkinter!")
                self.label.pack()

                #Creating tk canvas and inserting plots within ~ later used for collecting user inputs
                self.canvas = FigureCanvasTkAgg(self.fig,master=self.root)
                self.canvas.draw()
                self.canvas.get_tk_widget().pack()
                
                # Create a button
                self.button = tk.Button(root, text="Click me!", command=self.change_label)
                self.button.pack()

        def change_label(self):
                self.label.config(text="Button clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Applicaton(root)
    root.mainloop()
