import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "TimeSaver API"
    VERSION: str = "1.0.0"

settings = Settings()