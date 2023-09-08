import importlib
import logging

from utils import dict_without

logger = logging.getLogger(__name__)
DATA_ROOT = "data/"


def _get_class_from_str(module_class_str: str):
    """Import and get Class from as string.

    We assume config.name has format similar to module.submodule.Class
    """
    module_str, class_name = module_class_str.rsplit(".", 1)
    Class = getattr(importlib.import_module(module_str), class_name)

    return Class


def create_transform(config):
    """Factory method for single transform."""
    try:
        Class = _get_class_from_str(config.name)
    except:
        logger.error(f"{config.name} is not a supported transform.")
        raise ValueError(f"{config.name} is not a supported transform.")

    return Class(**dict_without(config, "name"))


def create_transforms(config):
    """Factory method for multiple transforms."""
    return [create_transform(transform_config) for transform_config in config]
