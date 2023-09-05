from omegaconf import OmegaConf

from models import create_model


if __name__ == "__main__":
    config = OmegaConf.load("configs/base.yaml")
    model = create_model(config.model)
    print(model)
