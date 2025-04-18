
# TimePlanner API

TimePlanner API is a **FastAPI**-based application designed to help users organize their tasks based on available time. It helps create an efficient schedule by considering the time available and the priority of each task.

## Features

- Automatically organizes tasks based on available time and priority.
- Generates an optimized schedule considering task durations.
- Automatic API documentation via **Swagger UI**.

## How to Use

### 1. Clone the project
```bash
git clone https://github.com/ThiagoRosa21/TimePlanner-API.git
cd TimePlanner-API
```

### 2. Install dependencies
The project uses **FastAPI**, **Uvicorn**, and **python-dotenv** for environment configuration. To install the dependencies, run:
```bash
pip install -r requirements.txt
```

### 3. Run the application using Uvicorn
To run the application, use the following command to start the **Uvicorn** server:
```bash
python -m uvicorn app.main:App --reload
```
- `--reload`: This flag enables automatic reloading of the server during development whenever code changes.

### 4. Access the automatic documentation (Swagger)
Once the application is running, you can access the API documentation at:
[http://localhost:8000/docs](http://localhost:8000/docs)

## API Endpoints

### `POST /organize`
This endpoint receives a list of tasks with their durations and priorities, along with the available time, and returns an optimized schedule.

#### Request Example:
```json
{
  "available_time": 240,
  "tasks": [
    {"description": "Study", "duration": 60, "priority": 5},
    {"description": "Exercise", "duration": 90, "priority": 4},
    {"description": "Lunch", "duration": 60, "priority": 1},
    {"description": "Emails", "duration": 30, "priority": 3}
  ]
}
```

#### Response Example:
```json
{
  "schedule": [
    "1. Study (60 min)",
    "2. Exercise (90 min)",
    "3. Emails (30 min)",
    "4. Lunch (60 min)"
  ],
  "total_time_used": 240,
  "remaining_time": 0
}
```

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- python-dotenv

## Running Tests
To run the tests, use the following command:
```bash
pytest
```

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

