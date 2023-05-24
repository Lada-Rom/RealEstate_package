from pathlib import Path
from typing import List

from pydantic import BaseModel
from strictyaml import YAML, load


class Config(BaseModel):
    dataset: str
    trained_model_path: str

    features: List[str]
    variables_to_drop: List[str]

    random_state: int
    train_size: float

    num_boost_round: int
    early_stopping_rounds: int
    verbose_eval: int
    metric: str

    predictors: List[str]
    predict_model: str


def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    PACKAGE_ROOT = Path(__file__).resolve().parent
    CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"

    if not cfg_path:
        cfg_path = CONFIG_FILE_PATH

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
    raise OSError(f"Did not find config file at path: {cfg_path}")
