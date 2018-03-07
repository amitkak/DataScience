import sys
import matplotlib.pyplot as pyy

def readPoints(filePath):
	'''reads in list of points from file with format x1, y2\\nx2, y2 ...'''
	points = []
	with open(filePath, 'r') as f:
		for line in f:
			parts = line.split(',')
			#TODO: make sure entries are actual numbers
			if len(parts) != 2:
				print "bad line (only two values per line): " + line
				continue
			try:
				px = float(parts[0])
				py = float(parts[1])
			except ValueError:
				print "bad line (entries must be numbers): " + line
			else:
                                pyy.scatter(px,py)
				points.append((px,py))
        pyy.show()
	return points
def getLValues(points, degree):
	assert(degree > 0)
	values = []
	for n in range(0, degree + 1):
		lsum = 0.0
		for x, y in points:
			lsum = lsum + (x**n) * y
		values.append(lsum)
	return values
def getSumsOfPowersOfXCords(points, degree):
	values = []
	for i in range(0, degree * degree + 1):
		rsum = 0.0
		for x, y in points:
			rsum = rsum + x**i
		values.append(rsum)
	return values
def getRValues(points, degree):
	powers = getSumsOfPowersOfXCords(points, degree)
	values = []
	for i in range(0, degree + 1):
		row = []
		for j in range(0, degree + 1):
			row.append(powers[i + j])
		values.append(row)
	return values
def solveSystem(A, b):
        """finds solution to Ax = b, modifies A and b and returns solution vector"""
        #from http://en.wikipedia.org/wiki/Gaussian_elimination#Pseudocode
        for i in range(0, len(A)):
                #find pivot
                pivotIndex = i
                for j in range(i, len(A)):
                        if A[j][i] > A[pivotIndex][i]:
                                pivotIndex = j
                pivot = A[pivotIndex][i]
                if pivot == 0:
                        print "no solutions"
                        return None
                #swap rows row i and row pivotIndex
                if pivotIndex != i:
                        tmp = A[i]
                        A[i] = A[pivotIndex]
                        A[pivotIndex] = tmp
                        #swap elements in b
                        tmp = b[i]
                        b[i] = b[pivotIndex]
                        b[pivotIndex] = tmp
                #sweep other rows
                for j in range(i + 1, len(A)):
                        ratio = A[j][i]/pivot
                        for k in range(i + 1, len(A)):
                                A[j][k] = A[j][k] - A[i][k] * ratio
                        A[j][i] = 0.0
                        b[j] = b[j] - ratio*b[i]
        #now matrix is triangular and backsubstitution can be used
        for j in range(len(A) - 1, -1, -1):
                b[j] = b[j]/A[j][j]
                for k in range(j - 1, -1, -1):
                        b[k] = b[k] - A[k][j]*b[j]
        return b
def answerToString(coef):
	s = "y = "
	for i in range(len(coef) - 1, -1, -1):
		s = s + str(coef[i])
		if i == 1:
			s = s + "*x + "
		elif i == 0:
			break
		else:
			s = s + "*x^" + str(i) + " + "
	return s
			
def usage():
	print "python2 polyReg.py data.csv <degree>"
	print "where data.csv list x,y pairs and degree is a natural number"
if __name__ == '__main__':
	#equations from http://www.efunda.com/math/leastsquares/lstsqr2dcurve.cfm
	if len(sys.argv) != 3:
		usage()
		exit(2)
	if not sys.argv[2].isdigit():
		print "error: second parameter should be a positive integer"
		exit(1)
	degree = int(sys.argv[2])
	pts = readPoints(sys.argv[1])
	lvs =  getLValues(pts, degree)
	rvs =  getRValues(pts, degree)
	print lvs
	print rvs
	answer = solveSystem(rvs,lvs)
	print answerToString(answer)
	
