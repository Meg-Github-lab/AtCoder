import numpy as np
import cv2
import math

n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]

#s_rot = list(np.rot90(s))
#print(s[1][2])
#print(s_rot[1][2])

def shift(s, t):

    s_left_w = n
    s_left_h = n
    t_left_w = n
    t_left_h = n

    for w in range(n):
        for h in range(n):
            if s[w][h] == '#':
                s_left_w = min(s_left_w, w)
                s_left_h = min(s_left_h, h)
            if t[w][h] == '#':
                t_left_w = min(t_left_w, w)
                t_left_h = min(t_left_h, h)
    #print(s_left_w, s_left_h, t_left_w, t_left_h)

    shift_w = s_left_w - t_left_w
    shift_h = s_left_h - t_left_h
    print(shift_w, shift_h)
    if shift_w < 0 or shift_h < 0:
        for w in range(n):
            for h in range(n):
                s_trans_w = abs(shift_w) + w
                s_trans_h = abs(shift_h) + h
        if s_trans_w < n and s_trans_h < n:
            s_trans = s[s_trans_w][s_trans_h]
        else:
            s_trans = '.'
    

def shift_x(shift):
    src = np.array([[0.0, 0.0],[0.0, 1.0],[1.0, 0.0]], np.float32)
    dest = src.copy()
    dest[:,0] += shift # シフトするピクセル値
    affine = cv2.getAffineTransform(src, dest)
    return cv2.warpAffine(s, affine, (n, n))

def shift_y(shift):
    src = np.array([[0.0, 0.0],[0.0, 1.0],[1.0, 0.0]], np.float32)
    dest = src.copy()
    dest[:,1] += shift # シフトするピクセル値
    affine = cv2.getAffineTransform(src, dest)
    return cv2.warpAffine(s, affine, (n, n))


def random_shift(shifts):
    src = np.array([[0.0, 0.0],[0.0, 1.0],[1.0, 0.0]], np.float32)
    dest = src + shifts.reshape(1,-1).astype(np.float32)
    affine = cv2.getAffineTransform(src, dest)
    return cv2.warpAffine(s, affine, (n, n))


shift(s,t)

radian = math.radians(0)
rows,cols = edges.shape
afin_matrix = np.float32([[math.cos(radian), math.sin(radian), 30],
  [-math.sin(radian), math.cos(radian), 10]])
dst = cv2.warpAffine(edges,afin_matrix,(cols,rows))