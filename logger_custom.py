import logging

formatter = logging.Formatter(
   "{name} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

def setup_logger(name, log_file, level=logging.DEBUG):
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger('important', 'app4.log')
#logger.info('dolezite')

logger_all = setup_logger('all_values', 'all4.log')
#logger_all.info('all')