import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# Fake Data
x = np.linspace(0,10,100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

fig = plt.figure(figsize=(8,6))

#adds height to chart types, aka top chart is tallest
gs = gridspec.GridSpec(3,1,height_ratios=[3,1,1])

axs = [fig.add_subplot(gs[0]),
        fig.add_subplot(gs[1]),
        fig.add_subplot(gs[2])]

#plots
axs[0].plot(x,y1)
axs[1].plot(x,y2)
axs[1].set_title("Volume")
axs[2].plot(x,y3)
axs[2].set_title("MACD")

#Top margin for graphics -gives space not so cramp
plt.subplots_adjust(hspace=0.5)

plt.show()