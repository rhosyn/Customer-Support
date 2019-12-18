from ._anvil_designer import DashStatsTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class DashStats(DashStatsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._my_time_period = None
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
  @property
  def value(self):
    return self.value_label.text

  @value.setter
  def value(self, value):
    self.value_label.text = value
    
  @property
  def title(self):
    return self.title_label.text

  @title.setter
  def title(self, value):
    self.title_label.text = value
    
  @property
  def delta(self):
    return self.delta_label.text

  @delta.setter
  def delta(self, value):
    if value == 0:
      self.delta_label.text = "Unchanged"
      self.role = ""
      self.delta_label.icon = None
      self.delta_label.role = ""
    else:
      self.delta_label.text = value if value > 0 else -value
      self.delta_label.icon = "fa:arrow-up" if value > 0 else "fa:arrow-down"
      self.role = "dash-up" if value > 0 else "dash-down"
      self.delta_label.role = "dash-up" if value > 0 else "dash-down"
    
  @property
  def time_period(self):
    return self._my_time_period

  @time_period.setter
  def time_period(self, value):
    self._my_time_period = value
    self.time_period_label.text = " vs previous " + value + " days"