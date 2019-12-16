from ._anvil_designer import DashboardHeaderTemplate
from anvil import *
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
  
  def display_dashboard_data(self, unassigned, unresolved, urgent):
    self.add_component(DashStats(title="Unassigned", delta=3, value=unassigned, time_period="month"))
    