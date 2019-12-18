from ._anvil_designer import TicketFiltersTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ..TicketInbox import TicketInbox

class TicketFilters(TicketFiltersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.filters = {'status':'open'}
    self.date_filter = {}
    self.all_tickets = anvil.server.call('get_tickets', 'date')
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def filter_tickets(self, **event_args):
    if event_args['sender'].selected_value is None:
      self.filters = {k: v for k, v in self.filters.items() if v is not None}
    self.parent.ticket_inbox.ticket_inbox_content.filter_tickets(self.filters)
    
  def clear_filters_link_click(self, **event_args):
    self.filters = {}
    self.refresh_data_bindings()
    self.parent.ticket_inbox.ticket_inbox_content.filter_tickets(self.filters)

  def date_picker_change(self, **event_args):
    if self.start_date_picker.date and self.end_date_picker.date:
      self.parent.ticket_inbox.ticket_inbox_content.filter_tickets(self.filters, self.date_filter)
      
      





