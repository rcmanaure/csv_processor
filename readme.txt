To run and build the container and collectstatic:

    docker-compose -f docker-compose.prod.yml up -d --build
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
    docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear


To Create a app in django:
    docker-compose up -d --build
    docker-compose exec web python manage.py startapp upload

To bring the containers down:
    docker-compose down -v
    docker-compose -f docker-compose.prod.yml down -v

To test prod:
    docker-compose -f docker-compose.prod.yml down -v
    docker-compose -f docker-compose.prod.yml up -d --build
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

In terms of actual deployment to a production environment, you'll probably want to use a:

    1-Fully managed database service -- like RDS or Cloud SQL -- rather than managing your own Postgres instance within a container.
    2-Non-root user for the db and nginx services


Django web application with Postgres for development.
 We also created a production-ready Docker Compose file that adds Gunicorn and Nginx into the mix to handle static and media files. You can now test out a production setup locally.