import os
import json
import logging
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from notion_client import Client
from google.oauth2 import service_account
from googleapiclient.discovery import build
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup rate limiting
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["500 per day", "100 per hour"],
    storage_uri="memory://"
)

# MongoDB connection
MONGODB_URI = os.getenv('MONGODB_URI')
db = None
if MONGODB_URI:
    try:
        client = MongoClient(MONGODB_URI)
        db = client.get_database()
        logger.info("Connected to MongoDB")
    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {str(e)}")
else:
    logger.error("MONGODB_URI not set. MongoDB won't work.")

# Notion connection
notion = None
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
if NOTION_TOKEN:
    try:
        notion = Client(auth=NOTION_TOKEN)
        logger.info("Connected to Notion API")
    except Exception as e:
        logger.error(f"Error connecting to Notion API: {str(e)}")
else:
    logger.error("NOTION_TOKEN not set. Notion API won't work.")

# Google services connection
drive_service = None
sheets_service = None
forms_service = None
GOOGLE_CREDENTIALS = os.getenv('GOOGLE_CREDENTIALS')
if GOOGLE_CREDENTIALS:
    try:
        creds_dict = json.loads(GOOGLE_CREDENTIALS)
        creds = service_account.Credentials.from_service_account_info(
            creds_dict,
            scopes=['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/forms']
        )
        drive_service = build('drive', 'v3', credentials=creds)
        sheets_service = build('sheets', 'v4', credentials=creds)
        forms_service = build('forms', 'v1', credentials=creds)
        logger.info("Connected to Google services")
    except Exception as e:
        logger.error(f"Error connecting to Google services: {str(e)}")
else:
    logger.error("GOOGLE_CREDENTIALS not set. Google services won't work.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gdrive')
def gdrive():
    if not drive_service &#8203;:contentReference[oaicite:0]{index=0}&#8203;
