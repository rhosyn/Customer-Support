from ._anvil_designer import TicketInboxTemplate
from anvil import *
import anvil.server

class TicketInbox(TicketInboxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.