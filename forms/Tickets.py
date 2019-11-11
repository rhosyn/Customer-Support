from anvil import *

class Tickets(TicketsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.repeating_panel_1.items = [
      {'name': 'Usman A', 'title': 'How do I update my DNS records?', 'category': 'Technical Support', 'agent':'Meredydd L', 'priority': 'Urgent', 'date': 'Just now'}
    ]