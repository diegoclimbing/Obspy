## Hand Piking
# Utiliza la tecla Espacio para hacer el picking, selecciona primero la P luego S
# Utiliza la tecla q para mostrar el pickin realizado y pasar a la siguiente estacion.

from obspy.core import read
from matplotlib.dates import date2num, num2date, datestr2num
from datetime import datetime, date, time, timezone

from obspy.core import UTCDateTime
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import datetime
import matplotlib.dates as mdates
from obspy.core.stream import Stream
from glob import glob

import numpy as np

######### busqueda de archivos #########

def ls(expr = '*.*'):
    return glob(expr)
from datetime import date, datetime

path='/home/diegoclimbing/Documents/WorkSpace/Obspy/2020-03-16_Mwr4.7'

#path='/home/diegoclimbing/Documents/WorkSpace/Obspy/2020-03-06_Mwr5.0'

#path='/home/diegoclimbing/Documents/WorkSpace/Obspy/2019-09-09_Mwr5.4'

###################### PICKING ##############################


########## SET station ###################
SDV = True
GR = True
BIM = True
SAM = True 
Stations = ['SDV', 'GRGR', 'BIM', 'SAM']
Nstation = 0
if SDV == True:
   Nstation += 1
if GR == True:
   Nstation += 1
if BIM == True:
   Nstation += 1
if SAM == True:
   Nstation += 1
if Nstation == 0:
   print("No hay estaciones")
print(" ")
print("Numero de estaciones:", Nstation)


for n in range(Nstation):   #


    if SDV == True:

       f1=0.01     #Frequency of the lower bandpass window.
       f2=1.0      #Frequency of the upper bandpass window.

       Wave_files=ls(path+"/*SDV*.SAC")     #Realiza la busqueda para SDV.
       print(" ")
       print("----------ESTACION SDV ----------  #", len(Wave_files))

       SDV = False

    ##########################################
    elif GR == True:
       f1=0.01      # lower bandpass window.
       f2=1.0    # upper bandpass window.    
       Wave_files=ls(path+"/*GR*Z*.SAC")     #Realiza la busqueda para GR.
       Wave_files+=ls(path+"/*GR*BH1*.SAC")     
       Wave_files+=ls(path+"/*GR*BH2*.SAC")     
       print(" ")
       print("----------ESTACION GR  ----------  #", len(Wave_files))
       GR=False

    ##########################################
    elif BIM == True:
       f1=0.01      # lower bandpass window.
       f2=1.0    # upper bandpass window.

       Wave_files=ls(path+"/*BIM*.SAC")     #Realiza la busqueda para BIM.
       print(" ")
       print("----------ESTACION BIN ----------  #", len(Wave_files))

       BIM = False

    ##########################################
    elif SAM == True:
       f1=0.01      # lower bandpass window.
       f2=1.0    # upper bandpass window.

       Wave_files=ls(path+"/*SAM*Z*.SAC")     #Realiza la busqueda para SAM.
       Wave_files+=ls(path+"/*SAM*BHN*.SAC")     
       Wave_files+=ls(path+"/*SAM*BHE*.SAC") 
       print(" ")
       print("----------ESTACION SAM ----------  #", len(Wave_files))

       SAM = False

    ##########################################

    Tr  = read(Wave_files[0], format="sac")
    Tr += read(Wave_files[1], format="sac")
    print(Tr)
    print(" ")

    Tr = Tr.filter("bandpass", freqmin=f1, freqmax=f2)

    pts = []
    
    figura = plt.figure(figsize=(15, 7))


    Tr.plot(fig=figura, right_vertical_labels=True, vertical_scaling_range=5e1, one_tick_per_line=True, show_y_UTC_label=True, equal_scale=False, show=False)
    pts = np.asarray(plt.ginput(2, timeout=-1,mouse_add=2, mouse_pop=1, mouse_stop=0))  
    (xP, y0), (xS, y1) = pts
    plt.show()
    tP = num2date(xP) #  Conversion de formato para matplotlib 
    tS = num2date(xS)

    print(" ")
    print("Tiempo de llegada phase P",tP)
    print("Tiempo de llegada phase S",tS)
    print(" ")
    figura = plt.figure(figsize=(15, 7))
    Tr.plot(fig=figura, right_vertical_labels=True, vertical_scaling_range=5e1, one_tick_per_line=True, show_y_UTC_label=True, equal_scale=False, show=False)
    plt.axvline(x= tP, color='r')
    plt.axvline(x= tS, color='b')
    plt.show()
    ##########################################

###########################################################

