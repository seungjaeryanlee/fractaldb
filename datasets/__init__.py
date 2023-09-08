import logging

from utils import dict_without, get_class_from_str


logger = logging.getLogger(__name__)
DATA_ROOT = "data/"


def create_dataset(config):
    """Factory method for dataset."""
    try:
        Class = get_class_from_str(config.name)
    except:
        logger.error(f"{config.name} is not a supported dataset.")
        raise ValueError(f"{config.name} is not a supported dataset.")

    return Class(root=DATA_ROOT, **dict_without(config, "name"))