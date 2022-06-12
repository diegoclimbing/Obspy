from obspy.taup import TauPyModel
from obspy.geodetics import degrees2kilometers
import matplotlib.pyplot as plt
from obspy.taup import plot_travel_times

fig, ax = plt.subplots(figsize=(9, 9))

#ax = plot_travel_times(source_depth=10, phase_list=["P", "S"], ax=ax, fig=fig, verbose=True)

#Km = degrees2kilometers(30) #30 grados a km

model = TauPyModel(model="iasp91")

#arrivals = model.get_travel_times(source_depth_in_km=55, distance_in_degree=30, phase_list=["P", "S"])

#ArTime = arrivals[0]

#Vp = Km/arrivals[0].time
#Vs = Km/arrivals[1].time


#####################################################
Ptimes=[0,0,0,0,0,0,0,0]
Stimes=[0,0,0,0,0,0,0,0]
SPtimes=[0,0,0,0,0,0,0,0]
dist=[10,20,30,40,50,60,70,80]
for n in range(8):

    ArrTimes = model.get_travel_times(source_depth_in_km=55, distance_in_degree=(n+2)*10, phase_list=["P", "S"])
    print(n)
    Ptimes[n]=ArrTimes[0].time
    Stimes[n]=ArrTimes[1].time
    SPtimes[n]=Stimes[n]-Ptimes[n]

ax.plot(dist,Ptimes)
ax.plot(dist,Stimes)
ax.plot(dist,SPtimes)
plt.show()
####################################################
print(" ")
print("Tiempos P")
print(Ptimes)
print(" ")
print("Tiempos P")
print(" ")
print(Stimes)
print(" ")
print("Tiempos S-P")
print(SPtimes)
