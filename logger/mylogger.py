from logging import getLogger,DEBUG, INFO,Formatter, StreamHandler, FileHandler
import os

class Logger:
    def __init__(self, base_dir:str, formatter:Formatter=None):
        self.logger = getLogger(__name__)
        
        self.log_dir = os.path.join(base_dir, 'logs')
        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)
        
        self.logger.setLevel(DEBUG)
        self.logger.propagate = False
        
        if formatter:
            self.formatter = formatter
        else:
            self.formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        self.sh = StreamHandler()
        self.sh.setLevel(DEBUG)
        self.sh.setFormatter(self.formatter)
        self.fh = FileHandler(os.path.join(self.log_dir,'main.log'))
        self.fh.setLevel(INFO)
        self.fh.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.sh)
        self.logger.info(f'logger has made. log_dir:{self.log_dir}')
    
    def add_new_handler(self, handler, formatter=None, level=INFO):
        additional_handler = handler
        
        additional_handler.setLevel(level)
        if formatter:
            additional_handler.setFormatter(formatter)
        else:
            additional_handler.setFormatter(self.formatter)
        
        self.logger.addHandler(additional_handler)
        self.logger.info('new handler added!')

        
