from anvil import *
import plotly.graph_objs as go
from .TicketsForm import TicketsForm
from Dashboard import Dashboard

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.current_form = TicketsForm()
    self.add_component(self.current_form, slot="default")
    self.ticket_link.role = 'active'

  def link_2_click(self, **event_args):
    self.current_form.remove_from_parent()
    self.current_form = Dashboard()
    self.add_component(self.current_form, slot="default")
    self.dash_link.role = 'active'
    
    
  def link_3_click(self, **event_args):
    self.current_form.remove_from_parent()
    self.current_form = TicketsForm()
    self.add_component(self.current_form, slot="default")
    self.ticket_link.role = 'active'


