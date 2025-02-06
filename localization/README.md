# Localization
Project for Atlas School

<br/>

## Description
To get started with internationalization (i18n) of backend strings using Babel, a Python tool, follow this tutorial. Babel helps localize Python applications by extracting and translating strings.

Prerequisites: * Python installed (version 3.6+ recommended) * Basic knowledge of Python

<br/>

## Tasks

<br/>


## 0. Setup i18n with Babel
Install Babel using pip:
```pip install Babel```
For a web framework like Flask, you can also install Flask-Babel
```pip install Flask-Babel```

<br/>


## 1. Mark Strings for Translation
You need to mark the strings in your Python code that need translation.

You can do this using the _() function provided by Babel. For example:
```
from babel import Babel, _

greeting = _("Hello, World!")
```
This will signal Babel that ```Hello, World!``` needs translation.

You can also use ngettext() for singular and plural forms:
```
message = ngettext("You have one message", "You have %(num)d messages", num)
```

<br/>


## 2. Create Babel Configuration File
Next, create a file named ```babel.cfg``` in your project directory. This file tells Babel where to find the strings that need translation. (This tells Babel to look for Python files in your project for translation strings.)
```

[python: **.py]
```

<br/>


## 3. Extract Strings for Translation
Once you’ve marked the strings, run the Babel command to extract the strings.

Use the following command to extract strings from the marked files:
```
pybabel extract -F babel.cfg -o messages.pot .
```
Notes: -F babel.cfg: Specifies the configuration file. -o messages.pot: Creates a messages.pot file containing the strings. .: Refers to the directory containing your project files. This creates a .pot file that contains all the strings marked for translation.

<br/>


## 4. Initialize Translations
You can now initialize translations for a specific language. For example, to create translations for French (fr):
```
pybabel init -i messages.pot -d translations -l fr
```
This creates a directory called translations with a French translation file in it (translations/fr/LC_MESSAGES/messages.po).

<br/>


## 5. Translate Strings
Open the generated .po file (e.g., translations/fr/LC_MESSAGES/messages.po) and add translations for each string:
```

msgid "Hello, World!"
msgstr "Bonjour, le monde!"
```

<br/>


## 6. Compile Translations
After translating the strings, compile them using:
```
pybabel compile -d translations

```
This creates compiled .mo files (e.g., translations/fr/LC_MESSAGES/messages.mo) that Babel uses at runtime.

<br/>


## 7. Using Translations in Code
To use translations, you’ll need to set the locale in your code. Here’s an example using Flask:
```
from flask import Flask, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Configure available languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

@babel.localeselector
def get_locale():
    # Use request headers or a user-specific preference to determine locale
    return request.accept_languages.best_match(['en', 'fr'])

@app.route('/')
def index():
    # This will display the string in the appropriate language
    return _("Hello, World!")

if __name__ == "__main__":
    app.run()
```

<br/>


## 8. Testing i18n
Run your application and set the Accept-Language header to fr in your browser or API client such as Postman. You should now see “Bonjour, le monde!” instead of “Hello, World!”
