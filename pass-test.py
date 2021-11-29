#!/usr/bin/env python3

speed_min=300
speed_max=900

laser_power=800
pass_min=2
pass_max=8

steps=3
size=10
gap=5

laser_width=0.2
task_start='''
M4 S0
S0 
G0X0Y0
'''
task_end='''
S0
M5 S0
'''


def main():
    
    print("; Pass test ")
    print('; settings ')
    print('; speed_min',speed_min)
    print('; speed_max',speed_max)
    print('; laser_power',laser_power)
    speed_delta=speed_max-speed_min

    print(task_start)
    laser=laser_power
    for s in range(0,steps):
        speed=speed_min+(s/(steps-1))*speed_delta
        for p in range(pass_min,pass_max+1):
            x=s*(size+gap)
            y=(p-pass_min)*(size+gap)
            print("; F=%d S=%d" % (speed,laser) )
            print("G0 X%dY%d" % (x,y))
            print("M4 S%d" % (laser))
            for j in range(p):
                print(";pass %d" % (j+1))
                print("G1 X%dY%d F%d" % (x+size,y,speed))
                print("X%dY%d" % (x+size,y+size))
                print("X%dY%d" % (x,y+size))
                print("X%dY%d" % (x,y))
            
            print("M4 S0" )

    print(task_end)
if __name__ == '__main__':
    main()
