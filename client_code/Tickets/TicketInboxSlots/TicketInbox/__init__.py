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

  def link_3_click(self, **event_args):
    self.ticket_inbox_content.data_grid_1.next_page()
    
  def set_pages(self):
    page = self.ticket_inbox_content.data_grid_1.get_page() + 1
    start_page = (page+1 * 8)
    text = f"Tickets {start_page}-{start_page+8} of {len(self.ticket_inbox_content.repeating_panel_1.items)}"
    print(text)










