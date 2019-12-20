from ._anvil_designer import CustomerEditTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .... import Validation

class CustomerEdit(CustomerEditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.customer_copy = {}
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def refresh_data(self):
    self.customer_copy = dict(list(self.item))

  def form_refreshing_data_bindings(self, **event_args):
    if self.customer_copy == {} and self.item:
      self.refresh_data()

  def cancel_link_click(self, **event_args):
    self.refresh_data()
    self.refresh_data_bindings()

  def save_link_click(self, **event_args):
    cust_validation_errors = Validation.get_customer_errors(self.customer_copy)
    if not cust_validation_errors:
      anvil.server.call('update_customer', self.item, self.customer_copy)
      Notification('Customer details updated').show()
      homepage = get_open_form()
      homepage.open_customers()     
    elif cust_validation_errors and tick_validation_errors:
      alert("The following fields are missing for your customer: \n{}.\n\nThe following field are missing for your ticket: \n{}".format(
        ' \n'.join(word for word in cust_validation_errors),
        ' \n'.join(word for word in tick_validation_errors)
      ))
    elif tick_validation_errors and not cust_validation_errors:
      alert("The following ticket fields are missing: \n{}".format(' \n'.join(word for word in tick_validation_errors)))
    elif cust_validation_errors and not tick_validation_errors:
      alert("The following customer fields are missing: \n{}".format(' \n'.join(word for word in cust_validation_errors)))



