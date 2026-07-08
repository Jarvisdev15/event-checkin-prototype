# QR-Based Event Check-in API

This is a lightweight prototype for faster attendance tracking at student events.

## Purpose

Manual attendance lists can slow down registration, create duplicate entries, and make it difficult to track live participant count during an event.

This prototype solves that by allowing a student ID to be submitted through a simple check-in API.

## Features

- Accepts student ID input
- Rejects missing student IDs
- Prevents duplicate check-ins
- Stores a timestamp for successful check-ins
- Returns clear HTTP status responses

## Tech Used

- Python
- Flask

## How to Run Locally

Install Flask:

```bash
pip install flask
```

Run the app:

```bash
flask --app event_checkin_prototype run
```

## API Endpoint

```http
POST /check-in
```

Example JSON body:

```json
{
  "student_id": "2025001"
}
```

## What the Code Demonstrates

- Input validation
- Duplicate prevention
- Timestamped records
- Clear API responses
- Simple backend logic using Flask

## Future Improvements

For a real deployment, this can be improved by adding:

- Staff login/authentication
- Database storage instead of temporary memory
- Dashboard for live attendance count
- Encrypted storage
- Clear student data retention rules
