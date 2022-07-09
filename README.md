#### 1 - Clone repo

```
git clone https://github.com/aloony/django-elasticsearch-docker-postgres
```

#### 2 - Start docker

```
docker-compose up --build
```

### 3 - Generate fixtures for database

```
docker exec -it <container_id> "/bin/bash"
```

```
python _generate_fixtures.py && python manage.py loaddata ./fixtures/data.json
```

### 4 - Play around with API

    Documentation is located at /
