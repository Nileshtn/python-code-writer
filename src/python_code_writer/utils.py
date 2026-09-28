import yaml


def load_yaml(path: str) -> dict:
    with open(path, "r") as yaml_file:
        config = yaml.safe_load(yaml_file)

    return config