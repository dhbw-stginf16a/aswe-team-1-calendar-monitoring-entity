# Concern Definition (Calendar)

**Concern-Tag :** `calendar`

This is all about calendar events.

## General Parameters

* **events** (array) Array of event items
* **event** (dictionary) A specific event
    - name
    - begin
    - end
    - description
    - location
    - categories

## Request Types

### Events for a given date

**Type-Tag:** `event_date`

#### Request

- **date** (ISO 8601 Timestring): Date to get all events for
- **user**: (string): Internal user id to get associated calendars

#### Response

- **events**: Array as listed in general parameters

#### Example

Request

```json
{
    'type': 'event_date',
    'payload': {
        'user': 'AntonHynkel',
        'date': '2007-11-01'
    }
}
```

Response

```json
[
    {
        'payload': {
            'events': [
                {
                    'begin': '2007-05-25T14: 00: 00+00: 00',
                    'categories': ['Speeches'],
                    'description': 'Expedition 15 Commander Fyodor Yurchikhin and Flight Engineer Oleg Kotov prepared this week for two spacewalks while Flight Engineer Suni Williams prepared for her return to Earth.',
                    'end': '2007-05-25T15: 00: 00+00: 00',
                    'location': None,
                    'name': 'International Space Station Status Report: SS07-28'
                }
            ]
        },
        'type': 'event_timerange'
    }
]
```


### Events for a given time range

**Type-Tag:** `event_timerange`

#### Request

- **startDate** (ISO 8601 Timestring): First day to get all events for
- **endDate** (ISO 8601 Timestring): Last day to get all events for
- **user**: (string): Internal user id to get associated calendars

#### Response

- **events**: Array as listed in general parameters

#### Example

Request

```json
{
    'type': 'event_timerange',
    'payload': {
       'user': 'AntonHynkel',
        'startDate': '2007-01-01',
        'endDate':  '2007-12-31'
    }
}
```

Response

```json
[
    {
        'payload': {
            'events': [
                {
                    'begin': '2007-05-25T14: 00: 00+00: 00',
                    'categories': ['Speeches'],
                    'description': 'Expedition 15 Commander Fyodor Yurchikhin and Flight Engineer Oleg Kotov prepared this week for two spacewalks while Flight Engineer Suni Williams prepared for her return to Earth.',
                    'end': '2007-05-25T15: 00: 00+00: 00',
                    'location': None,
                    'name': 'International Space Station Status Report: SS07-28'
                }
            ]
        },
        'type': 'event_timerange'
    }
]
```


## Subscription Types

### [Type Name]

**Type-Tag:** `[Type Tag]`

#### Message

- **[Parameter1 Name]** ([Parameter1 Type]): [Description]
  - _[Possible Value]_: [Value Description]
- **[Parameter2 Name]**: ([Parameter2 Type]): [Description]

#### Example

```json
[Example for message]
```
