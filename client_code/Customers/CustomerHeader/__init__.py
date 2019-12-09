from ._anvil_designer import CustomerHeaderTemplate
from anvil import *
import anvil.server
from ..CustomerOverlay import CustomerOverlay

class CustomerHeader(CustomerHeaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def link_1_click(self, **event_args):
    homepage = get_open_form()
    homepage.clear(slot="overlay")
    homepage.add_component(CustomerOverlay(), slot="overlay")


