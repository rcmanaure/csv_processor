import logging
import os

import pandas as pd
import shortuuid

from utils.fake_dataframe import make_music


FOLDER_LOCATION = os.path.join(os.path.dirname(__file__), "fake_csv/")
FOLDER_LOCATION_CSV = os.path.join(os.path.dirname(__file__), "csv_processed/")

# Here we generate fake data.
# If you want more or less data just change the value num.
# fake_data = pd.DataFrame(make_music(num=2000))
# fake_data.to_csv(FOLDER_LOCATION + "fake_data.csv")


def csv_processer(file, file_id, array: str = None):
    """
    Function which takes a CSV file of the following format as its input,
    processes it and generates the output CSV file. Using pandas library.
    """

    # Assign an unique identifier to each clean data file.
    file_name = file_id

    # We read the csv file to be processed
    # data = pd.read_csv(FOLDER_LOCATION + "fake_data.csv", chunksize=100000)
    data = pd.read_csv(file, chunksize=100000)
    columns = ["Song Name", "Date", "Number of Plays"]

    try:
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
            # In case the file is too large and can be cleaned or filtered more deeply.
            # dfr["chunk_id"] = shortuuid.uuid()

            # Here we save the cleaned csv file with unique filename.
            dfr.to_csv(
                FOLDER_LOCATION_CSV + f"{file_name}.csv", mode="a", header=header
            )

        if array is None:
            # to check the memory usage.
            print(dfr.memory_usage(index=False, deep=True) / df.shape[0])
            # To see the folder localtion and file name
            print(f"Clean data saved: {FOLDER_LOCATION_CSV}{file_name}.csv")

    except:
        logging.error(
            f"Error processing the csv file. Check if the columns are {columns}"
        )
