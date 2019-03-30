import math
def rollpitch(data):
    Acceleration_angle = [0,0]
    Acceleration_angle[0] = math.atan((data[1])/math.sqrt(pow(data[0],2) + pow(data[2],2)))*180/3.141592654;
    Acceleration_angle[1] = math.atan(-1*data[0]/math.sqrt(pow(data[1],2) + pow(data[2],2)))*180/3.141592654;
    return Acceleration_angle