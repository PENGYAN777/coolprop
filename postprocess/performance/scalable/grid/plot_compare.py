#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 19:01:08 2022

@author: yan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:35:29 2022

@author: yan

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import os
import CoolProp as CP
from IPython import get_ipython;   
get_ipython().magic('reset -sf')
os.system('clear')


fluidname = "HEOS::MD4M"
# fluidname = "HEOS::D6"
Pc = CP.CoolProp.PropsSI('Pcrit',fluidname)
Tc = CP.CoolProp.PropsSI('Tcrit',fluidname)
dc = CP.CoolProp.PropsSI('rhocrit',fluidname)



na = pd.read_csv("na.csv", ",", skiprows=0)
nb = pd.read_csv("nb.csv", ",", skiprows=0)
nc = pd.read_csv("nc.csv", ",", skiprows=0)




n = 1000
# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(na.iloc[:,0]/n , na.iloc[:,1]/na.iloc[0,1], 'k', lw=lwh, label="NozzleA")
axes.plot(na.iloc[:,0]/n , na.iloc[:,1]/na.iloc[0,1], 'ko', lw=lwh)

axes.plot(nb.iloc[:,0]/n , nb.iloc[:,1]/nb.iloc[0,1], 'b', lw=lwh, label="NozzleB")
axes.plot(nb.iloc[:,0]/n , nb.iloc[:,1]/nb.iloc[0,1], 'bo', lw=lwh)

axes.plot(nc.iloc[:,0]/n , nc.iloc[:,1]/nc.iloc[0,1], 'g', lw=lwh, label="NCSHOCK")
axes.plot(nc.iloc[:,0]/n , nc.iloc[:,1]/nc.iloc[0,1], 'go', lw=lwh)


# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))


axes.set_xlabel('Number of grid elements (k)',fontsize=12)
axes.set_ylabel('Time (normalized)',fontsize=12) 
axes.set_title('Computational time with different grids',fontsize=14)
axes.legend(loc=0) # 

fig1.savefig("scalable_grid.png")

