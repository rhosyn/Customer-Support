from ._anvil_designer import CustomerGridTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .CustomerTicketsRP import CustomerTicketsRP

class CustomerGrid(CustomerGridTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.customer_tickets = None
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def form_refreshing_data_bindings(self, **event_args):
    if self.customer_tickets is None and self.item:
      self.customer_tickets = anvil.server.call('get_tickets', 'date', filters={'customer': self.item})  


  
