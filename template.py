import os
from pathlib import Path


list_files = [
    "src/__init__.py",
    "src/data_ingestion.py",
    "src/embedding.py",
    "src/model_api.py",
    "app.py",
    "logger.py",
    "exception.py",
    "setup.py"
]

for filepath in list_files:
    filepath = Path(filepath)
    file_dir,filename = os.path.split(filepath)

    if file_dir!= "":
        os.makedirs(file_dir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass

