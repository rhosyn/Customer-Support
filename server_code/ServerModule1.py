import anvil.email
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, timedelta

# Ticket functions 
@anvil.server.callable
def get_tickets(sort, filters={}, date_filter={}):
  ascending = True if sort == 'title' or sort == 'priority' else False
  if date_filter:
    date_filter['end'] += timedelta(days=1)
    return app_tables.tickets.search(tables.order_by(sort, ascending=ascending), date=q.between(date_filter['start'], date_filter['end'], max_inclusive=True), **filters)
  return app_tables.tickets.search(tables.order_by(sort, ascending=ascending), **filters)

@anvil.server.callable
@tables.in_transaction
def add_ticket(ticket_dict, details, customer):
  if not app_tables.customers.has_row(customer):
    customer = add_customer(customer)
  ticket = app_tables.tickets.add_row(
      customer=customer, 
      status='open', 
      date=datetime.now(),
      **ticket_dict
    )
  app_tables.messages.add_row(
      date=datetime.now(),
      ticket=ticket,
      type=app_tables.types.get(name="INTERNAL_NOTE"),
      details=details
  )
  
@anvil.server.callable
def add_message(message_dict, ticket):
  app_tables.messages.add_row(
      date=datetime.now(),
      ticket=ticket,
      **message_dict
  )
#   TODO: send email to customer if type is OUTGOING_EMAIL
# TODO: call add_message when we receive an email from a customer, storing it as INCOMING_EMAIL
  
  
@anvil.server.callable
def update_ticket(ticket, ticket_dict):
  if app_tables.tickets.has_row(ticket):
    if ticket_dict['status'] == 'closed' and not ticket['status'] == 'closed':
      ticket_dict['closed'] = datetime.now()
    ticket.update(**ticket_dict)  
    
@anvil.server.callable
@tables.in_transaction
def delete_tickets(tickets):
  for t in tickets:
    if app_tables.tickets.has_row(t):
      t.delete()
  
@anvil.server.callable
def add_customer(cust_dict):
  cust_dict['created'] = datetime.now()
  return app_tables.customers.add_row(**cust_dict)

@anvil.server.callable
def update_customer(customer, customer_dict):
  if app_tables.customers.has_row(customer):
    customer.update(**customer_dict)  
      
@anvil.server.callable
def get_messages(ticket):
  return app_tables.messages.search(tables.order_by("date", ascending=False), ticket=ticket)

@anvil.server.callable
def get_dashboard_data(start_date, end_date, time_period):
  headline_stats = get_headline_dash_stats(start_date, end_date)
  progress_dash_stats = get_progess_data(start_date, end_date)
  resolution_data = get_resolution_data(start_date, end_date, time_period)
  return headline_stats, progress_dash_stats, resolution_data
  
def get_headline_dash_stats(start_date, end_date):
  unassigned = len(app_tables.tickets.search(agent=None, date=q.between(start_date, end_date)))
  unresolved = len(app_tables.tickets.search(closed=None, date=q.between(start_date, end_date)))
  urgent = len(app_tables.tickets.search(priority="urgent", date=q.between(start_date, end_date)))
  prev_start = start_date - timedelta(days=7)
  d_unassigned = len(app_tables.tickets.search(agent=None, date=q.between(prev_start, start_date))) - unassigned
  d_unresolved = len(app_tables.tickets.search(closed=None, date=q.between(prev_start, start_date))) - unresolved
  d_urgent = len(app_tables.tickets.search(priority="urgent", date=q.between(prev_start, start_date))) - urgent
  return {'unassigned':{'delta':-d_unassigned, 'number':unassigned}, 'unresolved':{'delta':-d_unresolved, 'number':unresolved}, 'urgent':{'delta':-d_urgent, 'number':urgent}}

@anvil.server.callable
def get_resolution_data(start, end, time_period):
  resolved_tickets, new_tickets = get_ticket_data(start, end)
  dates = []
  res = []
  unres = []
  for day in (start + timedelta(n) for n in range(time_period)):
    dates.append(day.strftime('%A, %d'))
    r = len([x for x in resolved_tickets if x['closed'].date() == day])
    res.append(r)
    u = len([x for x in new_tickets if not x['closed'] and x['date'].date() == day])
    unres.append(u)
  data = {'resolved':res, 'unresolved':unres}
  return dates, data

def get_ticket_data(start, end):
  resolved_tickets = app_tables.tickets.search(
    closed=q.between(start, end, max_inclusive=True)
  )
  new_tickets = app_tables.tickets.search(
    date=q.between(start, end, max_inclusive=True)
  )
  return resolved_tickets, new_tickets

@anvil.server.callable
def get_progess_data(start, end):
  resolved_tickets, new_tickets = get_ticket_data(start, end)
#   TODO: condition on the message being one reply to the customer from internal
  closed_on_first = [t for t in resolved_tickets if len(app_tables.messages.search(ticket=t)) == 1]
  new_customers = app_tables.customers.search(
    created=q.between(start, end, max_inclusive=True)
  )
  # Returning customers are those with new tickets who aren't in new_customers
  returning_customers = [x for x in new_tickets if x['customer'] not in new_customers]
  # Returning customers also includes those whose tickets have been resolved during the period (and aren't already acounted for)
  returning_customers += [x for x in resolved_tickets if x['customer'] not in new_customers and x['customer'] not in returning_customers]
  return {'resolved': {'total_resolved': len(resolved_tickets), 'closed_on_first':len(closed_on_first)}, 'customers':{'new_customers':len(new_customers), 'returning_customers':len(returning_customers)}}
  
  
@anvil.server.callable
def get_customers(filters={}):
  return app_tables.customers.search(tables.order_by('name', ascending=True), **filters)

@anvil.server.callable
def get_users():
  return app_tables.users.search()



