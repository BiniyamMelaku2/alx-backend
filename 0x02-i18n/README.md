# 0x02. i18n

## Resources
Read or watch:

* [Flask-Babel](https://flask-babel.tkte.ch/)
* [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
* [pytz](http://pytz.sourceforge.net/)

# Tasks

## [0. Basic Flask app](./0-app.py), [0-index.html](templates/0-index.html)
First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).
> python3 -m 0-app


## [1. Basic Babel setup](./1-app.py), [1-index.html](templates/1-index.html)
Install the Babel Flask extension:

`$ pip3 install flask_babel`
Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.
