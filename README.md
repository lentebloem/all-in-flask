[![Build Status](https://travis-ci.org/TwilioDevEd/automated-survey-flask.svg?branch=master)](https://travis-ci.org/TwilioDevEd/automated-survey-flask)

# Quickstart

This application is built for the Attendy Project for IEOR 171: Technology Firm Leadership and Organizational Behavior at *University of California, Berkeley*.

## Setting Up The Environment

Since our project is currently under development, we don't have an online version ready. However, you can test it locally by following the intructions below.

### Clone the repository

In bash, run:
```bash
git clone https://github.com/lentebloem/all-in-flask.git
cd all-in-flask
```


### Create a new virtual environment

- If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

    ```
    virtualenv venv
    source venv/bin/activate
    ```

- If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

    ```
    mkvirtualenv automated-survey
    ```

### Install the requirements.

```
pip install -r requirements.txt
```


1. Copy the `.env.example` file to `.env`, and edit it to match your database.

1. Run `source .env` to apply the environment variables (or even better, use [autoenv](https://github.com/kennethreitz/autoenv))

1. Run the migrations.

  ```
  python manage.py db upgrade
  ```

1. Seed the database.

 ```
 python manage.py dbseed
 ```

 Seeding will load `survey.json` into SQLite.

1. Expose your appliction to the wider internet using ngrok.

  To actually forward incoming calls, your development server will need to be publicly accessible.
  [We recommend using ngrok to solve this problem](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html).


   ```bash
   $ ngrok http 5000
   ```

 Once you have started ngrok, update your TwiML app's voice URL setting to use your ngrok hostname.
It will look something like this:

```
http://88b37ada.ngrok.io/support/call
```

### Start the development server

```
python manage.py runserver
```

Once ngrok is running, open up your browser and go to your ngrok URL. It will
look like this: `http://88b37ada.ngrok.io`
## License

MIT
