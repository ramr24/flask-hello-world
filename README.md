# Flask Hello World

Visit `/` to receive an inspiring greeting of world peace, or `/hello/YOURNAME/` or `/hola/YOURNAME` to receive a greeting in English or Spanish.

## To Run

All commands to be run from inside the repository directory.
```
$ pip install -r requirements.txt
$ python main.py
```

## To Publish to Heroku

All commands to be run from inside the repository directory.
```
$ git init                # Only necessary if this is not already a git repository
$ heroku create
$ git push heroku master  # Be sure to commit any changes before you push
$ heroku open
```
