from ._anvil_designer import TicketDetailContentTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class TicketDetailContent(TicketDetailContentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.replies = None
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
  
  def populate_replies(self):
    self.replies = anvil.server.call('get_replies', self.item)
    self.replies_repeating_panel.items = self.replies

  def form_refreshing_data_bindings(self, **event_args):
    if self.replies is None and self.item:
      print(f"getting replies for {self.item['title']}")
      self.populate_replies()


  
