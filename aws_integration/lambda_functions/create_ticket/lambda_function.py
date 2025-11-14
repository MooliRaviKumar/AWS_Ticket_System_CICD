import awsgi
from support_app.wsgi import application  # or your main app’s wsgi

def handler(event, context):
    return awsgi.response(application, event, context)
