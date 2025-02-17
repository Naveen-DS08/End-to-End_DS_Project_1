import os 
import yaml 
from src.dataScience import logger 
import json 
import joblib 
from ensure import ensure_annotations
from box import ConfigBox 
from pathlib import Path 
from typing import Any 
from box.exceptions import BoxValueError 

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read yaml file and returns.

    Args:
        path_to_yaml (str) : path input 
    Raises: 
        valueError: if yaml file is empty
        e: empty file 
    Returns: 
        ConfigBox: Configbox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file) 
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content) 
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories

    Args: 
        path_to_directories(list) : path of directories in list
        ignore_log(bool, optional) : ignor if multiple directories is to be created.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json file.

    Args: 
        path : path to json file
        data : data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load json file data

    Args: 
        path : path to Json file
    Returns:
        configBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path: Path):
    """
    Save binary file

    Args:
        data: data to be saved as binary
        path : path to binary file 
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary data
    Args:
        path: path to binary file
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded succesfully")
    return data
