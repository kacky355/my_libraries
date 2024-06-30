from logging import getLogger,DEBUG, INFO,Formatter, config
import os
import json

def get_my_logger(base_dir:str,filename:str='main.log'):
    log_dir = os.path.join(base_dir, 'logs')
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    logfile_dir=os.path.join(log_dir, filename)
    
    with open('logger/log_config.json', 'r') as f:
        log_conf = json.load(f)
    log_conf['handlers']['fileHandler']['filename'] = logfile_dir

    config.dictConfig(log_conf)
    
    logger=getLogger(__name__)
    logger.info(f'logger has made. log_dir:{log_dir}')

    return logger