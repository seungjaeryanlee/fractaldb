import logging

import torchvision


logger = logging.getLogger(__name__)


def create_model(config):
    """Factory method for model."""
    if config.name == "torchvision.models.resnet50":
        return torchvision.models.resnet50()

    logger.error(f"{config.name} is not a supported model.")
    raise ValueError(f"{config.name} is not a supported model.")
