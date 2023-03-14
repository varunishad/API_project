import csv
import os
import traceback
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .csv_parser import ParseCSV
from .fetch_data import Fetcher


@api_view(['POST'])
def read_csv(request):
    try:
        #To check whether the file is uploaded or not
        if len(request.FILES):
            for file in request.FILES:
                myfile = request.FILES[file]
                parser = ParseCSV(myfile)
                serializer = parser.insert_into_db()

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Error: Please mention a key and upload a CSV file as value")

    except:
         return Response(traceback.format_exc())


@api_view(['POST'])
def fetch_data(request):
    try:
        req = request.data
        tables = Fetcher(req)
        serializer = tables.fetch_data()
        return Response(serializer)

    except:
        return Response(traceback.format_exc())


#Also there are some other ways in which these APIs can be written.
