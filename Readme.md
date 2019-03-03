# ApiONG


#### How to ejecute the application with docker?

1. Open terminal.
2. Situate in project path.
3. Build docker with the command:
`$: docker-compose build`
4. Up docker with the command:
`$: docker-compose up`

#### How to ejecute tests?

1. Open terminal.
2. Entry in docker. `$: docker exec -ti apimrnoow_django_1 /bin/bash`
3. Situate in project root of django: `$ cd /code/ApiONG`
4. Ejecute command: `$: python manage.py test` 



#### APIS:
- Given an provides of country for each year with your contribution.

http://localhost:8000/get_activities/?country={country code}&year={year}
