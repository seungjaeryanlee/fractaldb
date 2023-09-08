import logging

from utils import create_class

logger = logging.getLogger(__name__)
DATA_ROOT = "data/"


def create_transform(config):
    """Factory method for a single transform."""
    try:
        transform = create_class(**config)
    except ValueError:
        logger.error(f"{config.name} is not a supported model.")
        raise ValueError(f"{config.name} is not a supported model.")

    return transform


def create_transforms(config):
    """Factory method for multiple transforms."""
    return [create_transform(transform_config) for transform_config in config]
