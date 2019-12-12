from ._anvil_designer import CustomerOverlayTemplate
from anvil import *
import anvil.server

class CustomerOverlay(CustomerOverlayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def clear_overlay(self):
    homepage = get_open_form()
    homepage.clear(slot="overlay")
