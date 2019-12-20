from ._anvil_designer import TicketNewDetailsOverviewTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class TicketNewDetailsOverview(TicketNewDetailsOverviewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.all_agents = anvil.server.call('get_users')
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def save_ticket_button_click(self, **event_args):
    self.parent.ticket_new_overview.add_ticket(ticket=self.item)

