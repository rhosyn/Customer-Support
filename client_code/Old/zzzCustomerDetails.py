from ._anvil_designer import zzzCustomerDetailsTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class zzzCustomerDetails(zzzCustomerDetailsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    row = {'number': '#112', 'date': 'Yesterday', 'title': 'Something went wrong...', 'response':'Hi Bridget, Here us the problem:'}

    items = []
    for i in range(20):
      items.append(row)
    self.repeating_panel_1.items = items