#!/usr/bin/env python

class PID:
    def __init__(self, kp, ki, kd, set_point=0.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0.0
        self.integral = 0.0
        self.set_point = set_point

    def set_point(self, set_point):
        self.set_point = set_point
        self.integral = 0.0
        self.prev_error = 0.0

        
