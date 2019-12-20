from ._anvil_designer import TicketNewOverviewTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .... import Validation
from ....Dashboard.DashboardSlots import DashboardSlots

class TicketNewOverview(TicketNewOverviewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.selected_customer = {}
    self.new_customer = {}
    self.new = True
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    # 'x-get-search-keys' is called on text_box_search 'focus' event
    self.search_hints_1.set_event_handler('x-get-search-keys', self.search_customers)
    # 'x-search-hints-result' is called when a result is selected
    self.search_hints_1.set_event_handler('x-search-hints-result', self.update_result_label)
    # 'x-new-customer' is called when the 'Add new' button is clicked
    self.search_hints_1.set_event_handler('x-new-customer', self.new_customer_button_click)
    self.search_hints_1.text_box_search.placeholder = "Search customers"
    
  def search_customers(self, **event_args):
    self.new = False
    self.new_customer_box.visible = False
    return anvil.server.call('get_customers')
  
  def update_result_label(self, result, **event_args):
    self.selected_customer = result
    self.customer_copy = dict(list(self.selected_customer))
    self.refresh_data_bindings()
    self.search_hints_1.text_box_search.text = f"{result['name']} {result['last_name']}"
    
  def new_customer_button_click(self, **event_args):
    self.new = True
    self.search_hints_1.repeating_panel_results.items = []
    self.search_hints_1.text_box_search.text = ""
    self.new_customer_box.visible = True
    
  def add_ticket(self, ticket):
    print(ticket['due'])
    if self.new:
      customer = self.new_customer
      cust_validation_errors = Validation.get_customer_errors(customer)
    else:
      customer = self.selected_customer
      cust_validation_errors = None
    tick_validation_errors = Validation.get_ticket_errors(ticket)
    if not cust_validation_errors and not tick_validation_errors:
      anvil.server.call('add_ticket', ticket, customer)
      Notification('ticket added').show()
      homepage = get_open_form()
      homepage.clear(slot="overlay")
      homepage.clear(slot="default")
      homepage.add_component(DashboardSlots() ,slot="default")
    elif cust_validation_errors and tick_validation_errors:
      alert("The following fields are missing for your customer: \n{}.\n\nThe following field are missing for your ticket: \n{}".format(
        ' \n'.join(word for word in cust_validation_errors),
        ' \n'.join(word for word in tick_validation_errors)
      ))
    elif tick_validation_errors and not cust_validation_errors:
      alert("The following ticket fields are missing: \n{}".format(' \n'.join(word for word in tick_validation_errors)))
    elif cust_validation_errors and not tick_validation_errors:
      alert("The following customer fields are missing: \n{}".format(' \n'.join(word for word in cust_validation_errors)))
