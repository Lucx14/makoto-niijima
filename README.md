### Makoto Niijima

# To run using docker

```
$ git clone https://github.com/Lucx14/makoto-niijima.git
$ cd makoto-niijima
$ touch .env.development
$ python3 -m venv venv
$ source venv/bin/activate
```

# populate .env.development with these keys

```
DEBUG=1
SECRET_KEY=dev
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=makoto_niijima_dev
SQL_USER=makoto_niijima
SQL_PASSWORD=makoto_niijima
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

# Build the images

```
$ docker compose up -d --build
```

# Run migrations

```
$ docker compose exec web python manage.py flush --no-input
$ docker compose exec web python manage.py migrate
```

View running app at localhost:8000

# Access db

```
$ docker compose exec db psql --username=makoto_niijima --dbname=makoto_niijima_dev
hello_django_dev=# \l
hello_django_dev=# \c makoto_niijima_dev
hello_django_dev=# \dt
hello_django_dev=# \q
```

# Check volume was created

```
$ docker volume inspect makoto-niijima_postgres_data
```

# Stop containers

```
$ docker compose down
$ docker compose down -v
$ docker container stop <container>
$ docker container prune
$ docker image prune
$ docker image rm <id>
$ docker system prune -af --volumes
```

# Connect a database GUI (example Tableplus)

- In the docker compose yml make sure you have mapped the ports for the db

```
ports:
      - "2345:5432"
```

- test the connection in table plus

```
Name: <name the database connection>
Host/Socket: 127.0.0.1
Port: 2345
User: makoto_niijima
Password: makoto_niijima
Database: makoto_niijima_dev
```

# Set some helpful alias commands

```
alias ds='docker compose'
alias ds_console='docker exec -it makoto-niijima_web_1 python manage.py shell'
alias ds_terminal='docker exec -it makoto-niijima_web_1 /bin/sh'
alias ds_logs='docker-compose logs -f --tail 20 makoto-niijima_web_1'
alias ds_test='docker exec -it makoto-niijima_web_1 python manage.py test'
```

# Access the docker container shell while running

```
$ docker exec -it makoto-niijima_web_1 /bin/sh
$ ds_terminal
$ exit
```

# Access the django python console

```
$ docker exec -it makoto-niijima_web_1 python manage.py shell
$ ds_console
$ exit()
```
