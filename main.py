from omegaconf import OmegaConf

from datasets import create_dataset
from models import create_model
from transforms import create_transform


if __name__ == "__main__":
    config = OmegaConf.load("configs/base.yaml")
    model = create_model(config.model)
    print(model)

    dataset = create_dataset(config.dataset)
    print(dataset)

    transform = create_transform(config.transform)
    print(transform)
