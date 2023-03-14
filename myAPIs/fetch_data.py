
from .models import CSVData

class Fetcher:
    def __init__(self, req):
        self.dic = req

    def fetch_data(self):
        if not self.dic:
            dataset = CSVData.objects.all().values()[:50]
        else:
            headers = []
            for key, val in self.dic.items():
                if val == 'desc':
                    key = "-" + key
                elif val != 'asc':
                    raise Exception("Please mention order as 'asc' or 'desc'")
                headers.append(key)

            dataset =  CSVData.objects.all().order_by(key).values()[:50]
            # dataset =  CSVData.objects.all().order_by(col for col in headers).values()[:50]

        fetched_data = [row for row in dataset]
        return fetched_data

