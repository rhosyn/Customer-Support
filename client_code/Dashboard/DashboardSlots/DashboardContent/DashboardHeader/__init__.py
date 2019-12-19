from ._anvil_designer import DashboardHeaderTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .DashStats import DashStats

class DashboardHeader(DashboardHeaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def display_dashboard_data(self, headline_stats, period):
    self.clear()
    self.add_component(DashStats(title="Unassigned", delta=headline_stats['unassigned']['delta'], value=headline_stats['unassigned']['number'], time_period=period))
    self.add_component(DashStats(title="Unresolved", delta=headline_stats['unresolved']['delta'], value=headline_stats['unresolved']['number'], time_period=period))
    self.add_component(DashStats(title="Urgent", delta=headline_stats['urgent']['delta'], value=headline_stats['urgent']['number'], time_period=period))
    