from ._anvil_designer import DashboardFiltersTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, timedelta
from ..DashboardContent import DashGraphs

class DashboardFilters(DashboardFiltersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.start_date = datetime.today() - timedelta(days=6)
    self.end_date = datetime.today()
    self.start_date_picker.date = self.start_date.date()
    self.end_date_picker.date = self.end_date.date()
    self.time_period = (self.end_date - self.start_date).days
    
  def end_date_picker_change(self, **event_args):
    self.get_dashboard_data()
    self.get_resolution_plots()
    
  def get_dashboard_data(self):
    self.start_date = self.start_date_picker.date
    self.end_date = self.end_date_picker.date + timedelta(days=1)
    self.time_period = (self.end_date - self.start_date).days
    headline_stats, progress_dash_stats, resolution_data = anvil.server.call('get_dashboard_data', self.start_date, self.end_date, self.time_period)
    print(headline_stats)
    print(progress_dash_stats)
    print(resolution_data)
#     unassigned, unresolved, urgent, d_unassigned, d_unresolved, d_urgent = anvil.server.call('get_dashboard_data', self.start_date, self.end_date, self.time_period)
#     self.parent.dash_content.dashboard_header.display_dashboard_data(unassigned, unresolved, urgent, d_unassigned, d_unresolved, d_urgent, str(self.time_period))

  def get_resolution_plots(self):
    labels, data = anvil.server.call('get_plots', self.start_date, self.end_date, self.time_period)
    self.parent.dash_content.dash_graphs.build_resolution_chart(labels, data)
  
  def get_progress_plots(self):
    data = anvil.server.call('get_progress_data', self.start_date, self.end_date, self.time_period)
    self.parent.dash_content.dash_graphs.build_progress_charts(progress_percent, prog2_value, prog2_percent)
  
  def form_show(self, **event_args):
    self.get_dashboard_data()
    self.get_resolution_plots()

