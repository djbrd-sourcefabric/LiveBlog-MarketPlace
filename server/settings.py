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

blogs = {
    'schema': {
        'marketer': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'marketers',
                'field': '_id',
                'embeddable': True
            }
        },
        'marketer_blog_id': {
            'type': 'string',
            'required': True
        },
        'title': {
            'type': 'string',
            'required': True
        },
        'description':  {
            'type': 'string',
            'required': True
        },
        'picture_url': {
            'type': 'string'
        },
        'public_url': {
            'type': 'string',
            'required': True
        }
    }
}

DOMAIN = {
    'marketers': marketers
}