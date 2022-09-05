from pathlib import Path

__version__ = "0.1.0"
__description__ = "Predictive Maintenance for Manufacturing SMEs"

MODEL_PATH = Path(__file__).parent.parent.parent / "model" / "optiplant.model.pkl"

LOGGING_CONFIG = Path(__file__).parent / "logging.conf"
