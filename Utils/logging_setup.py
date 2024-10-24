from loguru import logger


def logging_setup():
    log_path = 'C:\\Users\\Radan Krch\\Desktop\\github_projects\\VSBLOG\\Logs\\log.log'
    logger.add(sink=log_path, level="INFO", format="{time:YYYY-MM-DD | HH:mm:ss} - {level:<8} - {message}")