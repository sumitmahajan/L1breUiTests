from math import sin, cos, sqrt, atan2, radians
import math
import logging

logging.basicConfig(filename=
                    "test.log"
                    , level=logging.INFO)

class Coords_Algorithm:

    def get_distance(self=""):
        # approximate radius of earth in km
        R = 6373.0

        lat1 = radians(19.426094)
        lon1 = radians(-99.163648)
        lat2 = radians(19.367045)
        lon2 = radians(-99.136577)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return distance

    def get_coords(n, speed=40):
        R = 6378.1 #Radius of the Earth
        brng = 1.57 #Bearing is 90 degrees converted to radians.
        d = n*speed/3600 #Distance in km

        #lat2  52.20444 - the lat result I'm hoping for
        #lon2  0.36056 - the long result I'm hoping for.

        lat1 = math.radians(19.426094) #Current lat point converted to radians
        lon1 = math.radians(-99.163648) #Current long point converted to radians

        lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
                          math.cos(lat1)*math.sin(d/R)*math.cos(brng))

        lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                                 math.cos(d/R)-math.sin(lat1)*math.sin(lat2))

        lat2 = math.degrees(lat2)
        lon2 = math.degrees(lon2)
        logging.info(str(lat2)+":"+str(lon2))

        return [lat2, lon2]




