import logging

from fastapi import FastAPI
from fipy.ngsi.entity import EntityUpdateNotification

from optiplant import LOGGING_CONFIG, __description__, __version__

from .ngsy import MachineStatus
from .utilities import process_update

logging.config.fileConfig(LOGGING_CONFIG, disable_existing_loggers=False)
logger = logging.getLogger(__name__)


app = FastAPI()


@app.get("/")
def home_page():
    return {"optiplant": __version__, "description": __description__}


@app.get("/version")
def get_version():
    return {"optiplant": __version__}


@app.post("/prediction")
def make_prediction(notification: EntityUpdateNotification):
    logger.info(f"Received new notification: {notification}")

    updated_machines = notification.filter_entities(MachineStatus)
    if updated_machines:
        return process_update(updated_machines)
