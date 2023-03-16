import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Loading local configurations
LOCAL_CONFIG = os.getenv("LOCAL_CONFIG", "config/.env")
load_dotenv(os.path.join(BASE_DIR.parent, LOCAL_CONFIG))

ELASTICSEARCH_URL = os.getenv('ELASTICSEARCH_URL', 'http://docker.host:9200')
