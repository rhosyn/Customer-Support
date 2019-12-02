from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.server
import plotly.graph_objs as go
from ..Tickets.TicketInboxSlots import TicketInboxSlots
from ..Dashboard.DashboardHome import DashboardHome
from ..Tickets.TicketDetailSlots import TicketDetailSlots
from ..Customers.CustomerOverviewSlots import CustomerOverviewSlots

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.current_form = CustomerOverviewSlots()
    self.add_component(self.current_form, slot="default")
    self.customer_link.role = 'active'

  def dash_link_click(self, **event_args):
    self.current_form.remove_from_parent()
    self.current_form = DashboardHome()
    self.add_component(self.current_form, slot="default")
    self.clear_links()
    self.dash_link.role = 'active'
    
  def ticket_link_click(self, **event_args):
    self.current_form.remove_from_parent()
    self.current_form = TicketInboxSlots()
    self.add_component(self.current_form, slot="default")
    self.clear_links()
    self.ticket_link.role = 'active'

  def clear_links(self):
    for link in self.links_panel.get_components():
      link.role = ""

  def customer_link_click(self, **event_args):
    self.current_form.remove_from_parent()
    self.current_form = CustomerOverviewSlots()
    self.add_component(self.current_form, slot="default")
    self.clear_links()
    self.customer_link.role = 'active'




