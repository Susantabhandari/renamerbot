# Don't Remove Credit @SusantaBhandari GitHub 
# Subscribe Telegram Channel For Amazing Bot @Susanta_Bhandarii
# Ask Doubt on telegram @lifegrambot


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "")

API_HASH = os.environ.get("API_HASH", "")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Susanta_Bhandarii") 

             # Don't Remove Credit @SusantaBhandari GitHub
             # Subscribe Telegram Channel For Amazing Bot @Susanta_Bhandarii
             # Ask Doubt on telegram @lifegrambot

DB_NAME = os.environ.get("DB_NAME", "susantaxrenamerbot")     

DB_URL = os.environ.get("DB_URL", "")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @SusantaBhandari GitHub
# Subscribe Telegram Channel For Amazing Bot @Susanta_Bhandarii
# Ask Doubt on telegram @lifegrambot
