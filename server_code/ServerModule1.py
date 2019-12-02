import anvil.server
import numpy as np

@anvil.server.callable
def get_data():
  x = np.linspace(0, 10, 100)
  y = np.sin(x)
  return x,y
