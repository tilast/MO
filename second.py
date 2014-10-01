from math import sin, cos
from operator import sub, add, abs
from inspect import getsource

class Sample:
  def __init__(self, function, x, analytical):
    self.function   = function
    self.x          = x
    self.analytical = analytical

  def data(self):
    return { "function": self.function, "argument": self.x, "analytical": self.analytical }

class Lab2:
  @staticmethod
  def execute(function, x, n, h):
    # init double-dimensioned list
    he = [0]*n
    for i in range(n):
      he[i] = [0]*n

    for i in range(n):
      hiei = [0 if k != i else h[i] for k in range(n)]

      for j in range(n):
        hjej = [0 if k != j else h[j] for k in range(n)]
        
        he[i][j] = ( function( Lab2.listAddition( Lab2.listAddition( x, hiei ), hjej ) ) 
                 -   function( Lab2.listAddition( Lab2.listSubstraction( x, hiei ), hjej ) )
                 -   function( Lab2.listSubstraction( Lab2.listAddition( x, hiei ), hjej ) )
                 +   function( Lab2.listSubstraction( Lab2.listSubstraction( x, hiei ), hjej ) ) ) / (4 * hiei[i] * hjej[j])
    return he

  # TODO: need to add conditions on comparing of list's length
  @staticmethod
  def listSubstraction(x, y):
    return map(sub, x, y)

  @staticmethod
  def listAddition(x, y):
    return map(add, x, y)

  @staticmethod
  def listAbsolute(x):
    return map(abs, x)

  @staticmethod
  def matrixError(x, y):
    length = len(x)
    result = [0]*length

    for i in range(length):
      result[i] = Lab2.listAbsolute( Lab2.listSubstraction( x[i], y[i] ) )

    return result



def main():
  # varian 12 data
  variant12 = []

  variant12.append( Sample( lambda x: (x[0] - x[1])**2 + ((x[0] + x[1] - 10)**2) / 9.0, [0, 1], [[2 + 2.0/9.0, -2 + 2.0/9.0], [-2 + 2.0/9.0, 2 + 2.0/9.0]] ) )
  variant12.append( Sample( lambda x: 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2, [-1.2, 1], [[1330, 480], [480, 200]] ) )
  variant12.append( Sample( lambda x: (cos(x[1]) + x[0] - 1.5)**2 + (2*x[1] - sin(x[0] - 0.5) - 1)**2, [-1.2, 1], [[-1.92, -5.68], [-5.68, 4.25]] ) )

  for j in range(len(variant12)):
    data = variant12[j].data()
    print "\n\n"
    print getsource(data['function'])
    for i in range(2, 10):
      print "h = 10^-%s \n" % (i)
      he = Lab2.execute(data['function'], data['argument'], len(data['argument']), [10**(-i), 10**(-i)])
      print "hessian:\n"
      for i in range(len(he)):
        print "%s" % he[i]

      print "\nerror:\n"
      error = Lab2.matrixError(he, data['analytical'])
      for i in range(len(error)):
        print "%s" % error[i]

if __name__ == "__main__":
  main()