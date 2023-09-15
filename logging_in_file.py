import logging


def write_in_log_info(text, log_type="info"):
    # Настройка логирования
    logging.basicConfig(handlers=[logging.FileHandler('log_file_for_tests.log', 'a', 'utf-8')], level=logging.INFO,
                        format='%(asctime)s - %(levelname)s : %(message)s', force=True)

    if log_type == "info":
        logging.info(text)
    else:
        logging.error(text)