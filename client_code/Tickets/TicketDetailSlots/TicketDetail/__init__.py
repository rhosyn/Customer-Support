from ._anvil_designer import TicketDetailTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class TicketDetail(TicketDetailTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    print(f"Ticketd: {dict(list(self.item))}")
#     self.populate_replies()
    
  def populate_replies(self):
    replies = anvil.server.call('get_replies', self.item)
    self.ticket_detail_content.replies_repeating_panel.items = replies



