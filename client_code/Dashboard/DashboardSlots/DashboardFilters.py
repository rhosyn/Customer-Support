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

class DashboardFilters(DashboardFiltersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.start_date = datetime.today() - timedelta(days=7)
    self.end_date = datetime.today()
    self.start_date_picker.date = self.start_date.date()
    self.end_date_picker.date = self.end_date.date()