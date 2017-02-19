import psutil
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.low_light = True
red = [255,0,0]
green = [0,255, 0 ]
blue = [0,0,255]
white = [255,255,255]
cores = psutil.cpu_count()
sense.rotation = 180


def checkCPU():
    cpuDict = {}
    cpupercent = psutil.cpu_percent(interval = None, percpu = True)
    for i in range(0, cores):
        cpuDict[i] = cpupercent[i]
    #print(cpuDict)
    for key in cpuDict:
        lights(key, cpuDict[key]/100)

def checkMem():
    mem = psutil.virtual_memory()
    availMem = ((mem[0]-mem[1])/mem[0])
    #print(availMem)
    lights(6, availMem)

def checkDisk():
    disk = psutil.disk_usage('/home')
    freeSpace = disk[3]/100
    #print(freeSpace)
    lights(7, freeSpace)
    
    
    
def lights(row, ledstolight):
    ledstolight = int(8*ledstolight)+1
    if ledstolight <= 1:
        sense.set_pixel(0, row, green)
    elif ledstolight == 2:
        sense.set_pixel(0, row, white)
        sense.set_pixel(1, row, white)
    elif ledstolight == 3:
        sense.set_pixel(0, row, white)
        sense.set_pixel(1, row, white)
        sense.set_pixel(2, row, white)
        sense.set_pixel(3, row, white)  
    elif ledstolight == 4:
        sense.set_pixel(0, row, white)
        sense.set_pixel(1, row, white)
        sense.set_pixel(2, row, white)
        sense.set_pixel(3, row, white)
    elif ledstolight == 5:
        sense.set_pixel(0, row, white)
        sense.set_pixel(1, row, white)
        sense.set_pixel(2, row, white)
        sense.set_pixel(3, row, white)
        sense.set_pixel(4, row, white)
    elif ledstolight == 6:
        sense.set_pixel(0, row, white)
        sense.set_pixel(1, row, white)
        sense.set_pixel(2, row, white)
        sense.set_pixel(3, row, white)
        sense.set_pixel(4, row, white)
        sense.set_pixel(5, row, white)
    elif ledstolight == 7:
        sense.set_pixel(0, row, white)
        sense.set_pixel(1, row, white)
        sense.set_pixel(2, row, white)
        sense.set_pixel(3, row, white)
        sense.set_pixel(4, row, white)
        sense.set_pixel(5, row, white)
        sense.set_pixel(6, row, red)
    elif ledstolight >=8:
        sense.set_pixel(0, row, white)
        sense.set_pixel(1, row, white)
        sense.set_pixel(2, row, white)
        sense.set_pixel(3, row, white)
        sense.set_pixel(4, row, white)
        sense.set_pixel(5, row, white)
        sense.set_pixel(6, row, white)
        sense.set_pixel(7, row, red)

while True:
    sense.clear()
    checkCPU()
    checkMem()
    checkDisk()
    time.sleep(1)
