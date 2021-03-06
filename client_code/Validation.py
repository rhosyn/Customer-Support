import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

required_customer_keys = ['name', 'title', 'company', 'email', 'phone']
required_ticket_keys = ['title', 'priority', 'category', 'due', 'agent']
required_ticket_settings_keys = ['title', 'status', 'priority', 'category', 'agent', 'due']
required_message_keys = ['type', 'details']

def get_customer_errors(customer_dict):
  missing_keys = []
  for k in required_customer_keys:
    if not customer_dict.get(k, None):
      missing_keys.append(k)
  if missing_keys != []:
    return missing_keys
  else:
    return None
  
def get_ticket_errors(ticket_dict):
  missing_keys = []
  for k in required_ticket_keys:
    if not ticket_dict.get(k, None):
      missing_keys.append(k)
  if missing_keys != []:
    return missing_keys
  else:
    return None
  
def get_ticket_settings_errors(ticket_dict):
  missing_keys = []
  for k in required_ticket_settings_keys:
    if not ticket_dict.get(k, None):
      missing_keys.append(k)
  if missing_keys != []:
    return missing_keys
  else:
    return None

def get_message_errors(message_dict):
  missing_keys = []
  for k in required_message_keys:
    if not message_dict.get(k, None):
      missing_keys.append(k)
  if missing_keys != []:
    return missing_keys
  else:
    return None