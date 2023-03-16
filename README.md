## Guide to run both APIs on Postman:

**API 1.** To parse a CSV that Inserts the rows into a table.
- Upload your csv on postman with these required fields: **name, age, birthdate, pan**
- In the response it return the fields that have been inserted in the database table.

![Postman Screenshot 1](https://github.com/varunishad/API_project/blob/main/api1_ss.png?raw=true)


**API 2.** Sorting data that returns a JSON.
- The format for the request should be a dictonary with key as header and value as order.
- In the response it return 50 entries (if exists) after sorting as per the request.

![Postman Screenshot 2](https://github.com/varunishad/API_project/blob/main/api2_ss.png?raw=true)


