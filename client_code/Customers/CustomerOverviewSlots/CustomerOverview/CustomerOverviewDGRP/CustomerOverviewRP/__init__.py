from ._anvil_designer import CustomerOverviewRPTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .....CustomerOverlay import CustomerOverlay
from .....CustomerDetailsOverlay import CustomerDetailsOverlay

class CustomerOverviewRP(CustomerOverviewRPTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.


  def check_box_1_change(self, **event_args):
    if self.check_box_1.checked:
      get_open_form().current_form.customer_overview.repeating_panel_1.raise_event('x-select-customer', customer=self.item)
      self.parent.parent.parent
      self.role = "customers-repeating-panel-selected"
    else:
      self.parent.raise_event('x-select-ticket', ticket=self.item)
      self.role = "customers-repeating-panel"


  def customer_link_click(self, **event_args):
    homepage = get_open_form()
    homepage.clear(slot="overlay")
    homepage.add_component(CustomerDetailsOverlay(item=self.item),slot="overlay")



