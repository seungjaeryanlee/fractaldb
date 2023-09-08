import logging

from utils import create_class


logger = logging.getLogger(__name__)


def create_model(config):
    """Factory method for model."""
    try:
        model = create_class(**config)
    except ValueError:
        logger.error(f"{config.name} is not a supported model.")
        raise ValueError(f"{config.name} is not a supported model.")

    return model
