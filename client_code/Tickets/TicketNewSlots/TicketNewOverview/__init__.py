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
    self.search_hints_1.text_box_search.placeholder = "Search customers"
    
  def search_customers(self, **event_args):
    self.new = False
#     self.new_customer_box.visible = False
    return anvil.server.call('get_customers')
  
  def update_result_label(self, result, **event_args):
    self.selected_customer = result
    self.customer_copy = dict(list(self.selected_customer))
    self.refresh_data_bindings()
#     self.selected_customer_box.visible = True
    self.search_hints_1.text_box_search.text = result['name']
    
  def new_customer_button_click(self, **event_args):
    self.new = True
    self.search_hints_1.text_box_search.text = ""
#     self.new_customer_box.visible = True
#     self.selected_customer_box.visible = False