import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import timedelta


@anvil.server.callable
def get_tickets(sort, filters={}, date_filter={}):
  ascending = True if sort == 'title' else False
  if date_filter:
    start_date = datetime.combine(date_filter['date'] , datetime.min.time())
    end_date = start_date + timedelta(days=1)
    return app_tables.tickets.search(tables.order_by(sort, ascending=ascending), date=q.between(start_date, end_date), **filters)
  return app_tables.tickets.search(tables.order_by(sort, ascending=ascending), **filters)


@anvil.server.callable
def get_dashboard_data(start_date, end_date):
  unassigned = len(app_tables.tickets.search(agent=None, date=q.between(start_date, end_date)))
  unresolved = len(app_tables.tickets.search(closed=None, date=q.between(start_date, end_date)))
  urgent = len(app_tables.tickets.search(priority="urgent", date=q.between(start_date, end_date)))
  prev_start = start_date - timedelta(days=7)
  d_unassigned = len(app_tables.tickets.search(agent=None, date=q.between(prev_start, start_date))) - unassigned
  d_unresolved = len(app_tables.tickets.search(closed=None, date=q.between(prev_start, start_date))) - unresolved
  d_urgent = len(app_tables.tickets.search(priority="urgent", date=q.between(prev_start, start_date))) - urgent
  return unassigned, unresolved, urgent, -d_unassigned, -d_unresolved, -d_urgent




# labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

# datasets = [{
#             'label': 'Resolved',
#             'backgroundColor': '#9389DF',
#             'borderColor': '#7D71D8',
#             'data': [8, 10, 5, 2, 9, 11, 6]
#         },{
#             'label': 'Unresolved',
#             'backgroundColor': '#00FFAF',
#             'borderColor': '#00FFAF',
#             'data': [4, 3, 11, 12, 5, 6, 6]
#         }]


# @anvil.server.callable
# def get_plots(start, end):
#   resolved_tickets, new_tickets = get_ticket_data(start, end)
#   dates = []
#   res = []
#   unres = []
#   for i in range((start-end), 1):
#     day = (datetime.today().date() + timedelta(days=i))
#     dates.append(day.strftime('%A, %d'))
#     r = len([x for x in resolved_tickets if x['closed'].date() == day])
#     res.append(r)
#     u = len([x for x in new_tickets if not x['closed'] and x['date'].date() == day])
#     unres.append(u)
#   resolved = go.Bar(name="Resolved tickets", y=res, x=dates)
#   unresolved = go.Bar(name="Unresolved tickets", y=unres, x=dates)
#   return [resolved, unresolved]





def get_ticket_data(start, end):
  resolved_tickets = app_tables.tickets.search(
    closed=q.between(start, end)
  )
  new_tickets = app_tables.tickets.search(
    date=q.between(start, end)
  )
  return resolved_tickets, new_tickets

@anvil.server.callable
def get_stats(days):
  start_date = datetime.today() - timedelta(days=days)
  resolved_tickets, new_tickets = get_ticket_data(days)
  unresolved = (len(new_tickets) - len(resolved_tickets)) if len(new_tickets) > len(resolved_tickets) else 0
  urgent = len(app_tables.tickets.search(
    priority='urgent',
    date=q.between(start_date, datetime.today(),
    )
  ))
  received = len(new_tickets)
  
  resolved = len(resolved_tickets)
  return received, resolved, unresolved, urgent


  

@anvil.server.callable
def get_plots(days):
  resolved_tickets, new_tickets = get_ticket_data(days)
  dates = []
  res = []
  unres = []
  for i in range(-days+1, 1):
    day = (datetime.today().date() + timedelta(days=i))
    dates.append(day)
    r = len([x for x in resolved_tickets if x['closed'].date() == day])
    res.append(r)
    u = len([x for x in new_tickets if not x['closed'] and x['date'].date() == day])
    unres.append(u)
  resolved = go.Bar(name="Resolved tickets", y=res, x=dates)
  unresolved = go.Bar(name="Unresolved tickets", y=unres, x=dates)
  return [resolved, unresolved]

