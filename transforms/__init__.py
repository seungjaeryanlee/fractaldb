import logging
import os

import torchvision

from utils import dict_without

logger = logging.getLogger(__name__)
DATA_ROOT = "data/"


def create_transform(config):
    """Factory method for transform."""
    if config.name == "torchvision.transforms.CenterCrop":
        return torchvision.transforms.CenterCrop(**dict_without(config, "name"))

    logger.error(f"{config.name} is not a supported dataset.")
    raise ValueError(f"{config.name} is not a supported dataset.")
