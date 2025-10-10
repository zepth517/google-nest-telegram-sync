import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[RotatingFileHandler(filename="nest_sync.log",
                                                  mode="a+",
                                                  maxBytes=10000000,
                                                  backupCount=5)]
                    )
logger = logging.getLogger(__name__)
