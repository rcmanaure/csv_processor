# Dockerizing Django

## To run and build the container and collectstatic:

    docker-compose up -d --build


## To upload the file to the function csv processor:

    Go to localhost:8000 and upload a file.

## To download the cleaned file:
    Go to localhost:8000/download/<upload_id> and download the file.
    
## To bring the containers down:
    docker-compose down -v

## To create superuser
docker exec -it <container_id> python manage.py createsuperuser

# module/function which takes a CSV file of the following format as its input, processes it and generates the output CSV file.

##### The "csv_processor.py" file use pandas to process the csv file. In some case is better usar spark o dask to improve the performance for example dask (https://www.dask.org/get-started) provides advanced parallelism.



#### To run the files directly from the terminal, follow this steps:
    * Create and run a virtual enviroment to install the dependencies.
    * Install the requirements.py file with the command: pip install -r requirements.txt
    * Rune python manage.py migrate
    * Run python manage.py runserver
    * Go to **127.0.0.1:8000** and upload a file.

## To run the complexity calculator:
    Run the "app/complexity_calculator.py" file.
    The fake data can be updated to generata more data. If you want more or less data just change the value num,
    in the "app/csv_processor.py" file line 14.