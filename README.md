## run application
```
python manage.py runserver

 * [database] : [postgresql://postgres:HODL!fe@localhost:5432/hod] 
 * Serving Flask app "config" (lazy loading)
 * Environment: testing
 * Debug mode: on
 * Running on http://localhost:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * [database] : [postgresql://postgres:HODL!fe@localhost:5432/hod] 
 * Debugger is active!
 * Debugger PIN: 252-735-706

```
default port is **8080**


## secret settings
```
{
    "SECRET_KEY":"",
    "ENVIRONMENT": "TESTING",
    "SERVER_HOST": "localhost",
    "SERVER_PORT": 8080,    
    "DATABASE_ENGINE":"postgresql",
    "DB_USERNAME":"",
    "DB_PASSWORD":"",
    "DB_HOST":"localhost",
    "DB_PORT":"5432",
    "DB_NAME":"hod"
}
```