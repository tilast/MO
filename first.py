from math import cos, sin
from inspect import getsource

class Lab1:
  @staticmethod
  # returns calculated gradient's list
  def execute(function, x, n, h):
    
    var_x  = x
    g      = range(n)

    for i in range(n):
      f = range(2)
      
      var_x[i] += h
      f[0]      = function(var_x)

      var_x[i] -= 2*h
      f[1]      = function(var_x)
      
      g[i]      = (f[0] - f[1]) / (2 * h)
      var_x[i] += h

    return g


class Sample:
  def __init__(self, function, x, analytical):
    self.function   = function
    self.x          = x
    self.analytical = analytical

  def data(self):
    return { "function": self.function, "argument": self.x, "analytical": self.analytical }

def main():
  # varian 12 data
  variant12 = []

  variant12.append( Sample( lambda x: (x[0] - x[1])**2 + ((x[0] + x[1] - 10)**2) / 9 , [0, 1], [-4, 0] ) )
  variant12.append( Sample( lambda x: 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2, [-1.2, 1], [-215.6, -88] ) )
  variant12.append( Sample( lambda x: (cos(x[1]) + x[0] - 1.5)**2 + (2*x[1] - sin(x[0] - 0.5) - 1)**2, [-1.2, 1], [-3.8061, 11.6013] ) )

  for j in range(len(variant12)):
    data = variant12[j].data()
    print getsource(data['function'])
    for i in range(2, 10):
      print "h = 10^-%s" % (i)
      g = Lab1.execute(data['function'], data['argument'], 2, 10**(-i))
      print "gradient: %s" % (g)
      print "error: [%s, %s] \n" % (abs(g[0] - data['analytical'][0]), abs(g[1] - data['analytical'][1]))

  # print Lab1.execute(f1, x1, 2, 10**(-2))
  # print Lab1.execute(f2, x2, 2, 10**(-2))
  # print Lab1.execute(f3, x3, 2, 10**(-2))
  # calculate gradient by-hand
  # f3s1 = lambda x: 2*(cos(x[1]) + x[0] - 1.5) - 2*(2*x[1] - sin(x[0] - 0.5) - 1) * cos(x[0] - 0.5)
  # print f3s1(x3)
  # f3s2 = lambda x: -2*(cos(x[1]) + x[0] - 1.5) * sin(x[1]) + 4*(2*x[1] - sin(x[0] - 0.5) - 1)
  # print f3s2(x3)

if __name__ == '__main__':
  main()