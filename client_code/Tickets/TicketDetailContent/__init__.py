from ._anvil_designer import TicketDetailContentTemplate
from anvil import *
import anvil.server

class TicketDetailContent(TicketDetailContentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    row = {'name': 'Usman A', 'title': 'How do I update my DNS records?', 'category': 'Technical Support', 'agent':'Meredydd L', 'priority': 'Urgent', 'date': 'Just now'}

    items = []
    for i in range(20):
      items.append(row)
    self.repeating_panel_1.items = items