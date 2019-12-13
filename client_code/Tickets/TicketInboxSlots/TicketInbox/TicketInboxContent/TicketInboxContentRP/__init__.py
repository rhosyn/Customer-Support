from ._anvil_designer import TicketInboxContentRPTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .....TicketDetailSlots import TicketDetailSlots

class TicketInboxContentRP(TicketInboxContentRPTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.


  def ticket_title_link_click(self, **event_args):
    homepage = get_open_form()
    homepage.current_form.remove_from_parent()
    homepage.current_form = TicketDetailSlots(item=self.item)
    homepage.add_component(homepage.current_form, slot="default")
    homepage.ticket_link.role = 'active'
    

