# ApiONG


#### How to ejecute the application with docker?

1. Open terminal.
2. Situate in project path.
3. Build docker with the command:
`$: docker-compose build`
4. Up docker with the command:
`$: docker-compose up`

#### How to ejecute the application without docker (Linux)?

1. Open terminal.
2. Situate in project path.
3. Ejecute:
`$:pip install -r requirements.txt`
4. Run django in apimusic:
`$:python -u manage.py runserver 0.0.0.0:8000`


#### APIS:
- Given an provides of country for each year with your contribution.

http://localhost:8000/get_activities/?country={country code}&year={year}