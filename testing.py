from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger= get_logger(__name__)


def divide_number(a,b):
    try:
        result=a/b
        logger.info("dividing teo num")
        return result
    except:
        logger.error("error occured")
        raise CustomException("custom error zero", sys)
    
if __name__=="__main__":
    try:
        logger.info("Staring msg")
        divide_number(10,0)
    except CustomException as ce:
        logger.error(str(ce))