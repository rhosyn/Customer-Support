from ._anvil_designer import TicketNewContentTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class TicketNewContent(TicketNewContentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    row = {'name': 'Usman A', 'title': 'How do I update my DNS records?', 'category': 'Technical Support', 'agent':'Meredydd L', 'priority': 'Urgent', 'date': 'Just now'}

    items = []
    for i in range(20):
      items.append(row)
    self.repeating_panel_1.items = items