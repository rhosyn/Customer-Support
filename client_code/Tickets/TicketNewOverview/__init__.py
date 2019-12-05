from ._anvil_designer import TicketNewOverviewTemplate
from anvil import *
import anvil.server

class TicketNewOverview(TicketNewOverviewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.