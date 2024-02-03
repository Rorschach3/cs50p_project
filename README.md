---
runme:
  id: 01HNN1Q2SSPFD3ESFEN05R3Z1W
  version: v2.2
---

Accessing Supabase dashboard#
You can access the Supabase Dashboard through the API gateway on port 8000. For example: http://:8000, or localhost:8000 if you are running Docker locally.

You will be prompted for a username and password. By default, the credentials are:

    Username: supabase
    Password: this_password_is_insecure_and_should_be_updated
You should change these credentials as soon as possible using the instructions below.

##### change directory to project folder, and create a virtual environment

`cd project`
`python3 -m venv venv`
`source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`

##### install program requiremnts.txt

`pip install -r requirements.txt`

##### Get the code
    `git clone --depth 1 https://github.com/supabase/supabase`

##### Go to the docker folder
    `cd supabase/docker`

##### Copy the fake env vars
    `cp .env.example .env`

##### Pull the latest images
    `docker compose pull`

##### Start the services (in detached mode)
    `docker compose up -d`

Whenever restarting the service or continuing the development, you can start the services with the following command:

##### pull the latest images
    `docker-compose pull`

##### start the services
    `docker-compose up -d`