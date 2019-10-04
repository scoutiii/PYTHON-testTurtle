# A class which holds the information of the camera (mostly just its position).
# Uses spherical coordinates (rho phi theta) and also a zoom factor, to keep track of its position.
# These values will be used to help calculate the projection plane (the unit direction vectors of its tangent plane).
# NOTE: always use degrees for phi and theta
import math


class Camera:
    # Constructor which will make a camera with  given values, or use defaults
    def __init__(self, rho=100.0, phi=0.0, theta=0.0, zoom=1.0):
        self.phi = phi
        self.theta = theta

        # Can't have a zoom of 0
        if zoom != 0:
            self.zoom = zoom
        else:
            self.zoom = 1.0

        # Can't have a rho of 0
        if rho != 0:
            self.rho = rho
        else:
            self.rho = 100.0

    # Return the cameras rho
    def whatIsRho(self):
        return self.rho

    # Returns the cameras phi
    def whatIsPhi(self):
        return self.phi

    # Returns the cameras theta
    def whatIsTheta(self):
        return self.theta

    # Returns the x value of the cameras position
    def whatIsX(self):
        x = self.rho * math.sin(math.radians(self.phi)) * math.cos(math.radians(self.theta))
        return x

    # Returns the y value of the cameras position
    def whatIsY(self):
        y = self.rho * math.sin(math.radians(self.phi)) * math.sin(math.radians(self.theta))
        return y

    # Returns the z value of the cameras position
    def whatIsZ(self):
        z = self.rho * math.cos(math.radians(self.phi))
        return z

    # Returns the cameras zoom
    def whatIsZoom(self):
        return self.zoom

    # Changes the cameras rho value
    def setRho(self, newRho):
        # Can't have rho be 0
        if newRho == 0:
            return
        else:
            self.rho = newRho

    # Changes the cameras phi value
    def setPhi(self, newPhi):
        self.phi = newPhi

    # Changes the cameras theta value
    def setTheta(self, newTheta):
        self.theta = newTheta

    # Changes the cameras zoom value
    def setZoom(self, newZoom):
        # Can't have a zoom be 0
        if newZoom == 0:
            return
        else:
            self.zoom = newZoom

    # Prints the values of all the data objects (use for checking info, not actually that useful otherwise)
    def printCameraData(self):
        print("Rho:  ", self.rho)
        print("Phi:  ", self.phi)
        print("Theta:", self.theta)
        print("Zoom: ", self.zoom)
