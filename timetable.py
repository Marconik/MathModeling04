# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:24:05 2024

@author: mamin
"""

from datetime import timedelta as td


#Time origin
nL=td()
#Time gaps
TGap=[[nL,td(minutes=6),td(minutes=13),td(minutes=35)],
      [td(minutes=6),nL,td(minutes=17),td(minutes=37)],
      [td(minutes=13),td(minutes=17),nL,td(minutes=35)],
      [td(minutes=35),td(minutes=37),td(minutes=35),nL]]


#volume of commuters
EG=[(td(hours=0,minutes=0),td(hours=7,minutes=50),2),
    (td(hours=0,minutes=0),td(hours=9,minutes=45),5),
    (td(hours=0,minutes=0),td(hours=14,minutes=00),1),
    (td(hours=12,minutes=50),td(hours=14,minutes=0),6),
    (td(hours=12,minutes=50),td(hours=15,minutes=55),3),
    (td(hours=18,minutes=20),td(hours=19,minutes=30),3),
    (td(hours=19,minutes=0),td(hours=24,minutes=00),7)]

GE=[(td(hours=0,minutes=0),td(hours=7,minutes=50),3),
    (td(hours=0,minutes=0),td(hours=9,minutes=45),5),
    (td(hours=0,minutes=0),td(hours=14,minutes=00),3),
    (td(hours=12,minutes=50),td(hours=14,minutes=0),5),
    (td(hours=12,minutes=50),td(hours=15,minutes=55),2),
    (td(hours=18,minutes=20),td(hours=19,minutes=30),1),
    (td(hours=19,minutes=0),td(hours=24,minutes=00),7)]

EW=[(td(hours=0,minutes=0),td(hours=7,minutes=50),1),
    (td(hours=0,minutes=0),td(hours=9,minutes=45),1),
    (td(hours=9,minutes=25),td(hours=9,minutes=45),1),
    (td(hours=0,minutes=0),td(hours=14,minutes=0),1),
    (td(hours=12,minutes=00),td(hours=13,minutes=00),1),
    (td(hours=13,minutes=30),td(hours=15,minutes=55),1),
    (td(hours=15,minutes=35),td(hours=15,minutes=55),1),
    (td(hours=18,minutes=00),td(hours=19,minutes=00),1),
    (td(hours=18,minutes=00),td(hours=19,minutes=30),1),
    (td(hours=19,minutes=00),td(hours=19,minutes=30),1),
    (td(hours=21,minutes=00),td(hours=24,minutes=00),1),
    (td(hours=22,minutes=00),td(hours=24,minutes=00),1)]

WE=[(td(hours=0,minutes=0),td(hours=7,minutes=50),1),
    (td(hours=0,minutes=0),td(hours=9,minutes=45),1),
    (td(hours=9,minutes=25),td(hours=9,minutes=45),1),
    (td(hours=0,minutes=0),td(hours=14,minutes=0),1),
    (td(hours=12,minutes=00),td(hours=13,minutes=00),1),
    (td(hours=13,minutes=30),td(hours=15,minutes=55),1),
    (td(hours=15,minutes=35),td(hours=15,minutes=55),1),
    (td(hours=18,minutes=00),td(hours=19,minutes=00),1),
    (td(hours=18,minutes=00),td(hours=19,minutes=30),1),
    (td(hours=19,minutes=00),td(hours=19,minutes=30),1),
    (td(hours=21,minutes=00),td(hours=24,minutes=00),1),
    (td(hours=22,minutes=00),td(hours=24,minutes=00),1)]

ES=[(td(hours=0,minutes=0),td(hours=7,minutes=30),3),
    (td(hours=0,minutes=0),td(hours=8,minutes=00),2),
    (td(hours=11,minutes=20),td(hours=12,minutes=0),1),
    (td(hours=13,minutes=30),td(hours=15,minutes=0),1),
    (td(hours=18,minutes=0),td(hours=19,minutes=0),5),
    (td(hours=19,minutes=0),td(hours=20,minutes=0),3)]

SE=[(td(hours=0,minutes=0),td(hours=7,minutes=50),2),
    (td(hours=0,minutes=0),td(hours=8,minutes=30),4),
    (td(hours=12,minutes=0),td(hours=13,minutes=0),2),
    (td(hours=13,minutes=0),td(hours=14,minutes=0),1),
    (td(hours=14,minutes=30),td(hours=15,minutes=55),1),
    (td(hours=16,minutes=30),td(hours=17,minutes=20),3),
    (td(hours=18,minutes=0),td(hours=19,minutes=0),2)]

WS=[(td(hours=13,minutes=30),td(hours=15,minutes=00),1),
    (td(hours=18,minutes=0),td(hours=19,minutes=0),3),
    (td(hours=19,minutes=0),td(hours=20,minutes=0),2)]

SW=[(td(hours=0,minutes=0),td(hours=8,minutes=30),1),
    (td(hours=12,minutes=0),td(hours=13,minutes=00),2),
    (td(hours=14,minutes=30),td(hours=15,minutes=55),1),
    (td(hours=16,minutes=30),td(hours=17,minutes=20),2),
    (td(hours=18,minutes=0),td(hours=19,minutes=00),2)]