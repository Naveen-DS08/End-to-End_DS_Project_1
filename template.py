import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]:%(message)s:")


project_name = "dataScience"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init.py",
    f"src/{project_name}/comkponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html"
]

# Creating file directory

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Creating the directory
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename}")
    
    # Creating the file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:

            pass
            logging.info(f"Creating an empty file: {filename}")
        
    else:
        logging.info(f"{filename} already exists!")


