from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.server
import plotly.graph_objs as go
from ..Tickets import TicketInboxSlots
from ..Dashboard.DashboardHome import DashboardHome

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.current_form = DashboardHome()
    self.add_component(self.current_form, slot="default")
    self.dash_link.role = 'active'

  def link_2_click(self, **event_args):
    self.current_form.remove_from_parent()
    self.current_form = DashboardHome()
    self.add_component(self.current_form, slot="default")
    self.dash_link.role = 'active'
    
  def link_3_click(self, **event_args):
    self.current_form.remove_from_parent()
    self.current_form = TicketInboxSlots()
    self.add_component(self.current_form, slot="default")
    self.ticket_link.role = 'active'


