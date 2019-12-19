from ._anvil_designer import ProgressGraphPercentageTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class ProgressGraphPercentage(ProgressGraphPercentageTemplate):
  def __init__(self, **properties):
    self._shown = False
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
  @property
  def percentage(self):
    return self.value

  @percentage.setter
  def percentage(self, percentage):
    self.value = percentage
    
  def form_show(self, **event_args):
    self._shown = True
    self.maybe_draw_chart()
    
  def maybe_draw_chart(self):
    if self.percentage is not None and self._shown:
      self.call_js('drawChart1', self.value)
    

