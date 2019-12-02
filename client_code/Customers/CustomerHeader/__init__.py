from ._anvil_designer import CustomerHeaderTemplate
from anvil import *
import anvil.server
from ..CustomerOverviewEditSlots import CustomerOverviewEditSlots

class CustomerHeader(CustomerHeaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def link_1_click(self, **event_args):
    homepage = get_open_form()
    homepage.current_form.remove_from_parent()
    homepage.current_form = CustomerOverviewEditSlots()
    homepage.add_component(homepage.current_form, slot="default")
    homepage.customer_link.role = 'active'

