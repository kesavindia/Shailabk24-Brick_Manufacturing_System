import logging
logging.basicConfig(level=logging.INFO,filename="log.log",filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

# x=2
#log the value of variable
# logging.info(f"the value of x is {x}")

#logging level:(what logger i am using root logger):logging message
try:
    1/0
except ZeroDivisionError as e:
    # logging.error("ZeroDivisionError", exc_info=True)
    logging.exception("ZeroDivisionError")
logger = logging.getLogger(__name__)
#custom logger
handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info("test the custom logger")