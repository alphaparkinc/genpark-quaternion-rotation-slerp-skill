"""Quaternion 3D Rotation & SLERP Engine
100% Python Standard Library (math).
"""

import math

class Quaternion:
    """Hamiltonian 4D orientation quaternion."""
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def multiply(self, q):
        w = self.w * q.w - self.x * q.x - self.y * q.y - self.z * q.z
        x = self.w * q.x + self.x * q.w + self.y * q.z - self.z * q.y
        y = self.w * q.y - self.x * q.z + self.y * q.w + self.z * q.x
        z = self.w * q.z + self.x * q.y - self.y * q.x + self.z * q.w
        return Quaternion(w, x, y, z)

    def rotate_vector(self, v):
        p = Quaternion(0, v[0], v[1], v[2])
        conj = Quaternion(self.w, -self.x, -self.y, -self.z)
        res = self.multiply(p).multiply(conj)
        return [round(res.x, 4), round(res.y, 4), round(res.z, 4)]

    @staticmethod
    def from_axis_angle(axis, angle_rad):
        half = angle_rad / 2.0
        s = math.sin(half)
        mag = math.hypot(*axis)
        return Quaternion(math.cos(half), axis[0]/mag * s, axis[1]/mag * s, axis[2]/mag * s)
