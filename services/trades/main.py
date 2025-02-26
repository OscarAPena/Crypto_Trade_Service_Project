from loguru import logger

def main():
    """This program does 2 tasks.
        1. Reads trades from the Kraken API and
        2. Pushes the trades to a Kafka topic.
    Args:
        None
    Returns:
        None
    """
    logger.info("Start the trades service.")


if __name__ == "__main__":
    main()
