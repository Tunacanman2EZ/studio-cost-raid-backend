import os

class DevelopmentConfig:
    DEBUG = True  # explanation - enable debug mode in development
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///dev.db"
    )  # explanation - use DATABASE_URL from env, or fall back to local sqlite dev.db
    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY", "dev-secret-not-for-prod"
    )  # explanation - JWT secret from env, with a dev-only fallback

class TestingConfig:
    # explanation - settings used when running automated tests
    TESTING = True  # explanation - tells Flask we are in testing mode
    DEBUG = False   # explanation - usually keep debug off during tests
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "TEST_DATABASE_URL", "sqlite:///test.db"
    )  # explanation - test DB URL, falls back to separate sqlite file
    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY", "test-secret-not-for-prod"
    )  # explanation - JWT secret for tests


class ProductionConfig:
    # explanation - settings used in real deployment / live server
    DEBUG = False   # explanation - never show debug info in production
    TESTING = False # explanation - not running tests in production
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL"
    )  # explanation - read production DB URL from env (must be set in real prod)
    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY"
    )  # explanation - read production JWT secret from env (must be set in real prod)
    
config_map = {
    "development": DevelopmentConfig,   # explanation - use this class for dev runs
    "testing": TestingConfig,           # explanation - use this class for tests
    "production": ProductionConfig,     # explanation - use this class for live server
}