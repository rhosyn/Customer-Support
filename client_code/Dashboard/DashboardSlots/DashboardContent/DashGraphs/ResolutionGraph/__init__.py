from ._anvil_designer import ResolutionGraphTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class ResolutionGraph(ResolutionGraphTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self._shown = False
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
  @property
  def labels(self):
    return self.display_labels

  @labels.setter
  def labels(self, labels):
    self.display_labels = labels
    self.maybe_draw_chart()
    
  @property
  def datasets(self):
    return self.display_datasets

  @datasets.setter
  def datasets(self, datasets):
    self.display_datasets = datasets
    self.maybe_draw_chart()

  def form_show(self, **event_args):
    self._shown = True
    self.maybe_draw_chart()
    
  def maybe_draw_chart(self):
    if self.display_datasets and self.display_labels and self._shown:
      self.call_js('buildChart', self.display_datasets, self.display_labels)

