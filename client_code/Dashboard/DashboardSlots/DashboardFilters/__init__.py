from ._anvil_designer import DashboardFiltersTemplate
from anvil import *
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
    self.start_date = datetime.today() - timedelta(days=7)
    self.end_date = datetime.today()
    self.start_date_picker.date = self.start_date.date()
    self.end_date_picker.date = self.end_date.date()
    
  def end_date_picker_change(self, **event_args):
    self.start_date = self.start_date_picker.date
    self.end_date = self.end_date_picker.date
    self.get_dashboard_data()
    
  def get_dashboard_data(self):
    print((self.end_date.date() - self.start_date.date()))
    unassigned, unresolved, urgent, d_unassigned, d_unresolved, d_urgent = anvil.server.call('get_dashboard_data', self.start_date, self.end_date)
    self.parent.dash_content.dashboard_header.display_dashboard_data(unassigned, unresolved, urgent, d_unassigned, d_unresolved, d_urgent, period)

  def form_show(self, **event_args):
    self.get_dashboard_data()

