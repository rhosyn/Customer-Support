from ._anvil_designer import CustomerOverviewDGRPTemplate
from anvil import *
import anvil.server

class CustomerOverviewDGRP(CustomerOverviewDGRPTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.repeating_panel_1.items = self.item['people']