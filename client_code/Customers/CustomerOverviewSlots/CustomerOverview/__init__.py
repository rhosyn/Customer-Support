from ._anvil_designer import CustomerOverviewTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class CustomerOverview(CustomerOverviewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    people = [{'name': 'Daniel Barnes', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
              {'name': 'Daniel Bercow', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
              {'name': 'Daniel Bob', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
              {'name': 'Daniel Barnes', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
              {'name': 'Daniel Bercow', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
              {'name': 'Daniel Bob', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'}
             ]
    people_c = [{'name': 'Daniel Charles', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
                {'name': 'Daniel Coz', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
                {'name': 'Daniel Charles', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
                {'name': 'Daniel Coz', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
                {'name': 'Daniel Charles', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
                {'name': 'Daniel Coz', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'}
               ]
    
    
    
    data = [{'letter':'B', 'people': people},{'letter':'C', 'people': people_c}]
    
    self.repeating_panel_1.items = data