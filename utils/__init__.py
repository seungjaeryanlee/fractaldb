import importlib


def dict_without(d, key):
    """Create new dict without one key."""
    new_d = d.copy()
    new_d.pop(key)

    return new_d

def get_class_from_str(module_class_str: str):
    """Import and get Class from as string.

    We assume config.name has format similar to module.submodule.Class
    """
    module_str, class_name = module_class_str.rsplit(".", 1)
    Class = getattr(importlib.import_module(module_str), class_name)

    return Class
