X_DOMAINS = '*'
X_MAX_AGE = 24 * 3600
X_HEADERS = ['Content-Type', 'Authorization', 'If-Match']

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'marketplace'

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

URL_PREFIX = 'api'

marketers = {
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'public_methods': ['GET'],
    'public_item_methods': ['GET'],
    'schema': {
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 64,
            'required': True,
            'unique': True
        },
        'url': {
            'type': 'string',
            'required': True
        },
        'email': {
            'type': 'string',
            'required': True
        },
        'phone': {
            'type': 'string'
        }
    }
}

DOMAIN = {
    'marketers': marketers
}