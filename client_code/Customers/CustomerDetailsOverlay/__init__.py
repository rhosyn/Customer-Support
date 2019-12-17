from ._anvil_designer import CustomerDetailsOverlayTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..CustomerOverlay.CustomerDetails import CustomerDetails

class CustomerDetailsOverlay(CustomerDetailsOverlayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    print("customer details overlay: {}".format(self.item))
    self.add_component(CustomerDetails(item=self.item), slot="slot-2")
    

    


  