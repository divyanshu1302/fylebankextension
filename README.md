# Twitter Stream Filter API(TweetBot)

APIs is been created to retrieve data based on applied filters. It is two types-
1. Filter to extract bank details based on ifsc code
2. Filter to extract bank details based on bank name and city.

Technologies used:
  - Python
  - Flask framework
  - MongoDb
  
## To setup project (Installation Instructions)
  1. clone the project
  2. cd to project folder `cd fylebankextension` and create virtual environment
  `virtualenv venv`
  3. activate virtual environment
  `source venv/bin/activate`
  4. install requirements after activating virtual environment
  `pip install -r requirements.txt`
  5. Upload csv file on mlabs and configure project with mlabs credentials.


## To runserver (Installation Instructions)
Run the `python runserver.py` 
  
## API's/Endpoints

API - `/fetchdetails?bankname=ALLAHABAD BANK&city=RAE BARELI` or `/fetchdetails?ifsc=A12345I8`
(methods supported - GET, POST)

RESULT - `{`
    `"data":[{"address":"ABHYUDAYA BANK BLDG., 251, PERIN NARIMAN STREET, FORT,                MUMBAI-400001","bank_id":60,"bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED",  "branch":"FORT","city":"MUMBAI","district":"GREATER MUMBAI","ifsc":"ABHY0065006","state":"MAHARASHTRA"}],`
    `"message":"Suceesfully Extracted"`
    `"status":"success"`
    `}`

PRODUCTION - https://fylebankmanager.herokuapp.com/ deplyed on heroku and filter format is same as above