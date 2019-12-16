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

class DashGraphs(DashGraphsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.progress_percentage.percentage = 0.22
    self.progress_stats.percentage = 0.7
    self.progress_stats.display_value = 55
    self.resolution_graph.labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
    self.resolution_graph.datasets = [{
            'label': 'Resolved',
            'backgroundColor': '#9389DF',
            'borderColor': '#7D71D8',
            'data': [7, 10, 5, 2, 9, 11, 6]
        },{
            'label': 'Unresolved',
            'backgroundColor': '#00FFAF',
            'borderColor': '#00FFAF',
            'data': [2, 3, 11, 12, 5, 6, 6]
        }]
    
#   def display_dashboard_data(self, unassigned, unresolved, urgent):
    
    

