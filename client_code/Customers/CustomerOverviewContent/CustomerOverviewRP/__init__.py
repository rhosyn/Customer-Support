from ._anvil_designer import CustomerOverviewRPTemplate
from anvil import *
import anvil.server
from ...CustomerOverlay import CustomerOverlay
from ...CustomerDetailsOverlay import CustomerDetailsOverlay

class CustomerOverviewRP(CustomerOverviewRPTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def check_box_1_change(self, **event_args):
    homepage = get_open_form()
    if self.check_box_1.checked:
      self.role = "customers-repeating-panel-selected"
      homepage.clear(slot="overlay")
      homepage.add_component(CustomerDetailsOverlay(),slot="overlay")
    else:
      self.role = "customers-repeating-panel"
      homepage.clear(slot="overlay")
       

