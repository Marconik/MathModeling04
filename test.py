# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:01:38 2024

@author: mamin
"""

import numpy as np
import pandas as pd
from datetime import timedelta as td
import itertools

from timetable import TGap,EG,GE,ES,SE,EW,WE,WS,SW

#all possible routes
#0-E,1-W,2-S,3-G
nums=[0,1,2,3]
SList=list(itertools.permutations(nums))



#Start
startT0=td(hours=7,minutes=30)
Result=[]
for k in range(169):
    
    #StartTime and Initialize
    startT=startT0+k*td(minutes=5)
    VolP0=0
    SumT0=td(hours=24)
    per0=()
    
    #search on all routes
    for per in SList:
        per=list(per)
        VolP=0
        
        #Arrival time
        droptime=list(np.ones(5))
        droptime[0]=startT
        for i in range(1,5):
            droptime[i]=droptime[i-1]+TGap[per[(i-1)%4]][per[i%4]]
        SumT=droptime[4]-droptime[0]
        
        #Counting Passenger Volume
        PKList=list(itertools.combinations(per+[per[0]], 2))
        for x in PKList:
            if x == (0,3):
                x1=np.where(np.array(x)==0)[0][0]
                x2=np.where(np.array(x)==3)[0][-1]
                t1=droptime[x1]
                t2=droptime[x2]
                for y in EG:
                    if y[0]<=t1 and y[1] >=t2:
                        VolP=VolP+y[2]
                        
            if x == (3,0):
                x1=np.where(np.array(x)==3)[0][0]
                x2=np.where(np.array(x)==0)[0][-1]
                t1=droptime[x1]
                t2=droptime[x2]
                for y in GE:
                    if y[0]<=t1 and y[1] >=t2:
                        VolP=VolP+y[2]
            
            if x == (0,1):
                x1=np.where(np.array(x)==0)[0][0]
                x2=np.where(np.array(x)==1)[0][-1]
                t1=droptime[x1]
                t2=droptime[x2]
                for y in EW:
                    if y[0]<=t1 and y[1] >=t2:
                        VolP=VolP+y[2]
                        
            if x == (1,0):
                x1=np.where(np.array(x)==1)[0][0]
                x2=np.where(np.array(x)==0)[0][-1]
                t1=droptime[x1]
                t2=droptime[x2]
                for y in WE:
                    if y[0]<=t1 and y[1] >=t2:
                        VolP=VolP+y[2]
                
            if x == (0,2):
                x1=np.where(np.array(x)==0)[0][0]
                x2=np.where(np.array(x)==2)[0][-1]
                t1=droptime[x1]
                t2=droptime[x2]
                for y in ES:
                    if y[0]<=t1 and y[1] >=t2:
                        VolP=VolP+y[2]
                        
            if x == (2,0):
                x1=np.where(np.array(x)==2)[0][0]
                x2=np.where(np.array(x)==0)[0][-1]
                t1=droptime[x1]
                t2=droptime[x2]
                for y in SE:
                    if y[0]<=t1 and y[1] >=t2:
                        VolP=VolP+y[2]
                        
            if x == (1,2):
                x1=np.where(np.array(x)==1)[0][0]
                x2=np.where(np.array(x)==2)[0][-1]
                t1=droptime[x1]
                t2=droptime[x2]
                for y in WS:
                    if y[0]<=t1 and y[1] >=t2:
                        VolP=VolP+y[2]
                        
            if x == (2,1):
                x1=np.where(np.array(x)==2)[0][0]
                x2=np.where(np.array(x)==1)[0][-1]
                t1=droptime[x1]
                t2=droptime[x2]
                for y in SW:
                    if y[0]<=t1 and y[1] >=t2:
                        VolP=VolP+y[2]
        
        #Upgrade the best route
        if VolP > VolP0 or (VolP==VolP0 and SumT<SumT0):
            VolP0=VolP
            SumT0=SumT
            per0=per
    
    Result.append([startT,per0,VolP0,SumT0])

#Print to CSV
dataframe=pd.DataFrame(Result)
dataframe.to_csv("testresults.csv",index=False)
