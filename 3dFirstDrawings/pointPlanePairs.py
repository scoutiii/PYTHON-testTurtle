# class to help draw cube in a certain order
# stores a cubes distances, its self (points in a vector), and its color
class pointPlanePairs:
    def __init__(self, distance, plane, color):
        self.distance = distance
        self.plane = plane
        self.color = color

    def whatIsPlane(self):
        return self.plane

    def whatIsDistance(self):
        return self.distance

    def whatIsColor(self):
        return self.color
