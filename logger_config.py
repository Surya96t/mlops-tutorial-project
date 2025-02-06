from loguru import logger
import sys

def setup_logger(log_file="logs/main_log.log", level="INFO"):
    logger.remove()  # Remove default logger to prevent duplicate logs

    # Add file handler with rotation and retention
    logger.add(
        log_file,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} - {message}",
        level=level 
    )

    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=level
    )

    return logger

# Initialize logger
logger = setup_logger()

def get_logger():
    return logger
