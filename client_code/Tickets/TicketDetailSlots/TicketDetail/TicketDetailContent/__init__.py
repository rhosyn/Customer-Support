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
from datetime import datetime
from ..... import Validation

class TicketDetailContent(TicketDetailContentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.messages = None
    self.message = {}
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
     
  def populate_messages(self):
    self.messages = anvil.server.call('get_messages', self.item)
    self.messages_repeating_panel.items = self.messages
    
  def populate_to_dropdown(self):
    internal = app_tables.types.get(name="INTERNAL_NOTE")
    external = app_tables.types.get(name="OUTGOING_EMAIL")
    self.to_dropdown.items = [(f"{self.item['customer']['name']} {self.item['customer']['last_name']}", external), ('Internal Note', internal)]
    self.message['type'] = external

  def form_refreshing_data_bindings(self, **event_args):
    if self.messages is None and self.item:
      self.populate_messages()
      self.populate_to_dropdown()

  def send_reply_button_click(self, **event_args):
    message_validation_errors = Validation.get_message_errors(self.message)
    if not message_validation_errors:
      anvil.server.call('add_message', self.message, self.item)
      Notification('Reply added').show()
      homepage = get_open_form()
      homepage.open_ticket_details_form(self.item)
    else:
      alert("\nThe following field are missing for your reply: \n{}".format(
        ' \n'.join(word for word in message_validation_errors)
      ))
    
  def cancel_reply_button_click(self, **event_args):
    self.reply_details_box.text = ""
    self.populate_to_dropdown()
    self.ticket_reply.visible = False



  
