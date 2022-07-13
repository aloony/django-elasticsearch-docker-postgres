# use mannually via "docker exec -it <container id> "/bin/bash"
# and then "python _generate_fixtures.py && python manage.py loaddata ./fixtures/data.json" 

import random, string, json
from faker import Faker

faker = Faker()

with open('fixtures/data.json', 'w') as file:
    data = []
    for i in range(1000):
        data.append({
            'model': 'mainapp.Movie',
            'fields': {
                'imdb_title_id': i,
                'title': faker.name(),
                'description': faker.text(),
                'director': faker.name()
            }
        })
    file.write(json.dumps(data))