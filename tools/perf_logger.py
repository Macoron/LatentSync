import logging

# Create a separate logger
exec_time_logger = logging.getLogger('execution_time')
exec_time_logger.setLevel(logging.INFO)
# Create a file handler
file_handler = logging.FileHandler('execution_time.log', mode='w')
file_handler.setLevel(logging.INFO)

# Create a formatter and attach it
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
exec_time_logger.addHandler(file_handler)

