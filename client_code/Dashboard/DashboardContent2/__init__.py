from ._anvil_designer import DashboardContent2Template
from anvil import *
import anvil.server

class DashboardContent2(DashboardContent2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.