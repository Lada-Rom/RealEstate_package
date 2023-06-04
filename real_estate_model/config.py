from pathlib import Path
from typing import List

from pydantic import BaseModel
from strictyaml import YAML, load

PACKAGE_ROOT = Path(__file__).resolve().parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"


class Config(BaseModel):
    dataset: str
    trained_model_path: str

    features: List[str]
    variables_to_drop: List[str]

    random_state: int
    test_size: float

    num_boost_round: int
    early_stopping_rounds: int
    verbose_eval: int
    metric: str

    predictors: List[str]
    predict_model: str


def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    if not cfg_path:
        cfg_path = CONFIG_FILE_PATH

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
    raise OSError(f"Did not find config file at path: {cfg_path}")


def set_config_field(field_name: str, value: str, cfg_path: Path = None):
    if not cfg_path:
        cfg_path = CONFIG_FILE_PATH

    with open(cfg_path, "r") as conf_file:
        lines = conf_file.readlines()

    with open(cfg_path, "w") as conf_file:
        for line in lines:
            if line.find(field_name) != -1:
                line = field_name + ": " + value + '\n'
            conf_file.write(line)


if __name__ == "__main__":
    set_config_field("predict_model", "./trained_models/lgb_model_v2.txt")
