import logging
from typing import List

import joblib
from fipy.ngsi.entity import FloatAttr

from optiplant import MODEL_PATH

from .ngsy import MachineStatus, MachineStatusPrediction

logger = logging.getLogger(__name__)


def predict(machine_status: MachineStatus) -> MachineStatusPrediction:
    model = joblib.load(MODEL_PATH)
    input = [
        [
            machine_status.noise.value,
            machine_status.vibration.value,
            machine_status.humidity.value,
            machine_status.motor_1_status.value,
            machine_status.motor_1_rslr.value,
            machine_status.motor_1_rslm.value,
            machine_status.motor_1_voltage.value,
            machine_status.motor_1_ampere.value,
            machine_status.motor_2_status.value,
            machine_status.motor_2_rslr.value,
            machine_status.motor_2_rslm.value,
            machine_status.motor_2_voltage.value,
            machine_status.motor_2_ampere.value,
            machine_status.motor_3_status.value,
            machine_status.motor_3_rslr.value,
            machine_status.motor_3_rslm.value,
            machine_status.motor_3_voltage.value,
            machine_status.motor_3_ampere.value,
            machine_status.motor_4_status.value,
            machine_status.motor_4_rslr.value,
            machine_status.motor_4_rslm.value,
            machine_status.motor_4_voltage.value,
            machine_status.motor_4_ampere.value,
            machine_status.motor_5_status.value,
            machine_status.motor_5_rslr.value,
            machine_status.motor_5_rslm.value,
            machine_status.motor_5_voltage.value,
            machine_status.motor_5_ampere.value,
        ]
    ]
    prediction = model.predict(input)
    logger.info(f"The current status is {machine_status} and the prediction {prediction}")
    return MachineStatusPrediction(id=machine_status.id, status=FloatAttr.new(prediction[0]))


def process_update(updates: List[MachineStatus]) -> List[MachineStatusPrediction]:
    predictions = [predict(m) for m in updates]
    return predictions
