from ._anvil_designer import TicketInboxContentRPTemplate
from anvil import *
import anvil.server

class TicketInboxContentRP(TicketInboxContentRPTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.