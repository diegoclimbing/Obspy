#Hello_obspy.py

from obspy import read
from obspy.core import UTCDateTime
from obspy.core.stream import Stream
from glob import glob

T_in = UTCDateTime("2020-03-24T06:15:00") 



def ls(expr = '*.*'):
    return glob(expr)


path='/home/diegoclimbing/Documents/WorkSpace/Obspy/2020-03-16_Mwr4.7'

Wave_files=ls(path+"/*Z.*.SAC")

print(len(Wave_files))

for n in  range(len(Wave_files)):
    print(Wave_files[n])

st = Stream()
for n in  range(len(Wave_files)):
    st += read(Wave_files[n], format="sac")

#st.filter("lowpass", freq=0.1, corners=2)

print(T_in)

print(st)

st.plot( interval=60, right_vertical_labels=False, vertical_scaling_range=5e1, one_tick_per_line=True, show_y_UTC_label=True, equal_scale=False, events={'min_magnitude': 6.5})


#st.plot()

