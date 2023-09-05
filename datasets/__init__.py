import logging
import os

import torchvision


logger = logging.getLogger(__name__)
DATA_ROOT = "data/"


def create_dataset(config):
    """Factory method for dataset."""
    os.makedirs(DATA_ROOT, exist_ok=True)

    if config.name == "torchvision.datasets.CIFAR10":
        return torchvision.datasets.CIFAR10(DATA_ROOT, download=True)

    logger.error(f"{config.name} is not a supported dataset.")
    raise ValueError(f"{config.name} is not a supported dataset.")
