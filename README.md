# Test Deploy fast and easy a Django app to RailwayApp

## How to use

1. Create a new project on RailwayApp

2. Link the project to your Github account

3. Let him autodetect and deploy your app
    - settings > network > generate domain
    - Launch command `gunicorn --bind 0.0.0.0:8000 mon_site.wsgi:application`
    
## Development

### Version

python >= 3.10

### Environment

```bash	
python -m venv venv

# Linux or MacOS
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

### Run

```bash
python manage.py runserver
```
