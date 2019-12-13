from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.graph_objs as go
from ..Tickets.TicketInboxSlots import TicketInboxSlots
from ..Dashboard.DashboardSlots import DashboardSlots
from ..Tickets.TicketDetailSlots import TicketDetailSlots
from ..Customers.CustomerOverviewSlots import CustomerOverviewSlots
from ..Tickets.TicketNewSlots import TicketNewSlots

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    anvil.users.login_with_form()
    self.current_form = DashboardSlots()
    self.add_component(self.current_form, slot="default")
#     self.customer_link.role = 'active'
    

  def dash_link_click(self, **event_args):
    self.clear(slot="overlay")
    self.current_form.remove_from_parent()
    self.current_form = DashboardSlots()
    self.add_component(self.current_form, slot="default")
    self.clear_links()
    self.dash_panel.role = 'dash-link-selected'
    
  def ticket_link_click(self, **event_args):
    self.clear(slot="overlay")
    self.current_form.remove_from_parent()
    self.current_form = TicketInboxSlots()
    self.add_component(self.current_form, slot="default")
    self.clear_links()
    self.ticket_panel.role = 'dash-link-selected'

  def clear_links(self):
    for panel in self.links_panel.get_components():
      panel.role = "dash-link"

  def customer_link_click(self, **event_args):
    self.clear(slot="overlay")
    self.current_form.remove_from_parent()
    self.current_form = CustomerOverviewSlots()
    self.add_component(self.current_form, slot="default")
    self.clear_links()
    self.customer_panel.role = 'dash-link-selected'

  def new_ticket_button_click(self, **event_args):
    self.clear(slot="overlay")
    self.current_form.remove_from_parent()
    self.current_form = TicketNewSlots()
    self.add_component(self.current_form, slot="default")
    self.clear_links()
    self.ticket_panel.role = 'dash-link-selected'





