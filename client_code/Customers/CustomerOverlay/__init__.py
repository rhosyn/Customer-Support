from ._anvil_designer import CustomerOverlayTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class CustomerOverlay(CustomerOverlayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
#     print("item overlay = {}".format(self.item))
    
  def clear_overlay(self):
    homepage = get_open_form()
    homepage.clear(slot="overlay")
