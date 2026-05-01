import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    """Parse and expose environment variables"""
    
    # MongoDB Configuration
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME: str = os.getenv("DB_NAME", "digicollect")
    
    # FastAPI Configuration
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", "8000"))
    APP_TITLE: str = os.getenv("APP_TITLE", "DigiCollect API")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")


# Export settings instance
settings = Settings()
