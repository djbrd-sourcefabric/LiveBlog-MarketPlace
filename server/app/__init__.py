from eve import Eve
from app.oauth2 import BearerAuth
from flask import make_response
from flask.ext.sentinel import ResourceOwnerPasswordCredentials, oauth
import json

# delete a marketer's blogs when marketer is deleted
def on_delete_item_marketers(item):
    blogs_collection = app.data.driver.db['blogs']
    blogs_collection.delete_many({'marketer._id': item['_id']})

def on_delete_resource_marketers():
    blogs_collection = app.data.driver.db['blogs']
    blogs_collection.remove()

app = Eve(auth=BearerAuth)
ResourceOwnerPasswordCredentials(app)
app.on_delete_item_marketers += on_delete_item_marketers

@app.route("/api/languages", methods=['GET'])
def get_languages():
    blogs_collection = app.data.driver.db['blogs']
    languages = blogs_collection.distinct('language')
    return make_response(json.dumps(languages))

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Development Server Help')
    parser.add_argument("-d", "--debug", action="store_true", dest="debug_mode",
                        help="run in debug mode (for use with PyCharm)", default=False)
    parser.add_argument("-p", "--port", dest="port",
                        help="port of server (default:%(default)s)", type=int, default=5000)

    cmd_args = parser.parse_args()
    app_options = {"port": cmd_args.port}

    if cmd_args.debug_mode:
        app_options["debug"] = True
        app_options["use_debugger"] = False
        app_options["use_reloader"] = False