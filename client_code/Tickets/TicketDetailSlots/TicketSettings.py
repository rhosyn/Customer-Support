from ._anvil_designer import TicketSettingsTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from ... import Validation

class TicketSettings(TicketSettingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.ticket_copy = {}
    self.all_tickets = anvil.server.call('get_tickets', 'date')
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def cancel_link_click(self, **event_args):
    self.ticket_copy = dict(list(self.item))
    self.refresh_data_bindings()

  def save_link_click(self, **event_args):
    tick_validation_errors = Validation.get_ticket_settings_errors(self.ticket_copy)
    if not tick_validation_errors:
      anvil.server.call('update_ticket', self.item, self.ticket_copy)
      Notification('Ticket updated').show()
      homepage = get_open_form()
      homepage.open_tickets()     
    else:
      alert("\nThe following field are missing for your ticket: \n{}".format(
        ' \n'.join(word for word in tick_validation_errors)
      ))
    

  def form_refreshing_data_bindings(self, **event_args):
    if self.ticket_copy == {} and self.item:
      self.ticket_copy = dict(list(self.item))








