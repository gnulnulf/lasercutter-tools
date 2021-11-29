#!/usr/bin/env python3

speed_min=800
speed_max=1500

laser_min=200
laser_max=800

steps=5
size=5
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
    print("( infill test )")
    print('( settings )')
    print('# speed_min',speed_min)
    print('# speed_max',speed_max)
    print('# laser_min',laser_min)
    print('# laser_max',laser_max)
    speed_delta=speed_max-speed_min
    laser_delta=laser_max-laser_min

    print(task_start)
    for f in range(0,steps):
        speed=speed_min+(f/(steps-1))*speed_delta
        for s in range(0,steps):
            laser=laser_min+(s/(steps-1))*laser_delta
            x=f*(size+gap)
            y=s*(size+gap)
            print("(# F=%d S=%d)" % (speed,laser) )
            print("G0 X%dY%d" % (x,y))
            print("M4 S%d" % (laser))

            for st in range(0,int(size/(laser_width*2))):
                print("G1 X%dY%.2f F%d" % (x+size,y+st*(laser_width*2),speed))
                print("G1 X%dY%.2f "  % (x+size,y+st*(laser_width*2)+laser_width))
                print("G1 X%dY%.2f " % (x,y+st*(laser_width*2)+laser_width))
                print("G1 X%dY%.2f " % (x,y+(st+1)*(laser_width*2)))
                #print("G1 X%dY%.2f " % (x,y+st*laser_width+laser_width+laser_width))
            #print("X%dY%d" % (x+size,y+size))
            #print("X%dY%d" % (x,y+size))
            #print("X%dY%d" % (x,y))
            
            print("M4 S0" )

    print(task_end)
if __name__ == '__main__':
    main()
