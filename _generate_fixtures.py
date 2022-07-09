# use mannually via "docker exec -it <container id> "/bin/bash"
# and then "python _generate_fixtures.py && python manage.py loaddata ./fixtures/data.json" 

import random, string, json

with open('fixtures/data.json', 'w') as file:
    data = []
    for i in range(100):
        data.append({
            'model': 'mainapp.Movie',
            'fields': {
                'imdb_title_id': i,
                'title': ''.join(random.choice(string.ascii_letters) for _ in range(5)) + ' ' + ''
                            .join(random.choice(string.ascii_letters) for _ in range(3)) + ' ' + ''
                            .join(random.choice(string.ascii_letters) for _ in range(8)),
                'description': ''.join(random.choice(string.ascii_letters) for _ in range(15)) + ' ' + ''
                                .join(random.choice(string.ascii_letters) for _ in range(5)) + ' ' + ''
                                .join(random.choice(string.ascii_letters) for _ in range(10)),
                'director': ''.join(random.choice(string.ascii_letters) for _ in range(8))
            }
        })
    file.write(json.dumps(data))