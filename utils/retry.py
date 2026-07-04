import time

from config import Config

from utils.logger import Logger


logger = Logger()


def retry(func):

    def wrapper(*args, **kwargs):

        last_error = None

        for attempt in range(1, Config.MAX_RETRIES + 1):

            try:

                if attempt > 1:

                    logger.info(

                        f"Retry Attempt {attempt}"

                    )

                return func(*args, **kwargs)

            except Exception as e:

                last_error = e

                logger.error(

                    f"Attempt {attempt} Failed : {e}"

                )

                time.sleep(2)

        raise last_error

    return wrapper