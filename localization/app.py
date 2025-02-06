from flask import Flask, render_template, request
from flask_babel import Babel, _

# Create a Flask app
app = Flask(__name__)

# Initialize Flask-Babel
babel = Babel(app)

# Set up app config
app.config['BABEL_DEFAULT_LOCALE'] = 'en' # Default Language (English)
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations' # Supported Languages (English, French)

# Set Flask-Babel to use best locale for the user
def get_locale():
    # Use request headers or a user-specific preference to determine locale
    return request.accept_languages.best_match(['en', 'fr', 'es'])

# Manually initialize locale selector with Babel
babel.init_app(app, locale_selector=get_locale)

# Define a route
@app.route('/')
def index():
    # Using _() to mark text for translation
    greeting = _("Hello, World!")
    return render_template('index.html', greeting=greeting)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
