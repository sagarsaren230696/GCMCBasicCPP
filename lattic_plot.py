from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pArr = [0.998e5,5.726e5,32.452e5,56.7e5]
for p in pArr:
    latticFile = pd.read_csv(r'./results_lattice_new/lattic_config_U-250.00_d4.00_P{:.2f}.txt'.format(p))
    print(latticFile.head())

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    plt.style.use("classic")

    def markerFunc(val):
        if val == 0:
            return 'o'
        else: 
            return '^'

    markerData = [markerFunc(val) for val in latticFile['occ'].values]
    latticFile['m'] = markerData
    labels = ["Occupied","Unoccupied"]
    colors = ['r','b']
    for count,(marker, d) in enumerate(latticFile.groupby('m')):
        ax.scatter(d["x"],d["y"],d["z"],marker=marker,s=30,label=labels[count],color=colors[count])


    ax.set_xlabel('X (A)')
    ax.set_ylabel('Y (A)')
    ax.set_zlabel('Z (A)')
    ax.legend(fontsize=10)
    ax.set_title("Pressure {:.1f} kPa".format(p/1000))

    plt.savefig(r'./results_lattice_new/latticePlot_p{:.2f}.png'.format(p),dpi=500)