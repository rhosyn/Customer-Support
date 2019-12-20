from ._anvil_designer import TicketDetailRPTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class TicketDetailRP(TicketDetailRPTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def set_to_labels(self):
    if self.item['type']['name'] == "INTERNAL_NOTE":
      return "[INTERNAL NOTE]"
    elif self.item['type']['name'] == "INCOMING_EMAIL":
      return "To: Support"
    else:
      return f"To:{self.item['ticket']['customer']['name']} {self.item['ticket']['customer']['last_name']}"

    # In case we want to also bind colour to whether it's internal or external 
    # "white" if self.item['type']['name'] == "INCOMING_EMAIL" else "rgb(191, 186, 223)"