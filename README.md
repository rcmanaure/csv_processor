# Dockerizing Django

## To run and build the container and collectstatic:

    docker-compose up -d --build

## To bring the containers down:
    docker-compose down -v

## To create superuser
docker exec -it <container_id> python manage.py createsuperuser

# module/function which takes a CSV file of the following format as its input, processes it and generates the output CSV file.

## To run the function csv processor:
##### The "csv_processor.py" file use pandas to process the csv file. In some case is better usar spark o dask to improve the performance because dask (https://www.dask.org/get-started) provides advanced parallelism.

Run the "csv_processor.py" file to generate a fake data to be processed and saved in the folder
csv. The data processed is saved in the csv folder. 

The fake data can be updated to generata more data. If you want more or less data just change the value num,
in the "app/csv_processor.py" file line 14.
#### The files can be run directly from the terminal follow this steps:
* Create and run a virtual enviroment to install the dependencies.
* Install the requirements.py file with the command: pip install -r requirements.txt
* Go to the folder app and run the files as described above with the command:python name_file.py

## To run the complexity calculator:
Run the "app/complexity_calculator.py" file.