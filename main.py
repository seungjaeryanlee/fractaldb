from omegaconf import OmegaConf

from datasets import create_dataset
from models import create_model
from transforms import create_transforms


if __name__ == "__main__":
    config = OmegaConf.load("configs/base.yaml")
    model = create_model(config.model)
    print(model)

    dataset = create_dataset(config.dataset)
    print(dataset)

    transforms = create_transforms(config.transforms)
    print(transforms)
