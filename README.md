# blabber-jabber
A sample Realtime Chat application

### What is implemented
- [x] User join or create a chat room by entering a name.
- [x] User see the list of users in the chat room
- [x] User can read the last 10 messages.
- [x] Users can read new messages.
- [x] User can write and send new messages.

### Other features

- [x] User can signup.
- [x] User can login.
- [ ] A hosted version of your app
- [ ] Admin of a chat room (first user) can kick other users

### Extra features
- [x] See who is typing in a chat room.
- [x] Get notifications when a message is posted on a specific chat room

---
# How to run 

A version of the project is deployed under https://blabber.playground.codeplumbers.eu, but it is a WIP. I've had issues with deploying the websocket service behind a reverse proxy (nginx) and traefik :/. I didn't have the time to fix this.

There are two .env files that need to be created:
- <root>/.env (see .env.sample)
  ```
    SECRET_KEY=django-fake*-secret-key
    DEBUG=True

    # Database connection
    DB_HOST=blabber-db
    DB_NAME=blabber-app
    DB_USER=postgres
    DB_PASS=postgres
    POSTGRES_VERSION=latest
    DJANGO_DOCKER_PORT=8080
    POSTGRES_DOCKER_PORT=5432
    FRONTEND_DOCKER_PORT=80
    PGADMIN_MAIL=admin@dev.dev
    PGADMIN_PW=admin
    PGADMIN_PORT=5050
    REDIS_HOST=blabber-cache
    REDIS_PORT=6379
    REDIS_PASSWORD=changeme
    CACHE_TTL=30
  ``` 
- <root>/frontend/.env (see frontend/.env.sample)
  ```
   VUE_APP_API_BASE_URL='http://localhost:8080/api/v1/'
   VUE_APP_WEBSOCKET_URL='ws://localhost:8008/ws'
  ```
Once that is done, you can run the development environment locally, from the main branch, using:

```
docker-compose -f docker-compose-dev.yml up -d
```

or (branch: deploy, WIP):

```
docker-compose -f docker-compose-prod.yml up -d
```

---

# Architecture
## Docker
The project is built using docker and docker compose. it has the following services: 
* **blabber-app**: a django application that exposes a REST Api and handles websocket connections
* **blabber-frontend**: the UI built with vue js
* **blabber-db**: a PostgreSQL server
* **blabber-pgadmin**: a pgadmin instance (dev)
* **blabber-portainer**: portainer dashboard to manage docker containers
* **blabber-cache**: a redis server
* **blabber-cache-ui**: a redis ui helper (dev)

## Frontend:
The UI is built using 
* Vue3
* Typescript
* Bulma CSS
* Vue Router
* Vuex (with vuex-helper-decorators)

In order to easily prototype vue components, I've user Storybook. You can launch it with: 
```yarn storybook```

## Backend
Used: 
* Django
* Djang Rest Framework
* Redis
* Django channels for the realtime chat (websockets)
* PostgreSQL

I've added a management command in order to seed the db, to run it: 

`
docker exec -it blabber-it python manage.py db_seed --users 3 
`

The `users` argument is the number of users that will be created. e.g. --users 3 will create: 

```
User 1: username=user1, password=password
User 2: username=user2, password=password
User 3: username=user3, password=password
```