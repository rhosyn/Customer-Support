from ._anvil_designer import DashGraphsTemplate
from anvil import *
import plotly.graph_objs as go
import anvil.server

class DashGraphs(DashGraphsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    x,y = anvil.server.call('get_data')
    positive_y = []
    for i in y:
      positive_y.append(i+2)
    
    y2 = []
    for i in y:
      y2.append(i +2/2)
      
#     x2 = []
#     for i in x:
#       x2.append(i+2)
    
    self.plot_1.data = [go.Line(y=y2, 
                                x=x, 
                                fill='tozeroy',
                                line=dict(color="#00FFAF"),
                                name="Unresolved"),
                        go.Line(y=positive_y, 
                                x=x, 
                                fill='tonexty', 
                                line=dict(color="#8478DA"),
                                name="Resolved"),
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
                          legend=dict(x=0, y=1.2, font=dict(size=18), orientation="h"),
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
    
    
    labels1 = ['Unresolved','Resolved',]
    labels2 = ['New','Returning']
    values1 = [0.25, 0.75]
    values2 = [0.55,0.35]
    self.plot_2.data = go.Pie(values=values1, labels=labels1, hole=.85,marker=dict(colors=['gray', '#8478DA']),textinfo='none')
    self.plot_3.data = go.Pie(values=values2, labels=labels2, hole=.85,marker=dict(colors=['#2e2951', '#8478DA']),textinfo='none')
    layout_pie = go.Layout(margin=dict(
                              l=0, #left margin
                              r=0, #right margin
                              b=0, #bottom margin
                              t=0, #top margin
                          ),showlegend=False,
                          )
    self.plot_3.layout = layout_pie
    self.plot_2.layout = layout_pie
    
    
    