import logging
import warnings
from typing import Optional

from fastapi import FastAPI, Header
from fipy.ngsi.entity import EntityUpdateNotification
from fipy.ngsi.headers import FiwareContext

from optiplant import LOGGING_CONFIG, __description__, __version__

from .ngsy import MachineStatus
from .utilities import process_update, update_context

warnings.filterwarnings("ignore")
logging.config.fileConfig(LOGGING_CONFIG, disable_existing_loggers=False)
logger = logging.getLogger(__name__)


app = FastAPI(
    title="Optiplant",
    description=__description__,
    version="1.0.1",
    contact={
        "name": "Michael Loukeris",
        "url": "http://www.intellia.gr",
        "email": "mloukeris@intellia.gr",
    },
)


@app.get("/")
def home_page():
    return {"optiplant": __version__, "description": __description__}


@app.get("/version")
def get_version():
    return {"optiplant": __version__}


@app.post("/prediction")
def make_prediction(
    notification: EntityUpdateNotification,
    fiware_service: Optional[str] = Header(None),
    fiware_servicepath: Optional[str] = Header(None),
    fiware_correlator: Optional[str] = Header(None),
):

    ctx = FiwareContext(
        service=str(fiware_service), service_path=str(fiware_servicepath), correlator=str(fiware_correlator)
    )

    logger.info(f"Received new notification: {notification}")

    updated_machines = notification.filter_entities(MachineStatus)
    if updated_machines:
        predictions = process_update(updated_machines)
        update_context(ctx, predictions)
