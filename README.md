# AI into Production [ Oktopus.io ]
--Made with love for AI devs--

Using FastAPI, AWS S3 and AstraDB.
Clone this repo and follow the steps to push it to production easily!
Before starting, use model-tester to test that your model meets accuracy standards. 

### Settings
Create a .env file to store configuration data:
-ASTRA_DB_CLIENT_ID
-ASTRA_DB_CLIENT_SECRET
-AWS_ACCESS_KEY_ID
-AWS_SECRET_ACCESS_KEY
-ENPOINT_URL
-BUCKET_NAME
-REGION_NAME

### To execute data pipeline we use Pypyr
python3 -m pypyr pipelines/ai-model-download

### To execute the app
uvicorn app.main:app --reload

### To configure DB
Change key in app/main.py (last endpoint ) & app/models.py

### Online testing before going into production
Unzip ngrok.zip --> add to virtualenv bin folder
port = 8000
ngrok http 8000 
