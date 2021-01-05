#This file is a journey time predictor, used to help the classifier judge the reservations in the system , whether they are safe or fake

import math

def getDistance(longitude1 , latitude1 , longitude2, latitude2) :
    # The Euclidean distance between two coordinates having actual distance = 1 kilometer
    coordinateDistanceOfOneKilometer = 0.0095481163 

    # get Euclidean distance between the two points coordinates

    x = pow(longitude1 - longitude2, 2)
    y = pow(latitude1 - latitude2, 2)

    # The Euclidean distance between the two coordinates
    dxy2 = round(math.sqrt(x + y), 10)

    distanceInKilometers = round(dxy2 / coordinateDistanceOfOneKilometer, 2)

    return distanceInKilometers 

def getTimeNeededForAWalk(distance) :
    # This function takes the distance and returns the number of minutes a person takes to complete walking
    # The distance received here is measured in kilometers
    # the standard measure for walking distance is 80 meters for 1 minute of walking time
    # this rate is appropriate to include time spend in traffic 
    
    metersPerMinute = 80
    time = ( distance * 1000 ) / metersPerMinute
    return time

def getTimeNeededForDriving(distance, speed) :
    # This function takes the distance and returns the number of minutes a person takes to complete while driving
    # The distance received here is measured in kilometers
    # The speed can be fast, med, slow or fly
    # 15 km/h is approximately 250 meters per minute .. very appropriate for regions with a lot of traffic
    # 30 km/h is approximately 500 meters per minute 
    # 80 km/h is approximately 1300 meters per minute .. appropriate for motor ways
    
    metersPerMinute = 250

    if speed == 'fast' :
        metersPerMinute = 1300
    elif speed == 'med' :
        metersPerMinute = 500
    elif speed == 'fly' :
        metersPerMinute = 12000

    time = ( distance * 1000 ) / metersPerMinute
    return math.ceil(time)

def determineSpeedWeights(distance):
    if distance <= 25 :
        # This means the user is mostly within the city .. no need to worry
        return [1,2,15, 0, 18]
    elif distance <= 100:
        # This means the user is mostly around the city
        return [4,15,1, 0, 20]
    elif distance > 100 and distance <= 300: 
        # This means the user is in a neighbouring city
        return [10,15,1, 0, 31]
    elif distance > 300 and distance < 800:
        # This means the user is in a different city or a country
        return [20,5,0, 0.2, 25.2]
    elif distance >= 800 :
        # This means the user has to travel by air
        return [0.1,0.01,0.00001, 40, 40.11001]

def getAverageTimeNeededForJourney(distance) :
    # This function takes the distance and returns the number of minutes a person takes to complete while driving
    # The distance received here is measured in kilometers
    # The speed can be fast, med or slow - We take their weighted average
    # by giving large weight for high speed driving
    if distance < 1 :
        return getTimeNeededForAWalk(distance)
    
    weights = determineSpeedWeights(distance)

    time = 1/(weights[4]) * (getTimeNeededForDriving(distance, 'fast') * weights[0] + 
        getTimeNeededForDriving(distance, 'med')  * weights[1]+ 
        getTimeNeededForDriving(distance, 'slow') * weights[2]+
        getTimeNeededForDriving(distance, 'fly') * weights[3]) 
    return math.ceil(time)

def areDistanceAndTimeCompatible(longitude1 , latitude1 , longitude2, latitude2, timeDifference) :
    distance = getDistance(longitude1 , latitude1 , longitude2, latitude2)
    
    time = getAverageTimeNeededForJourney(distance)
    if timeDifference >= time : return 'safe'
    else :
        difference = time - timeDifference 
        if timeDifference <= 0.6 * time and time > 360 :
            return 'fake'
        elif timeDifference < 120 :
            # Assuming that a reservation can't be made before two hours from the last one
            return 'fake'


# Assiut university
x1 = 27.187214
y1 = 31.167686
# Hegaz square
x2 = 30.111288
y2 = 31.345750 

# Harvard university
x3 = 42.37696126941314
y3 = -71.1166466915781

# Alf maskan square
t1 = 30.118840052355925
t2 = 31.340254650650376


#d = getDistance(x2, y2, x1, y1)
#print(d, " km") 
t = getAverageTimeNeededForJourney(64)
print(t/60, " mins")

