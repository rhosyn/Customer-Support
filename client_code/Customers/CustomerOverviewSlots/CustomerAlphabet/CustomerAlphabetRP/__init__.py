from ._anvil_designer import CustomerAlphabetRPTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class CustomerAlphabetRP(CustomerAlphabetRPTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  
  def letter_link_click(self, **event_args):
    selected_letter = self.item['letter']
    # dgrp_form here is an instance of CustomerOverviewGDRP
    for dgrp_form in get_open_form().current_form.customer_overview.repeating_panel_1.get_components():
      if dgrp_form.item['letter'] == selected_letter:
        dgrp_form.scroll_into_view()


