from ._anvil_designer import CustomerHeaderTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ....CustomerOverlay import CustomerOverlay

class CustomerHeader(CustomerHeaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.


  def close_pane_link_click(self, **event_args):
    homepage = get_open_form()
    homepage.clear(slot="overlay")

  def edit_customer_link_click(self, **event_args):
    homepage = get_open_form()
    homepage.clear(slot="overlay")
    homepage.add_component(CustomerOverlay(), slot="overlay")




