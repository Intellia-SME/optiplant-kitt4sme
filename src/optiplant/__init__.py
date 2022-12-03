from pathlib import Path

__version__ = "1.0.2"
__description__ = "Optimised Predictive Maintenance for Manufacturing SMEs through Automated ML"

MODEL_PATH = Path(__file__).parent.parent.parent / "model" / "optiplant.model.pkl"

LOGGING_CONFIG = Path(__file__).parent / "logging.conf"
