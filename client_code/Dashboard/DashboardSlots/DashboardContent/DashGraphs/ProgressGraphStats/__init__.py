from ._anvil_designer import ProgressGraphStatsTemplate
from anvil import *
import anvil.server
from ...... import Dashboard

class ProgressGraphStats(ProgressGraphStatsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.