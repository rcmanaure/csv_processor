import os
import uuid

import pandas as pd

from utils.fake_dataframe import make_music

FOLDER_LOCATION = os.path.join(os.path.dirname(__file__), "mediafiles/")
FOLDER_LOCATION_CSV = os.path.join(os.path.dirname(__file__), "csv/")


fake_data = pd.DataFrame(make_music(num=5))
fake_data.to_csv(FOLDER_LOCATION + "fake_data.csv")


data = pd.read_csv(FOLDER_LOCATION + "fake_data.csv", chunksize=100)

columns = ["Song Name", "Date", "Number of Plays"]
header = True
for num, chunk in enumerate(data):
    myuuid = uuid.uuid4()
    if num > 0:
        header = False
    df = chunk[columns]
    dfx = df.groupby(["Song Name", "Date"]).sum().reset_index()
    dfr = dfx.rename(
        columns={"Number of Plays": "Total Number of Plays for Date"},
        errors="raise",
    )
    dfr["chunk_id"] = myuuid
    # dfr.loc[].to_csv('existing.csv', mode='a', header=header)
    dfr.to_csv(FOLDER_LOCATION_CSV + "clean_data.csv", mode="a", header=header)
print("done")


# z = pd.read_csv('existing.csv')
# - usar spark
# - que el formato sea parquet y no csv
# - particionar la data en archivos por fecha de extraccion
