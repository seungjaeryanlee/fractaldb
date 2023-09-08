import logging

from utils import dict_without, get_class_from_str

logger = logging.getLogger(__name__)
DATA_ROOT = "data/"


def create_transform(config):
    """Factory method for single transform."""
    try:
        Class = get_class_from_str(config.name)
    except Exception:
        logger.error(f"{config.name} is not a supported transform.")
        raise ValueError(f"{config.name} is not a supported transform.")

    return Class(**dict_without(config, "name"))


def create_transforms(config):
    """Factory method for multiple transforms."""
    return [create_transform(transform_config) for transform_config in config]
