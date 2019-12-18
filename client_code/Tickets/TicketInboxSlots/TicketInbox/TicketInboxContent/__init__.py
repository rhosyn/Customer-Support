from ._anvil_designer import TicketInboxContentTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class TicketInboxContent(TicketInboxContentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.filters = {'status':'open'}
    self.date_filter = {}
    self.selected_tickets = []
    self.all_tickets = anvil.server.call('get_tickets', 'date')
    self.filtered_tickets = anvil.server.call('get_tickets', 'date', self.filters)
    
    self.init_components(**properties)
    self.repeating_panel_1.set_event_handler('x-select-ticket', self.select_ticket)
    self.repeating_panel_1.set_event_handler('x-deselect-ticket', self.deselect_ticket)
    # Any code you write here will run when the form opens.
    
  def select_ticket(self, ticket, **event_args):
    self.selected_tickets.append(ticket)
    
  def deselect_ticket(self, ticket, **event_args):
    self.selected_tickets.remove(ticket)


