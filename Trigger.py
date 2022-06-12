from obspy.core import read
from obspy.signal.trigger import plot_trigger
from obspy.signal.trigger import z_detect
from obspy.signal.trigger import classic_sta_lta
from obspy.signal.trigger import recursive_sta_lta
from obspy.signal.trigger import ar_pick

from obspy.core import UTCDateTime
import matplotlib.pyplot as plt
from obspy.core.stream import Stream
from glob import glob

######### busqueda de archivos #########

def ls(expr = '*.*'):
    return glob(expr)


path='/home/diegoclimbing/Documents/WorkSpace/Obspy/2020-03-16_Mwr4.7'

Wave_files=ls(path+"/*BIM*.SAC")     #Realiza la busqueda en path que cumpla la condicion.

print(len(Wave_files))


for n in  range(len(Wave_files)):
    print(Wave_files[n])

#######################################

######## diferentes triger #############
trace = read(Wave_files[0], format="sac")[0]
df = trace.stats.sampling_rate

cftZ = z_detect(trace.data, int(10 * df))

cft = classic_sta_lta(trace.data, int(5 * df), int(10 * df))

cftR = recursive_sta_lta(trace.data, int(5 * df), int(10 * df))

#######################################


###################### PICKING ##############################
print(" Frecuencia de muestreo Hz")
print(df)
print(" ")

########## SET station ###################
SDV = True
GR = True
BIM = True

Nstation = 0
if SDV == True:
   Nstation += 1
if GR == True:
   Nstation += 1
if BIN == True:
   Nstation += 1
if Nstation == 0:
   print("No hay estaciones")
print(Nstation)

for n in range(Nstation):


    if SDV == True:
       ltaP=5.0    # Length of LTA for the P arrival in seconds.
       staP=1.0    #Length of STA for the P arrival in seconds.
       ltaS=5.0    #Length of LTA for the S arrival in seconds.
       staS=1.0    #Length of STA for the S arrival in seconds.
       SDV = False

    ##########################################
    if GR == True:
       ltaP=5.0    # Length of LTA for the P arrival in seconds.
       staP=1.0    #Length of STA for the P arrival in seconds.
       ltaS=5.0    #Length of LTA for the S arrival in seconds.
       staS=1.0    #Length of STA for the S arrival in seconds.
       GR = False

    ##########################################
    if BIN == True:
       ltaP=5.0    # Length of LTA for the P arrival in seconds.
       staP=1.0    #Length of STA for the P arrival in seconds.
       ltaS=5.0    #Length of LTA for the S arrival in seconds.
       staS=1.0    #Length of STA for the S arrival in seconds.
       GR = False

    ##########################################


    TrZ = read(Wave_files[0], format="sac")[0]
    Tr1 = read(Wave_files[1], format="sac")[0]
    Tr2 = read(Wave_files[2], format="sac")[0]

    print(TrZ)
    print(" ")
    print(Tr1)
    print(" ")
    print(Tr2)
    print(" ")

    df = TrZ.stats.sampling_rate

    p_pick, s_pick = ar_pick(TrZ.data, Tr1.data, Tr2.data, df, 0.1, 60.0, ltaP, staP, ltaS, staS, 2, 11, 0.2, 0.3) 



    print(p_pick)
    print(" ")
    print(s_pick)
    print(" ")

    T_in = TrZ.times("utcdatetime")
    print(T_in[0]+p_pick)
    print(" ")
    print(T_in[0]+s_pick)
    print(" ")

###########################################################



############### PLOT ###################

## busqueda de archivos ##

Wave_files=ls(path+"/*Z*.SAC")    




st = Stream()
for n in  range(len(Wave_files)):
    st += read(Wave_files[n], format="sac")

st.plot( interval=60, right_vertical_labels=False, vertical_scaling_range=5e1, one_tick_per_line=True, show_y_UTC_label=True, equal_scale=False, events={'min_magnitude': 6.5})

#plot_trigger(trace, cftR, 1.4, 0.75)

#plot_trigger(trace, cftZ, -0.4, -0.3)

#plot_trigger(trace, cft, 1.3, 0.7)


##### OUT #####



#######################################
