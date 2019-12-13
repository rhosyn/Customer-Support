import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import numpy as np

@anvil.server.callable
def get_data():
  x = np.linspace(0, 10, 100)
  y = np.sin(x)
  return x,y
