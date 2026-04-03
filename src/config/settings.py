"""
Application configuration settings
"""

from pydantic_settings import BaseSettings
from typing import Optional
from datetime import datetime


class Settings(BaseSettings):
    # Database
    database_url: str
    redis_url: str = "redis://localhost:6379"
    
    # Twelve Data API
    twelve_data_api_key: str
    
    # Application
    debug: bool = False
    log_level: str = "INFO"
    secret_key: str
    
    # Historical Data
    historical_start_date: datetime = datetime(2000, 1, 1)
    historical_end_date: datetime = datetime(2024, 12, 31)
    default_market: str = "INDIA"
    
    # Cache
    cache_ttl_seconds: int = 3600
    max_cache_size: int = 1000
    
    # Rate Limiting
    rate_limit_per_minute: int = 60
    rate_limit_per_hour: int = 1000
    
    class Config:
        env_file = ".env"


# Global settings instance
settings = Settings()
