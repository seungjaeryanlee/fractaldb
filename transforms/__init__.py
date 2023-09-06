import logging

import torchvision

from utils import dict_without

logger = logging.getLogger(__name__)
DATA_ROOT = "data/"


def create_transform(config):
    """Factory method for single transform."""
    if config.name == "torchvision.transforms.CenterCrop":
        return torchvision.transforms.CenterCrop(**dict_without(config, "name"))
    if config.name == "torchvision.transforms.RandomVerticalFlip":
        return torchvision.transforms.RandomVerticalFlip(**dict_without(config, "name"))

    logger.error(f"{config.name} is not a supported transform.")
    raise ValueError(f"{config.name} is not a supported transform.")


def create_transforms(config):
    """Factory method for multiple transforms."""
    return [create_transform(transform_config) for transform_config in config]
