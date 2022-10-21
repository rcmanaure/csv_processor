import os
import uuid

import pandas as pd
import shortuuid

from utils.fake_dataframe import make_music

FOLDER_LOCATION = os.path.join(os.path.dirname(__file__), "mediafiles/")
FOLDER_LOCATION_CSV = os.path.join(os.path.dirname(__file__), "csv/")

# Here we generate fake data.
# If you want more or less data just change the value num.
fake_data = pd.DataFrame(make_music(num=50))
fake_data.to_csv(FOLDER_LOCATION + "fake_data.csv")


def csv_processer(array: str = None):
    """
    Function which takes a CSV file of the following format as its input,
    processes it and generates the output CSV file. Using pandas library.
    """
    # Assign an unique identifier to each clean data file.
    file_name = shortuuid.uuid()

    # We read the csv file to be processed
    data = pd.read_csv(FOLDER_LOCATION + "fake_data.csv", chunksize=100)

    columns = ["Song Name", "Date", "Number of Plays"]
    header = True
    for num, chunk in enumerate(data):
        # Here we process the data to be saved.
        if num > 0:
            header = False
        df = chunk[columns]
        # Process the csv file.
        dfx = df.groupby(["Song Name", "Date"]).sum().reset_index()
        # rename the columnn to be saved in the new file.
        dfr = dfx.rename(
            columns={"Number of Plays": "Total Number of Plays for Date"},
            errors="raise",
        )

        # If you want create id for block of chunk.
        # myuuid = uuid.uuid4()
        # dfr["chunk_id"] = myuuid

        # Here we save the cleaned csv file with unique filename.
        dfr.to_csv(
            FOLDER_LOCATION_CSV + f"{file_name}.csv",
            mode="a",
            header=header,
            sep="\t",
        )
    if array is None:
        print(f"Clean data saved: {FOLDER_LOCATION_CSV}")


# Run the python file to process the csv file generated with fake data.
csv_processer()


# Manera de optimizar:
# - usar spark
# - que el formato sea parquet y no csv
# - particionar la data en archivos por fecha de extraccion
