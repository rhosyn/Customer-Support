from ._anvil_designer import DashGraphsTemplate
from anvil import *
import plotly.graph_objs as go
import anvil.server
import anvil.js

class DashGraphs(DashGraphsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def form_show(self, **event_args):
    self.custom_1.call_js('drawChart1', 0.75)
    self.custom_2.call_js('drawChart2', 0.6, 100)

