import numpy as np
import utils

final_cord = np.load("final_cord.npy")
print("final_cord: {}".format(final_cord))
first_rect_cord = final_cord[0:4]
second_rect_cord = final_cord[4:8]
third_rect_cord = final_cord[8:12]

print("final_cord: {} \n".format(first_rect_cord))
print("second_rect_cord: {} \n".format(second_rect_cord))
print("third_rect_cord: {} \n".format(third_rect_cord))

v1 = np.array(utils.compute_vanishing_point([first_rect_cord[0], first_rect_cord[1], first_rect_cord[2], first_rect_cord[3]]))
v2 = np.array(utils.compute_vanishing_point([first_rect_cord[0], first_rect_cord[2], first_rect_cord[1], first_rect_cord[3]]))

v3 = np.array(utils.compute_vanishing_point([second_rect_cord[0], second_rect_cord[1], second_rect_cord[2], second_rect_cord[3]]))
v4 = np.array(utils.compute_vanishing_point([second_rect_cord[0], second_rect_cord[2], second_rect_cord[1], second_rect_cord[3]]))

v5 = np.array(utils.compute_vanishing_point([third_rect_cord[0], third_rect_cord[1], third_rect_cord[2], third_rect_cord[3]]))
v6 = np.array(utils.compute_vanishing_point([third_rect_cord[0], third_rect_cord[2], third_rect_cord[1], third_rect_cord[3]]))

print("v1: {}".format(v1))
print("v2: {}".format(v2))
print("v3: {}".format(v3))
print("v4: {}".format(v4))
print("v5: {}".format(v5))
print("v6: {}".format(v6))

v1_h = np.append(v1, 1)
v2_h = np.append(v2, 1)
v3_h = np.append(v3, 1)
v4_h = np.append(v4, 1)
v5_h = np.append(v5, 1)
v6_h = np.append(v6, 1)
print("v1_h: {}".format(v1_h))
print("v2_h: {}".format(v2_h))
print("v3_h: {}".format(v3_h))
print("v4_h: {}".format(v4_h))
print("v5_h: {}".format(v5_h))
print("v6_h: {}".format(v6_h))

pts_v6 = np.vstack((v1_h, v2_h, v3_h, v4_h, v5_h, v6_h))
print("pts_v6: {}".format(pts_v6))
print("pts_v6.shape: {}".format(pts_v6.shape))
pts_v6 = pts_v6.reshape(int(pts_v6.shape[0]/2),-1)
print("pts_v6.shape: {}".format(pts_v6.shape))

A = np.empty((3, 3))
b = np.empty((3, 1))
for i, v in enumerate(pts_v6):
    A[i] = np.array([v[5]*v[0] + v[3]*v[2], v[5]*v[1] + v[4]*v[2], v[5]*v[2]])
    b[i] = -(v[3]*v[0] + v[4]*v[1])

print("A: {}".format(A))
print("b: {}".format(b))

omega = np.linalg.solve(A, b).reshape(3,)
print("omega: {}".format(omega))
Omega = [[1, 0, omega[0]],
         [0, 1, omega[1]],
         [*omega]]

k13 = -omega[0]
k23 = -omega[1]
k11 = np.sqrt(omega[2] - k13**2 - k23**2)
print("k13: {}".format(k13))
print("k23: {}".format(k23))
print("k11: {}".format(k11))

K = [[k11, 0, k13],
     [0, k11, k23],
     [0, 0, 1]]

print("K: {}".format(K))
print(np.matrix(K))

d1 = np.dot(np.linalg.inv(K), v1_h)
d2 = np.dot(np.linalg.inv(K), v2_h)
print("Left Facade Direction Vector d1: {}, \n d2: {}:\n".format(d1, d2))

d1 = d1.reshape((1,3))
d2 = d2.reshape((1,3))
first_plane_normal = np.cross(d1, d2)
print("first_plane_normal: {} \n".format(first_plane_normal))
print("first_plane_normal: {} \n".format(first_plane_normal.shape))

d3 = np.dot(np.linalg.inv(K), v3_h)
d4 = np.dot(np.linalg.inv(K), v4_h)
print("second_plane direction d3: {}, \n d4: {}:\n".format(d3, d4))

d3 = d3.reshape((1,3))
d4 = d4.reshape((1,3))
second_plane_normal = np.cross(d3, d4)
print("second_plane_normal: {} \n".format(second_plane_normal))
print("second_plane_normal: {} \n".format(second_plane_normal.shape))

angel = utils.angle_between(first_plane_normal.T, second_plane_normal)
print("Angele between first_plane_normal and second_plane_normal: {} \n".format(np.degrees(angel)))

angle_degrees = np.degrees(angel)
print("Angele between first_plane_normal and second_plane_normal in degrees : {} \n".format(angle_degrees))

ang1 = utils.compute_angle_between_planes([v1.tolist(), v2.tolist()], [v3.tolist(), v4.tolist()], np.array(K))
print("Angele between first_plane and second_plane : {} \n".format(ang1))

ang2 = utils.compute_angle_between_planes([v1.tolist(), v2.tolist()], [v5.tolist(), v6.tolist()], np.array(K))
print("Angele between first_plane and third_plane : {} \n".format(ang2))

ang3 = utils.compute_angle_between_planes([v3.tolist(), v4.tolist()], [v5.tolist(), v6.tolist()], np.array(K))
print("Angele between second_plane and third_plane : {} \n".format(ang3))