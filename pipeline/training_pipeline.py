# here we will write the code to train the pipeline,make it a package

# here we will write the code to train the pipeline,make it a package

import os

from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataProcessor
from src.model_training import ModelTraining
from utils.common_functions import read_yaml
from config.paths_config import *


if __name__=="__main__":
    # Compute absolute config path relative to project root
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    absolute_config_path = os.path.join(root_dir, 'config', 'config.yaml')  # Adjust 'config/config.yaml' if your file is nested differently

    ### 1. Data Ingestion
    data_ingestion = DataIngestion(read_yaml(absolute_config_path))
    data_ingestion.run()

    ### 2. Data Processing
    processor = DataProcessor(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,CONFIG_PATH)
    processor.process()

    ### 3. Model Training
    trainer = ModelTraining(PROCESSED_TRAIN_DATA_PATH,PROCESSED_TEST_DATA_PATH,MODEL_OUTPUT_PATH)
    trainer.run()