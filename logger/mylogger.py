from logging import getLogger,DEBUG, INFO,Formatter, config
import os
import json

def get_my_logger(base_dir:str,filename:str='main.log', config_path=None):
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

    config.dictConfig(log_conf)
    
    logger=getLogger(__name__)
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
            "__main__": {
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