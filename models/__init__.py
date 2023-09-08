import logging

from utils import dict_without, get_class_from_str


logger = logging.getLogger(__name__)


def create_model(config):
    """Factory method for model."""
    try:
        Class = get_class_from_str(config.name)
    except:
        logger.error(f"{config.name} is not a supported model.")
        raise ValueError(f"{config.name} is not a supported model.")

    return Class(**dict_without(config, "name"))
