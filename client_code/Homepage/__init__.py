from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.facebook.auth
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
from ..Tickets.TicketDetailSlots import TicketDetailSlots

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    anvil.users.login_with_form()
    self.current_form = TicketInboxSlots()
    self.add_component(self.current_form, slot="default")
    self.ticket_panel.role = 'dash-link-selected'
    self.headline_label.text = "Tickets"
    
  def open_dashboard(self):
    self.clear(slot="overlay")
    self.clear(slot="default")
    self.headline_label.text = "Dashboard"
    self.current_form = DashboardSlots()
    self.add_component(self.current_form, slot="default")
    self.clear_links()
    self.dash_panel.role = 'dash-link-selected'
  
  def open_tickets(self):
    self.clear(slot="overlay")
    self.clear(slot="default")
    self.headline_label.text = "Tickets"
    self.current_form = TicketInboxSlots()
    self.add_component(self.current_form, slot="default")
    self.clear_links()
    self.ticket_panel.role = 'dash-link-selected'
    
  def open_ticket_details_form(self, item):
    self.clear(slot="overlay")
    self.clear(slot="default")
    self.headline_label.text = "Tickets"
    self.current_form = TicketDetailSlots(item=item)
    self.add_component(self.current_form, slot="default")
    self.clear_links()
    self.ticket_panel.role = 'dash-link-selected'
    
  def open_new_ticket_form(self):
    self.clear(slot="overlay")
    self.clear(slot="default")
    self.headline_label.text = "Tickets"
    self.current_form = TicketNewSlots()
    self.add_component(self.current_form, slot="default")
    self.clear_links()
    self.ticket_panel.role = 'dash-link-selected'
    
    
  def open_customers(self):
    self.clear(slot="overlay")
    self.clear(slot="default")
    self.headline_label.text = "Customers"
    self.current_form = CustomerOverviewSlots()
    self.add_component(self.current_form, slot="default")
    self.clear_links()
    self.customer_panel.role = 'dash-link-selected'
    
    
  def dash_link_click(self, **event_args):
    self.open_dashboard()
    
  def ticket_link_click(self, **event_args):
    self.open_tickets()
  
  def customer_link_click(self, **event_args):
    self.open_customers()
    
  def new_ticket_button_click(self, **event_args):
    self.open_new_ticket_form()
    
  def clear_links(self):
    for panel in self.links_panel.get_components():
      panel.role = "dash-link"


    


    





