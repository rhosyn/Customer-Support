from ._anvil_designer import TicketInboxContentTemplate
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

class TicketInboxContent(TicketInboxContentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.filters = {'status':'open'}
    self.selected_tickets = []
    self.filtered_tickets = anvil.server.call('get_tickets', 'date', self.filters)
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.repeating_panel_1.set_event_handler('x-select-ticket', self.select_ticket)
    self.repeating_panel_1.set_event_handler('x-deselect-ticket', self.deselect_ticket)
    
  def select_ticket(self, ticket, **event_args):
    self.selected_tickets.append(ticket)
    
  def deselect_ticket(self, ticket, **event_args):
    self.selected_tickets.remove(ticket)

  def filter_tickets(self, filters, sort='date', date_filter={}):
    # Update self.filters if there are filters
    if filters is not None:
      self.filters = filters 
    self.filtered_tickets = anvil.server.call('get_tickets', sort, self.filters, date_filter)
    self.refresh_data_bindings()
    
  def select_all(self):
    self.selected_tickets = []
    self.selected_tickets += self.repeating_panel_1.items
    for t in self.repeating_panel_1.get_components():
      t.role = "tickets-repeating-panel-selected"
      t.check_box_1.checked = True

  def deselect_all(self):
    self.selected_tickets = []
    for t in self.repeating_panel_1.get_components():
      t.role = "tickets-repeating-panel"
      t.check_box_1.checked = False

  def delete_tickets(self):
    if self.selected_tickets:
      if confirm("Are you sure you want to delete: \n{}?".format(' \n'.join(t['title'] for t in self.selected_tickets))):
        anvil.server.call('delete_tickets', self.selected_tickets)
        self.refresh_data_bindings()
    else:
      alert("No tickets selected")