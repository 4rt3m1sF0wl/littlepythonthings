
# Python acceleration calculator

print("welcome to the kinematic solver! Please input your values as directed:\nPress enter for no value")
# vars we need 
error = False
# collect info & check if all are numbers
while error == False:
    try:
        dist = input("input change in distance (in meters): ")
        vel0 = input("input initial velocity (in m/s): ")
        velf = input("input final velocity (in m/s): ")
        time = input("input change in time (in seconds): ")
        accl = input("input acceleration (in m/s^2): ")
        
# decide which equations to do (many elif statements lol) and solve
    
        while dist == '' or vel0 == '' or velf == '' or time == '' or accl == '':
        
        # equations for both velocities
            if bool(vel0 == '' and velf != '') or bool(velf == '' and vel0 != ''):
                if accl != '' and dist != '' and time != '':
                    accl = float(accl)
                    dist = float(dist)
                    time = float(time)
                    vel0 = float(vel0)
                    vel0 = velf - accl*time
                    vel0 = velf - 2*accl*dist
                    vel0 = velf - (2*dist)/time
                    velf = vel0 + accl*time
                    velf = vel0 + 2*accl*time
                    velf = vel0 + (2*dist)/time
            # equations to find the other velocity 
                if accl != '' and dist != '' and vel0 != '':
                    accl = float(accl)
                    dist = float(dist)
                    vel0 = float(vel0)
                    velf = vel0 + accl*dist
                elif accl != '' and dist != '' and velf != '':
                    accl = float(accl)
                    dist = float(dist)
                    velf = float(velf)
                    vel0 = velf - accl*dist   
                elif dist != '' and time != '' and vel0 != '':
                    dist = float(dist)
                    time = float(time)
                    vel0 = float(vel0)
                    velf = vel0 + (2*dist)/time
                elif dist != '' and time != '' and velf != '':
                    dist = float(dist)
                    time = float(time)
                    velf = float(velf)
                    vel0 = velf - (2*dist)/time
                elif accl != '' and time != '' and vel0 != '':
                    accl = float(accl)
                    time = float(time)
                    vel0 = float(vel0)
                    velf = vel0 + 2*accl*time
                elif accl != '' and time != '' and velf != '':
                    accl = float(accl)
                    time = float(time)
                    velf = float(velf)
                    vel0 = velf - 2*accl*time
                    
                
                     
        # equations for vel0 velf and dist
            if dist != '' and vel0 != '' and velf != '' and time == '':
                dist = float(dist)
                vel0 = float(vel0)
                velf = float(velf)
                time = (2*dist)/(vel0 + velf)
                accl = (velf - vel0)/(2*dist)
        # equations for vel0 velf and accl
            if accl != '' and vel0 != '' and velf != '' and time == '':
                velf = float(velf)
                vel0 = float(vel0)
                accl = float(accl)
                time = (velf - vel0)/accl
            if accl != '' and vel0 != '' and velf != '' and dist == '':
                velf = float(velf)
                vel0 = float(vel0)
                accl = float(accl)
                dist = (velf -vel0)/(2*accl)
        #equations for vel0 velf and time
            if time != '' and vel0 != '' and velf != '' and accl == '':
                time = float(time)
                vel0 = float(vel0)
                velf = float(velf)
                accl = (velf - vel0)/time
            elif time != '' and vel0 != '' and velf != '' and dist == '':
                time = float(time)
                vel0 = float(vel0)
                velf = float(velf)
                dist = ((velf - vel0)/2)*time
        # set the error checker to True (no Errors)
        error = True
        # check if time is negative and flip it with acceleration
        if time < 0:
            time = abs(time)
            accl = accl*-1
        # print the results
        print('Values according to kinematics(all values rounded to 3 decimal places and in standard units):','\nDistace:',round(float(dist),3),'\nIntitial velocity:',round(float(vel0),3),'\nFinal velocity:',round(float(velf),3),'\nTime:',round(float(time),3),'\nAcceleration:',round(float(accl),3))

    # check if there was an error
    except ValueError:
        error = False
        print('ERROR: Make sure you either input a number or a blank string (hit enter):\n')
        
# uwu this code is very optimized


