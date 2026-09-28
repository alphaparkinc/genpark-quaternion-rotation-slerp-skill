from client import Quaternion
import math

def main():
    q = Quaternion.from_axis_angle([0, 0, 1], math.pi / 2.0)
    v = [1, 0, 0]
    rotated = q.rotate_vector(v)
    print("Quaternion 3D Rotation Verification:")
    print(f"Original Vector: {v}")
    print(f"Rotated 90 deg around Z: {rotated} (Expected: [0, 1, 0])")

if __name__ == "__main__":
    main()
