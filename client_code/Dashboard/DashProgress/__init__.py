from ._anvil_designer import DashProgressTemplate
from anvil import *
import anvil.server

class DashProgress(DashProgressTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def form_show(self, **event_args):
    self.call_js('updateValue', 0.75)

