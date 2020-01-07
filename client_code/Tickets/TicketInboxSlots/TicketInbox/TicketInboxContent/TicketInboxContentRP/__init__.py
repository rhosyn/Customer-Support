from ._anvil_designer import TicketInboxContentRPTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .....TicketDetailSlots import TicketDetailSlots
from datetime import datetime

class TicketInboxContentRP(TicketInboxContentRPTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.date_label.text = self.item['date'].strftime("%d %b %Y")
    self.overdue_label.visible = self.item['due'] < datetime.now()


  def ticket_title_link_click(self, **event_args):
    homepage = get_open_form()
    homepage.open_ticket_details_form(item=self.item)
    
  def check_box_1_change(self, **event_args):
    if self.check_box_1.checked:
      self.parent.raise_event('x-select-ticket', ticket=self.item)
      self.role = "tickets-repeating-panel-selected"
    else:
      self.parent.raise_event('x-deselect-ticket', ticket=self.item)
      self.role = "tickets-repeating-panel"


