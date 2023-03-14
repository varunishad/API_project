
import pandas as pd
from .serializers import CSVSerializer

class ParseCSV:
    def __init__(self, myfile):
        self.myfile = myfile
        self.df = self.read_file()

    def read_file(self):
        return pd.read_csv(self.myfile)

    def insert_into_db(self):
        csv_data = self.df.to_dict('records')
        return CSVSerializer(data=csv_data, many=True)

#Could have also be done using DictReader instead of pandas
