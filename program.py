import FaBo9Axis_MPU9250
#import time
#import sys

#begin = True
#mpu9250 = FaBo9Axis_MPU9250.MPU9250()
    

def getData(mpu9250):            
        a = mpu9250.readAccel();
        g = mpu9250.readGyro();
        m = mpu9250.readMagnet();
        return [a['x'],a['y'],a['z'],g['x'],g['y'],g['z'],m['x'],m['y'],m['z']]




#return [a[0],a[1],a[2],g[0],g[1],g[2],m[0],m[1],m[2]]
'''
        accel = mpu9250.readAccel()
        print " ax = " , ( accel['x'] )
        print " ay = " , ( accel['y'] )
        print " az = " , ( accel['z'] )

        gyro = mpu9250.readGyro()
        print " gx = " , ( gyro['x'] )
        print " gy = " , ( gyro['y'] )
        print " gz = " , ( gyro['z'] )

        mag = mpu9250.readMagnet()
        print " mx = " , ( mag['x'] )
        print " my = " , ( mag['y'] )
        print " mz = " , ( mag['z'] )
        print

        time.sleep(0.1)
'''
#except KeyboardInterrupt:
#    sys.exit()
