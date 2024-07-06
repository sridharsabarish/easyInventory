from googleapiclient.discovery import build
from google.oauth2 import service_account

# Set up credentials
credentials = service_account.Credentials.from_service_account_file('path/to/credentials.json')
scopes = ['https://www.googleapis.com/auth/calendar']
credentials = credentials.with_scopes(scopes)

# Build the service
service = build('calendar', 'v3', credentials=credentials)

# Create an event
event = {
    'summary': 'Sample Event',
    'start': {
        'date': '2022-01-01',
        'timeZone': 'America/New_York',
    },
    'end': {
        'date': '2022-01-02',
        'timeZone': 'America/New_York',
    },
}

# Insert the event
calendar_id = 'primary'  # Use 'primary' for the primary calendar
event = service.events().insert(calendarId=calendar_id, body=event).execute()

print('Event created: %s' % (event.get('htmlLink')))