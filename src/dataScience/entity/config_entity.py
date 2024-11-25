from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: Path 
    local_data_file: Path 
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path 
    status_file: str 
    unzip_data_dir: Path
    all_schema: dict

@dataclass 
class DataTransformationConfig:
    root_dir: Path 
    data_path: Path