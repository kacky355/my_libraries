from logging import getLogger,DEBUG, INFO,Formatter, config
import os
import json

def get_my_logger(base_dir:str,logger_name:str=None, level=INFO, handlers:list=["consoleHandler", "fileHandler"], propagate=False, filename:str='main.log', config_path=None):
    log_dir = os.path.join(base_dir, 'logs')
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    logfile_dir=os.path.join(log_dir, filename)
    
    if config_path:
        with open(config_path, 'r') as f:
            log_conf = json.load(f)
    else:
        log_conf=_get_default_config()
        log_conf['handlers']['fileHandler']['filename'] = logfile_dir
    
        
    if logger_name:
        log_conf['loggers'].pop('main_log')
        log_conf = _set_new_logger(log_conf, logger_name, level, handlers, propagate)
    else:
        logger_name='main_log'

    config.dictConfig(log_conf)
    logger=getLogger(logger_name)
    logger.info(f'logger has made. log_dir:{log_dir}')
        
    return logger

def _get_default_config():
    log_conf = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s"
            }
        },

        "handlers": {
            "consoleHandler": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },
            "fileHandler": {
                "class": "logging.FileHandler",
                "level": "INFO",
                "formatter": "simple",
                "filename": ""
            }
        },

        "loggers": {
            "main_log": {
                "level": "DEBUG",
                "handlers": ["consoleHandler", "fileHandler"],
                "propagate": False
            }
        },

        "root": {
            "level": "INFO"
        }
    }
    
    return log_conf

def _set_new_logger(log_conf:dict, logger_name:str, level, handlers:list, propagate:bool):
    conf = log_conf
    new_logger = {
        "level" : level,
        "handlers" : handlers,
        "propagate" : propagate
    }
    conf['loggers'][logger_name] = new_logger
    return conf