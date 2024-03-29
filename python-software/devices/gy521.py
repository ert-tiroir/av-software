
from devices.abstract import AbstractDevice

import adafruit_mpu6050
import time

from devices.kalman import KalmanFilter

# ======================================================================================
# ======================================== MATH ========================================
# ======================================================================================

class Matrix:
    def __init__(self, array):
        self.shape = (len(array), len(array[0]))
        self.array = array
    def __add__(self, other: "Matrix"):
        assert self.shape == other.shape
        arr = [
            [
                self.array[x][y] + other.array[x][y]
                for y in range(self.shape[1])
            ] for x in range(self.shape[0])
        ]
        return Matrix(arr)
    def __mul__(self, other):
        if isinstance(other,int) or isinstance(other, float):
            arr = [
                [
                    self.array[x][y] * other
                    for y in range(self.shape[1])
                ] for x in range(self.shape[0])
            ]
            return Matrix(arr)
        assert self.shape[1] == other.shape[0]
        arr = [
            [
                0 for y in range(other.shape[1])
            ] for x in range(self.shape[0])
        ]
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                for k in range(other.shape[1]):
                    arr[i][k] += self.array[i][j] * other.array[j][k]
        return Matrix(arr)
    def __rmul__(self, other):
        if isinstance(other, Matrix): return None
        return self.__mul__(other)
    def __str__(self):
        return "[" + "\n ".join(list(map(str, self.array))) + "]"

def vector (*args):
    return Matrix([[args[i]] for i in range(len(args))])

from math import cos, sin



def rotation_x(a):
    return Matrix([
        [ 1,     0,        0 ],
        [ 0, cos(a), -sin(a) ],
        [ 0,  sin(a),  cos(a)]
    ])

def rotation_y (a):
    return Matrix([
        [ cos(a),   0, sin(a) ],
        [ 0,        1, 0      ],
        [ - sin(a), 0, cos(a) ]
    ])

def rotation_z (a):
    return Matrix([
        [ cos(a), - sin(a), 0 ],
        [ sin(a), cos(a),   0 ],
        [ 0, 0, 1 ]
    ])

   
def rotation (x, y, z):
    return rotation_x(x) * rotation_y(y) * rotation_z(z)

# ======================================================================================
# ======================================= DEVICE =======================================
# ======================================================================================

class GY521Device(AbstractDevice):
    def __init__(self, context):
        self.gy521 = adafruit_mpu6050.MPU6050(context.i2c)

        self.rotation         = vector(0, 0, 0)
        self.angular_velocity = vector(0, 0, 0)

        self.rx = KalmanFilter(0.001, 0.003, 0.03)
        self.ry = KalmanFilter(0.001, 0.003, 0.03)
        self.rz = KalmanFilter(0.001, 0.003, 0.03)

        self.time = time.time()
    def rotation_matrix (self):
        return rotation(self.rotation.array[0][0],
                        self.rotation.array[1][0],
                        0)
    def is_query(self, query):
        return query == "0x68"
    def query(self, query):
        new_time  = time.time()
        dt        = new_time - self.time
        self.time = new_time

        gyro = self.gy521.gyro
        gyro = [
            self.rx.update(gyro[0], gyro[0]),
            self.ry.update(gyro[1], gyro[1]),
            self.rz.update(gyro[2], gyro[2])
        ]
        angular_acceleration =  self.rotation_matrix() * vector(*gyro)

        self.angular_velocity = self.angular_velocity + dt * angular_acceleration
        self.rotation         = self.rotation         + dt * self.angular_velocity
        
        return f"{self.rotation.array[0][0]} {self.rotation.array[1][0]} {self.rotation.array[2][0]}"
        # T|P|H\n
