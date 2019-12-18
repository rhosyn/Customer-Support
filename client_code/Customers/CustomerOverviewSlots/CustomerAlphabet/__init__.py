from ._anvil_designer import CustomerAlphabetTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import string

class CustomerAlphabet(CustomerAlphabetTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
#     people = [{'name': 'Daniel Barnes', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
#               {'name': 'Daniel Bercow', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
#               {'name': 'Daniel Bob', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
#               {'name': 'Daniel Barnes', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
#               {'name': 'Daniel Bercow', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
#               {'name': 'Daniel Bob', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'}
#              ]
#     people_c = [{'name': 'Daniel Charles', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
#                 {'name': 'Daniel Coz', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
#                 {'name': 'Daniel Charles', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
#                 {'name': 'Daniel Coz', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
#                 {'name': 'Daniel Charles', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'},
#                 {'name': 'Daniel Coz', 'company': 'Forty8Creates', 'telephone': '+44(0)20 710 13348', 'email':'daniel@forty8creates.com'}
#                ]
    
    
    
#     data = [{'letter':'B', 'people': people},{'letter':'C', 'people': people_c}]
    
#     visible_letters = [x['letter'] for x in data]
    
#     self.repeating_panel_1.items = data
    
#     letters = [{
#         'letter': x,
#         'visible': x in visible_letters
#       } for x in string.ascii_uppercase]

#     self.repeating_panel_1.items = letters
    letters = list(string.ascii_uppercase)
    customers = anvil.server.call('get_customers')
    data = []
    for let in letters:
      people = [x for x in customers if x['last_name'][0].upper() == let]
      if people:
        data.append({'letter': let, 'people':people})
    
    visible_letters = [x['letter'] for x in data]
    letters = [{
        'letter': x,
        'visible': x in visible_letters
      } for x in string.ascii_uppercase]

    self.repeating_panel_1.items = letters