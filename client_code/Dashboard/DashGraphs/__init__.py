from ._anvil_designer import DashGraphsTemplate
from anvil import *
import plotly.graph_objs as go
import anvil.server

class DashGraphs(DashGraphsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    line1 = [30,35,30,25,21,20,40,45,43,33,25,10]
    line2 = [19,10,21,16,30,28,22,10,26,40,41,43]
    x=[1,2,3,4,5,6,7,8,9,10,11,12]
    
    trace1 = go.Line(y=line1, x=x)
    trace2 = go.Line(y=line2, x=x)
    
    self.plot_1.data = [trace1, trace2]