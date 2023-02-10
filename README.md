# Detect Waste

Proof of concept for uploading images via an API, processing them in the background, and then checking for the response by another API call.

[Detect Waste](https://detectwaste.netlify.app/) was a part of the Sustainability Hackathon organized by [N3XTCODER](https://n3xtcoder.org/).

## How to run this prototype

### 1. Download the code

Download the code from Github.

### 2. Create and activate a Python virtual environment

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

### 3. Install pip requirements

```bash
(venv)$ pip install -r requirements/dev.txt
```

### 4. Create the secrets.json file

Copy `sample_secrets.json` to `secrets.json`. Modify the settings there as necessary if you change the database from SQLite to MySQL or PostgreSQL.

### 5. Run migrations

Create the database by running the `migrate` management command:

```bash
(venv)$ python manage.py migrate
```

### 6. Create super user

Create the superuser, such as "admin":

```bash
(venv)$ python manage.py createsuperuser
```

### 7. Run local webserver

```bash
(venv)$ python manage.py runserver
```

### 8. Create some categories for classification

Go to `http://127.0.0.1:8000/en/admin/image_processing/category/` and add some categories for waste, such as "Glass bottles", "Metal cans", "Paper", etc.

### 9. Try uploading an images

- Go to `http://127.0.0.1:8000/en/`.
- Login with your superuser credentials.
- Upload an image.
- Go to `http://127.0.0.1:8000/en/admin/image_processing/processedimage/` to classify the image. Later this will happen automatically in the background by machine learning algorithm.
- Switch back to `http://127.0.0.1:8000/en/` and retrieve the classified results.

## Further development

- Add a background task (Celery or Huey) that automatically calls image classification and saves the result in the database.
- Try different authentication options if the upload happens from a drone or another device.
- Create a user-friendly frontend or mobile app for uploading images from a mobile phone by authenticated users.
