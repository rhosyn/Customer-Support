from ._anvil_designer import CustomerOverviewContentTemplate
from anvil import *
import anvil.server

class CustomerOverviewContent(CustomerOverviewContentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    row = {'name': 'Daniel Barnes', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'}

    items = []
    for i in range(20):
      items.append(row)
    self.repeating_panel_1.items = items