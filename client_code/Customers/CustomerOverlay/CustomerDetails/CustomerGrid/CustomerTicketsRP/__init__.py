from ._anvil_designer import CustomerTicketsRPTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ......Tickets.TicketDetailSlots import TicketDetailSlots

class CustomerTicketsRP(CustomerTicketsRPTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.date_label.text = self.item['date'].strftime("%d %b %Y")

  def title_link_click(self, **event_args):
    homepage = get_open_form()
    homepage.open_ticket_details_form(item=self.item)
    
  def get_message(self):
    messages = anvil.server.call('get_messages', self.item)
    first_message = messages[len(messages) - 1]
    return f"{first_message['details'][0:25]}..."