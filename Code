from roboticstoolbox import Bicycle, RandomPath, VehicleIcon,RangeBearingSensor,LandmarkMap
from math import pi , atan2
import matplotlib.pyplot as plt
Robot_initial=(input("Please enter the robot's start coordinates as x  y  z : "))
Robot_initial=Robot_initial.split()
Target_Coordinates=(input("Please enter the target coordinates as x  y: "))
Target_Coordinates=Target_Coordinates.split()
Num_of_obstacles=(input("Please input number of obstacles: "))
anim = VehicleIcon('redcar.png', scale = 2)

#Robot's place and design
veh = Bicycle(
animation = anim,
control = RandomPath,
x0 = (Robot_initial[0],Robot_initial[1],Robot_initial[2]),
)
print(veh.x)
veh.init(plot=True)
veh._animation.update(veh.x)

#Target design and coordinates
goal=[float(Target_Coordinates[0]),float(Target_Coordinates[1])];
goal_marker_style = {
'marker': 'X',
'markersize': 15,
'color': 'b',
}
plt.plot(goal[0],goal[1], **goal_marker_style)

#map and number of obsticles
map=LandmarkMap(int(Num_of_obstacles), 10)
map.plot()
sensor=RangeBearingSensor(robot=veh,map=map,animate=True)

#Function that detects the obstacle near the car and direction that the car will choose
def detect_obstacles(readings):
    for i in readings:
        if i[0]< 1.5 and i[1]<pi/4 and i[1]>=0:
            return True #True refers to right direction
        elif i[0]< 1.5 and i[1]>-pi/4 and i[1]<0:
            return False #False refers to left direction


#Function that moves the car to the target and update angle to goal
def ON():
    goal_heading=atan2(
    (goal[1]-veh.x[1]),(goal[0]-veh.x[0])
    )
    steer = goal_heading-veh.x[2]
    veh.step(1.9,steer)
    veh._animation.update(veh.x)
    plt.pause(0.005)
    
    
#Funtion that checks that the car reached the target
def reach_condtion():
    if ((abs(goal[0]-veh.x[0])<0.05) or (abs(goal[1] -veh.x[1])<0.05)):
        return False


run=True
while(run):
    if (detect_obstacles(sensor.h(veh.x)) is True):
        veh.step(1.8,-pi/2.5)
        veh._animation.update(veh.x)
        plt.pause(0.005)

    elif (detect_obstacles(sensor.h(veh.x)) is False):
        veh.step(1.8,pi/2.5)
        veh._animation.update(veh.x)
        plt.pause(0.005)  

    else:
        ON()
        if reach_condtion() is False:
            run=False
        else:
            run=True
             
plt.pause(1000)
