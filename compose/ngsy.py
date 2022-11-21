from typing import Optional

from fipy.ngsi.entity import Attr, BaseEntity, FloatAttr, TextAttr


class DateTimeAttr(Attr):
    type = "DateTime"
    value: str


class MachineStatus(BaseEntity):
    type = "ElevatorMachine"
    # timestamp: Optional[DateTimeAttr]
    uuid: Optional[TextAttr]
    noise: Optional[FloatAttr]
    vibration: Optional[FloatAttr]
    humidity: Optional[FloatAttr]
    motor_1_status: Optional[FloatAttr]
    motor_1_rslr: Optional[FloatAttr]
    motor_1_rslm: Optional[FloatAttr]
    motor_1_voltage: Optional[FloatAttr]
    motor_1_ampere: Optional[FloatAttr]

    motor_2_status: Optional[FloatAttr]
    motor_2_rslr: Optional[FloatAttr]
    motor_2_rslm: Optional[FloatAttr]
    motor_2_voltage: Optional[FloatAttr]
    motor_2_ampere: Optional[FloatAttr]

    motor_3_status: Optional[FloatAttr]
    motor_3_rslr: Optional[FloatAttr]
    motor_3_rslm: Optional[FloatAttr]
    motor_3_voltage: Optional[FloatAttr]
    motor_3_ampere: Optional[FloatAttr]

    motor_4_status: Optional[FloatAttr]
    motor_4_rslr: Optional[FloatAttr]
    motor_4_rslm: Optional[FloatAttr]
    motor_4_voltage: Optional[FloatAttr]
    motor_4_ampere: Optional[FloatAttr]

    motor_5_status: Optional[FloatAttr]
    motor_5_rslr: Optional[FloatAttr]
    motor_5_rslm: Optional[FloatAttr]
    motor_5_voltage: Optional[FloatAttr]
    motor_5_ampere: Optional[FloatAttr]
