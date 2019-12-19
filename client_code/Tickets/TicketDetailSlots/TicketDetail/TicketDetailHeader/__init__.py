from ._anvil_designer import TicketDetailHeaderTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

class TicketDetailHeader(TicketDetailHeaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.ticket = {}
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def form_refreshing_data_bindings(self, **event_args):
    if self.ticket == {} and self.item:
      self.ticket = self.item
      if self.item['due'] < datetime.now():
        self.overdue_label.visible = True

