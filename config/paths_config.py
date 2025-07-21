import os


########### DATA INGESTION ##############

# where to store data after ingestion
RAW_DIR= "artifacts/raw"
RAW_FILE_PATH= os.path.join(RAW_DIR, "raw.csv")
TRAIN_FILE_PATH = os.path.join(RAW_DIR, "train.csv")
TEST_FILE_PATH = os.path.join(RAW_DIR, "test.csv")

CONFIG_PATH="/Users/ridhampuri/Desktop/projectsmlpipelines/project1/config/config.yaml"


################### DATA PROCESSINF ######################


# HERE ALL PATHS REQUIRED FOR DATA PROCESSING ARE DEFINED


PROCESSED_DIR = "artifacts/processed"
PROCESSED_TRAIN_DATA_PATH = os.path.join(PROCESSED_DIR, "processed_train.csv")
PROCESSED_TEST_DATA_PATH = os.path.join(PROCESSED_DIR, "processed_test.csv")



###################### MODEL TRAINING ###########################

MODEL_OUTPUT_PATH = "artifacts/models/lgbm_model.pkl"