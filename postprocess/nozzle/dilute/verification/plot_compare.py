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

pig_euler = pd.read_csv("pig_eule.csv", ",", skiprows=0)
pig_rans = pd.read_csv("pig_rans.csv", ",", skiprows=0)
coolprop_euler = pd.read_csv("../coolprop_euler/mesh3.csv", ",", skiprows=0)
coolprop_rans = pd.read_csv("../coolprop_rans/mesh2.csv", ",", skiprows=0)





nn = len(pig_euler.iloc[:,4])
# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
ax2 = axes.twinx()
dmax = np.zeros(nn)
dmin = np.zeros(nn)
axes.plot(pig_euler.iloc[:,4]*1000 , pig_euler.iloc[:,2], 'k', lw=lwh, label="PIG Euler")
# axes.plot(pig_rans.iloc[:,4]*1000 , pig_rans .iloc[:,2], 'r--', lw=lwh, label="PIG RANS")
axes.plot(coolprop_euler.iloc[:,4]*1000 , coolprop_euler.iloc[:,2], 'r', lw=lwh, label="CoolProp Euler")
# axes.plot(coolprop_rans.iloc[:,4]*1000 , coolprop_rans .iloc[:,2], 'r', lw=lwh, label="CoolProp RANS")

for i in range(nn):
    dmax[i] = max(pig_euler.iloc[i,2],coolprop_euler.iloc[i,2])
    dmin[i] = min(pig_euler.iloc[i,2],coolprop_euler.iloc[i,2])
   
ax2.plot(pig_euler.iloc[:,4]*1000, (dmax-dmin)/dmax*100 , 'k*', lw=lwh)    
ax2.set_ylabel('$\Delta_{P/P_t}$(%)',fontsize=12) 
# ax2.set_ylim(0,4)
axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$P/P_t$',fontsize=12) 
axes.set_title('Static-to-total pressure ratio along centerline',fontsize=14)
axes.legend(loc=6) # 
# axes.set_xlim(0,120)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("nozzle_di_euler_vv.pdf")

# fig 2
fig2 = plt.figure( dpi=300)
lwh = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
ax2 = axes.twinx()
dmax = np.zeros(nn)
dmin = np.zeros(nn)
# axes.plot(pig_euler.iloc[:,4]*1000 , pig_euler.iloc[:,2], 'k', lw=lwh, label="PIG Euler")
axes.plot(pig_rans.iloc[:,4]*1000 , pig_rans .iloc[:,2], 'r--', lw=lwh, label="PIG RANS")
# axes.plot(coolprop_euler.iloc[:,4]*1000 , coolprop_euler.iloc[:,2], 'r', lw=lwh, label="CoolProp Euler")
axes.plot(coolprop_rans.iloc[:,4]*1000 , coolprop_rans .iloc[:,2], 'r', lw=lwh, label="CoolProp RANS")

for i in range(nn):
    dmax[i] = max(pig_rans.iloc[i,2],coolprop_rans.iloc[i,2])
    dmin[i] = min(pig_rans.iloc[i,2],coolprop_rans.iloc[i,2])
   
ax2.plot(pig_rans.iloc[:,4]*1000, (dmax-dmin)/dmax*100 , 'k*', lw=lwh)    
ax2.set_ylabel('$\Delta_{P/P_t}$(%)',fontsize=12) 
# ax2.set_ylim(0,4)
axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$P/P_t$',fontsize=12) 
axes.set_title('Static-to-total pressure ratio along centerline',fontsize=14)
axes.legend(loc=6) # 
# axes.set_xlim(0,120)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig2.savefig("nozzle_di_rans_vv.pdf")

