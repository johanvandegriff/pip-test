import numpy
import scipy

def my_function():
  print("numpy:", numpy.__version__)
  print("scipy:", scipy.__version__)

class MyClass():
  def get_versions(self):
    my_function()
