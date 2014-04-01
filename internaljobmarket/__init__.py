"""
Initialize Flask app

"""
from flask import Flask
import os
#from flask_debugtoolbar import DebugToolbarExtension
#from werkzeug.debug import DebuggedApplication

app = Flask('application')

if os.getenv('FLASK_CONF') == 'DEV':
#development settings n
    app.config.from_object('application.settings.Development')
# Flask-DebugToolbar (only enabled when DEBUG=True)
    toolbar = DebugToolbarExtension(app)
    
    # Google app engine mini profiler
    # https://github.com/kamens/gae_mini_profiler
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

elif os.getenv('FLASK_CONF') == 'TEST':
    app.config.from_object('application.settings.Testing')

else:
    app.config.from_object('application.settings.Production')

# Enable jinja2 loop controls extension
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# Pull in URL dispatch routes
import urls