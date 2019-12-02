from ._anvil_designer import CustomerOverviewContentTemplate
from anvil import *
import anvil.server
import string

class CustomerOverviewContent(CustomerOverviewContentTemplate):
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
    
    self.repeating_panel_2.items = data
    letters = list(string.ascii_lowercase)
    
    alphabet = {}
    for d in data:
      letter = d['letter']
      alphabet[letter] = True
 
    print(alphabet)
    self.repeating_panel_1.items = list(string.ascii_uppercase)