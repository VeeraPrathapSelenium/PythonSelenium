import logging

#step 1: Create and configure the logger

logging.basicConfig(filename="Logstatus.log",filemode='w',format='%(asctime)s   %(module)s  %(lineno)d %(levelname)s %(message)s' )


#Step2: Create an object to the logger class

logger=logging.getLogger()

#Step 3: set the level for logging
logger.setLevel(logging.DEBUG)

logger.debug("Hello i am from debug level")
logger.info("Hello i am from info level")
logger.warning("Hello i am from warning level")
logger.error("Hello i am from error level")
logger.critical("Hello i am from critical level")