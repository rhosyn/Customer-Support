from ._anvil_designer import DashGraphsTemplate
from anvil import *
import plotly.graph_objs as go
import anvil.server
import anvil.js

class DashGraphs(DashGraphsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    x,y = anvil.server.call('get_data')
    sales1 = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9, 5]
    sales2 = [3, 7, 9, 6, 4, 5, 14, 7, 6, 16, 12]
    
    self.plot_1.data = [go.Line(y=sales1, 
                                x=range(0,12), 
                                fill='tonexty',
                                line=dict(color="#00FFAF"),
                                fillcolor=dict(color="#00FFAF"),
                                name="Unresolved"),
                        go.Line(y=sales2, 
                                x=range(0,12), 
                                fill='tozeroy',
                                fillcolor=dict(color="#8478DA"),
                                line=dict(color="#8478DA"),
                                name="Resolved")
                                
                       ]
    
    self.plot_1.layout = go.Layout(
                          title="Resolution Overview",
                          # expand the graphs
                          margin=dict(
                              l=90, #left margin
                              r=50, #right margin
                              b=50, #bottom margin
                              t=50, #top margin
                          ),
                          font=dict(family='Barlow', size=10),
                          legend=dict(x=0, y=1.2, font=dict(size=12), orientation="h"),
                          # Format x-axis
                          xaxis=dict(
                            showgrid=False,
                            zeroline=False,
                            tickfont=dict(
                                family='Barlow',
                                size=14,
                                color='#808080'
                            ),
                            ticks="outside", 
                            tickwidth=4, 
                            tickcolor='transparent', 
                            ticklen=25, 
                            col=1
                          ),
                          # Format y-axis
                          yaxis=dict(
                              zeroline=False,
                              tickfont=dict(
                                  family='Barlow',
                                  size=14,
                                  color='#808080'
                              ),
                              ticks="outside", 
                              tickwidth=2, 
                              tickcolor='transparent', 
                              ticklen=25, 
                              col=1
                          )
                        )
    

  def form_show(self, **event_args):
    self.custom_1.call_js('drawChart1', 0.75)
    self.custom_2.call_js('drawChart2', 0.6, 100)

