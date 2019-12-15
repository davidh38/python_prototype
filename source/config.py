import yaml
import os

def read(file="config.yml") -> dict:
    """ reads the config.yml file and returns the data as dictionary

    Returns:
        (dict): dictionary of .yml file
    """
    print(os.getcwd())
    with open(file) as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        return dict(cfg)