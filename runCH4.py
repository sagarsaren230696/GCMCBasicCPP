import numpy as np
import pandas as pd
import subprocess as sp

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import AutoMinorLocator

kb = 1.3806448e-23 # Boltzmann constant J/K
N = 6.023e23 # Avogadro's number

data = {"Energy":[],"Pressure(bar)":[],"Loading(vSTP/v)":[]}
df = pd.DataFrame(data)

methaneData = pd.read_csv(r"./methanedatanew.csv")

Q0 = methaneData['qst(kJ/mol)'].values # Heat of adsorption in kJ/mol
U0 = -Q0/kb/N*1000
pArr = methaneData['F(Pa)'].values
wArr = []
labels = []

plt.style.use('classic')
parameters = {'axes.labelsize': 24,
            'axes.titlesize': 18,
            "legend.fontsize" : 16,
            'figure.autolayout': True,
            'axes.edgecolor':'black',
            'axes.linewidth':2,
            'axes.titlecolor': "black",
            'legend.fontsize': 16,
            'lines.linewidth':3,
            'mathtext.fontset':'stix',
            'font.family':'STIXGeneral'}
plt.rcParams.update(parameters)
colors = plt.cm.autumn(np.linspace(0,1,len(Q0)))

fig,ax = plt.subplots()
ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
ax.tick_params(direction='in', which="major", length=6, width=2, labelsize=18)
ax.tick_params(direction='in', which="minor", length=4, width=2, labelsize=18)
for i,(u,p) in enumerate(zip(U0,pArr)):
    print("Simulating empty_GCMC with background energy {}".format(u))
    # sp.call([r"./empty_GCMC_singleP.exe","{}".format(-2405),"{}".format(30000),"{}".format(p)])
    # sp.call([r"./empty_GCMC_singleP.exe","{}".format(-2405),"{}".format(30000),"{}".format(p)])
    dataFile = pd.read_csv(r"./results_empty_box/SIM_U{:.2f}_P{:.2f}.txt".format(u,p),sep=',',header=2)
    wArr.append(dataFile["Loading(vSTP/v)"].values[0])
    
ax.plot(pArr/pArr[-1],wArr)

ax.set_xlabel("Relative pressure (-)")
ax.set_ylabel("Methane uptake (cc(STP)/cc)")
# ax.legend(loc="best")
plt.savefig(r"./results_empty_box/uptake_profile_methane_var.png",dpi=300)


