from llama_index.core import SimpleDirectoryReader
from exception import CustomException
from logger import logging

import sys

def load_data(data):

    try:
        logging.info("Data loading started------")
        loader = SimpleDirectoryReader("data")
        documents = loader.load_data()

        logging.info("Data loading completed-----")
        return documents
    
    except Exception as e:
        logging.info("Exception in loading data-------")
        raise CustomException(e,sys)



