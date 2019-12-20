from ._anvil_designer import TicketInboxTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class TicketInbox(TicketInboxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.set_pages()


  def select_all_box_change(self, **event_args):
    if self.select_all_box.checked:
      self.ticket_inbox_content.select_all()
    else:
      self.ticket_inbox_content.deselect_all()
    

  def clear_selected_link_click(self, **event_args):
    self.ticket_inbox_content.deselect_all()
    self.select_all_box.checked = False

  def sort_dropdown_change(self, **event_args):
    sort = self.sort_dropdown.selected_value.lower()
    self.ticket_inbox_content.filter_tickets(filters=None, sort=sort)

  def delete_tickets_link_click(self, **event_args):
    self.ticket_inbox_content.delete_tickets()


  def previous_page_link_click(self, **event_args):
    self.ticket_inbox_content.data_grid_1.previous_page()
    self.set_pages()
    self.refresh_data_bindings()

  def next_page_link_click(self, **event_args):
    self.ticket_inbox_content.data_grid_1.next_page()
    self.set_pages()
    self.refresh_data_bindings()
    
  def set_pages(self):
    page = self.ticket_inbox_content.data_grid_1.get_page()
    start_page = ((page + 1) * 8)
    end_page = min(start_page, len(self.ticket_inbox_content.repeating_panel_1.items))
    text = f"Tickets {(page * 8) + 1}-{end_page} of {len(self.ticket_inbox_content.repeating_panel_1.items)}"
    return text


    











