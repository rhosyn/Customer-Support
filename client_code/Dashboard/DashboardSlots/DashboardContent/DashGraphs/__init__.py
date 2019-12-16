from ._anvil_designer import DashGraphsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objs as go
import anvil.server
import anvil.js

def set_data(data):
  print(data)

class DashGraphs(DashGraphsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
#     print(self.parent)
#     anvil.server.call('get_plots', DashboardFilters().start_date, DashboardFilters.start_date)

  def set_data(self, data):
    print(data)

  def form_show(self, **event_args):
    self.custom_1.call_js('drawChart1', 0.75)
    self.custom_2.call_js('drawChart2', 0.6, 100)
    
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
    datasets = [{
            'label': 'Resolved',
            'backgroundColor': '#9389DF',
            'borderColor': '#7D71D8',
            'data': [8, 10, 5, 2, 9, 11, 6]
        },{
            'label': 'Unresolved',
            'backgroundColor': '#00FFAF',
            'borderColor': '#00FFAF',
            'data': [4, 3, 11, 12, 5, 6, 6]
        }]
    self.custom_3.call_js('buildChart', datasets, labels)

