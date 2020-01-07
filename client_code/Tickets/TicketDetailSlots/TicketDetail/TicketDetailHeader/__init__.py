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

  def delete_ticket_button_click(self, **event_args):
    if confirm(f"Are you sure you want to delete: \n{self.item['title']}?"):
      # Delete tickets expects a list of tickets so pass self.item as a list 
      anvil.server.call('delete_tickets', [self.item])
      homepage = get_open_form()
      homepage.open_tickets()

  def reply_button_click(self, **event_args):
    self.parent.ticket_detail_content.ticket_reply.visible = True






