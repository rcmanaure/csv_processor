# Dockerizing Django

## To run and build the container and collectstatic:

    docker-compose up -d --build

## To bring the containers down:
    docker-compose down -v

## To create superuser
docker exec -it <container_id> python manage.py createsuperuser

# module/function which takes a CSV file of the following format as its input,
# processes it and generates the output CSV file.

## To run the function csv processor:
Run the "csv_processor.py" file to generate a fake data to be processed and saved in the folder
csv. The data processed is saved in the csv folder.

The fake data can be updated to generata more data. If you want more or less data just change the value num,
in the "csv_processor.py" file line 14.