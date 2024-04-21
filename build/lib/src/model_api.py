import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
from exception import CustomException
from logger import logging

import google.generativeai as genai

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

def load_model():

    try:
        model = Gemini(models="gemini-pro",api_key=google_api_key)
        return model
    except Exception as e:
        raise CustomException(e,sys)