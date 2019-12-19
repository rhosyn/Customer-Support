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
  ascending = True if sort == 'title' else False
  if date_filter:
    date_filter['end'] += timedelta(days=1)
    return app_tables.tickets.search(tables.order_by(sort, ascending=ascending), date=q.between(date_filter['start'], date_filter['end'], max_inclusive=True), **filters)
  return app_tables.tickets.search(tables.order_by(sort, ascending=ascending), **filters)

@anvil.server.callable
@tables.in_transaction
def delete_tickets(tickets):
  for t in tickets:
    if app_tables.tickets.has_row(t):
      t.delete()
      
@anvil.server.callable
def get_replies(ticket):
  print("getting replies for {}".format(ticket['title']))
  return app_tables.replies.search(tables.order_by("date", ascending=False), ticket=ticket)

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
  closed_on_first = [t for t in resolved_tickets if len(app_tables.replies.search(ticket=t)) == 1]
  new_customers = app_tables.customers.search(
    created=q.between(start, end, max_inclusive=True)
  )
  returning_customers = [x for x in new_tickets if x['customer'] not in new_customers]
  return {'resolved': {'total_resolved': len(resolved_tickets), 'closed_on_first':len(closed_on_first)}, 'customers':{'new_customers':len(new_customers), 'returning_customers':len(returning_customers)}}
  
  
@anvil.server.callable
def get_customers():
  return app_tables.customers.search()




