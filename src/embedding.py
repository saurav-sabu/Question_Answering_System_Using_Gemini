from llama_index.core import VectorStoreIndex, ServiceContext, StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from src.data_ingestion import load_data
from src.model_api import load_model

import sys
from exception import CustomException
from logger import logging 


def download_gemini_embedding(model,document):

    try:
        logging.info("Embedding started to download -------")
        gemini_embedding_model = GeminiEmbedding(model_name="models/embedding-001")
        service_context = ServiceContext.from_defaults(llm=model,embed_model=gemini_embedding_model,chunk_size=800,chunk_overlap=20)

        logging.info("Storing Vector embedding--------")
        index = VectorStoreIndex.from_documents(document,service_context=service_context)
        index.storage_context.persist()


        logging.info("Querying results------")
        query_engine = index.as_query_engine()
        return query_engine
    
    except Exception as e:
        raise CustomException(e,sys)


