from ._anvil_designer import CustomerOverviewTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import string

class CustomerOverview(CustomerOverviewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.selected_customers = []
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.repeating_panel_1.set_event_handler('x-select-customer', self.select_customer)
    self.repeating_panel_1.set_event_handler('x-deselect-customer', self.deselect_customer)
    
    letters = list(string.ascii_uppercase)
    customers = anvil.server.call('get_customers')
    data = []
    for let in letters:
      people = [x for x in customers if x['last_name'][0].upper() == let]
      if people:
        data.append({'letter': let, 'people':people})
    self.repeating_panel_1.items = data


  def select_all_box_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass
  
  def select_customer(self, customer, **event_args):
    self.selected_customers.append(customer)
    
  def deselect_customer(self, customer, **event_args):
    self.selected_customers.remove(customer)
    
  def select_all(self):
    self.selected_customers = []
    self.selected_customers += self.repeating_panel_1.items
    for t in self.repeating_panel_1.get_components():
      t.role = "tickets-repeating-panel-selected"
      t.check_box_1.checked = True

  def deselect_all(self):
    self.selected_customers = []
    for t in self.repeating_panel_1.get_components():
      t.role = "customers-repeating-panel"
      t.check_box_1.checked = False


