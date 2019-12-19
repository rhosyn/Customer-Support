from ._anvil_designer import DashGraphsTemplate
from anvil import *
import anvil.facebook.auth
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
#     self.build_progress_charts()
    
  def build_progress_charts(self, progress_percent, prog2_value, prog2_percent):
    self.progress_percentage.percentage = 0.75
    self.progress_stats.display_value = 500
    self.progress_stats.percentage = 0.2
    
    
  def build_resolution_chart(self, labels, data):
    # This is called initially in the form_show event of the DashboardFilters Form
    self.resolution_graph.labels = labels
    self.resolution_graph.datasets = [{
            'label': 'Resolved',
            'backgroundColor': '#9389DF',
            'borderColor': '#7D71D8',
            'data': data['resolved']
        },{
            'label': 'Unresolved',
            'backgroundColor': '#00FFAF',
            'borderColor': '#00FFAF',
            'data': data['unresolved']
        }]
   





