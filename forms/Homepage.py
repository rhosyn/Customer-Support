from anvil import *
import plotly.graph_objs as go
from .TicketsForm import TicketsForm
from Dashboard import Dashboard

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.content_panel.add_component(TicketsForm(), full_width_row=True)
    self.ticket_link.role = 'active'

  def link_2_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Dashboard(), full_width_row=True)
    self.dash_link.role = 'active'
    
    
  def link_3_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(TicketsForm(), full_width_row=True)
    self.ticket_link.role = 'active'


