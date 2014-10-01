from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
from operator import sub, add

def F1(x):
	return ((x[0] - x[1]) ** 2) + ((x[0]+x[1]-10) ** 2) / 9.0

def F2(x):
	return 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2

def F3(x):
	return (x[0]**2 + x[1]**2 - x[0] - 4.75)**2 + (2*x[0]**2 - x[0]*x[1] - x[1]**2 - 14)**2
 
def func(x):
	return F1(x)

def plot3D(point, length, N):
	delta = length / float(N)
	x_source = [(point[0] - length / 2. + i * delta) for i in range(N)]
	y_source = [(point[1] - length / 2. + i * delta) for i in range(N)]
	xx, yy = np.meshgrid(x_source, y_source)
	z = func([xx, yy])

	plt3d = plt.figure().gca(projection='3d')

	Gx, Gy = np.gradient(xx * yy)  # gradients with respect to x and y
	G = (Gx ** 2 + Gy ** 2) ** .5  # gradient magnitude
	N1 = G / G.max()  # normalize 0..1

	plt3d.plot_surface(xx, yy, z, rstride=1, cstride=1,
	                   facecolors=cm.jet(N1),
	                   linewidth=0, antialiased=False, shade=False
	)
	plt.show()


def hessian_matrix(x,h):
    length = len(x)
    hesse = [[0]*length for i in range(length)]

    for i in range(length):
    	hi_ei = [0 if k != i else h[i] for k in range(length)]
    	for j in range(length):    		
    		hj_ej = [0 if k != j else h[j] for k in range(length)]
    		x1 = map(add, x, hi_ei)
    		x1 = map(add, x1, hj_ej)
    		x2 = map(sub, x, hi_ei)
    		x2 = map(add, x2, hj_ej)
    		x3 = map(add, x, hi_ei)
    		x3 = map(sub, x3, hj_ej)
    		x4 = map(sub, x, hi_ei)
    		x4 = map(sub, x4, hj_ej)

    		hesse[i][j] = (func(x1) - func(x2) - func(x3) + func(x4)) / (4.0 * h[i] * h[j])

    return hesse


def main():

	x_F1 = [0.0, 1.0]
	x_F2 = [-1.2, 1.0]
	x_F3 = [1.0, 2.0]
	F1_Hesse_a = [[20 / 9.0, - 16 / 9.0],[- 16 / 9.0, 20 / 9.0]]
	F2_Hesse_a = [[],[]]
	F3_Hesse_a = [[],[]]

	# print hessian_matrix(x_F2, [10**(-2)]*2)

	# print "F1"
	# print "  h  \t     F1 x1               F1 x2             abs x1             abs x2"
	for i in range(-2, 10):
		h = 10 ** (-i)
		# print [h]*2
		H = hessian_matrix(x_F1, [h]*2)

		print "\n\n10^-%d" % (i)
		print "Hessian matrix:"
		print "[ %20.14f   %20.14f ]" % (H[0][0], H[0][1])
		print "[ %20.14f   %20.14f ]" % (H[1][0], H[1][1])
		print "\nError matrix"
		print "[ %20.14f   %20.14f ]" % (abs(H[0][0] - F1_Hesse_a[0][0]), abs(H[0][1] - F1_Hesse_a[0][1]))
		print "[ %20.14f   %20.14f ]" % (abs(H[1][0] - F1_Hesse_a[1][0]), abs(H[1][1] - F1_Hesse_a[1][1]))


if __name__ == '__main__':
	main()