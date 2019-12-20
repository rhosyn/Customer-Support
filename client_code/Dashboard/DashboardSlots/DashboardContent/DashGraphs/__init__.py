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
    
  def build_progress_charts(self, progress_dash_stats):
    # This is called initially in the form_show event of the DashboardFilters Form
    total_resolved = progress_dash_stats['resolved']['total_resolved']
    closed_on_first = progress_dash_stats['resolved']['closed_on_first']
    closed_on_first_percent = max((closed_on_first/total_resolved), 0)
    self.progress_percentage.percentage = closed_on_first_percent
    self.closed_on_first_label.text = f"{closed_on_first/100}% of tickets were resolved with the first reply"
    new_customers = progress_dash_stats['customers']['new_customers']
    returning_customers = progress_dash_stats['customers']['returning_customers']
    self.progress_stats.display_value = new_customers
    self.progress_stats.percentage = max((returning_customers / (new_customers + returning_customers)),0)
    self.new_custs_label.text = f"{new_customers} new customers \n{returning_customers} returning customers"
    
    
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
   





