from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import logging

logger = logging.getLogger(__name__)

def create_database_automatically(database_url: str):
    """
    Automatically creates the database if it doesn't exist.
    """
    try:
        # Extract database name from URL
        db_name = database_url.split('/')[-1]
        base_url = database_url.rsplit('/', 1)[0]
        
        # Connect to default database to create target database
        temp_engine = create_engine(f"{base_url}/postgres")
        
        with temp_engine.connect() as conn:
            conn.execute(text("COMMIT"))
            try:
                conn.execute(text(f"CREATE DATABASE {db_name}"))
                logger.info(f"Database '{db_name}' created successfully")
            except Exception as e:
                if "already exists" in str(e):
                    logger.info(f"Database '{db_name}' already exists")
                else:
                    logger.error(f"Error creating database: {e}")
        
        temp_engine.dispose()
        
    except Exception as e:
        logger.error(f"Database creation error: {e}")
