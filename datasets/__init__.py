import logging

from utils import create_class


logger = logging.getLogger(__name__)
DATA_ROOT = "data/"


def create_dataset(config):
    """Factory method for dataset."""
    try:
        dataset = create_class(**config)
    except ValueError:
        logger.error(f"{config.name} is not a supported dataset.")
        raise ValueError(f"{config.name} is not a supported dataset.")

    return dataset
