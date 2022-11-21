import random
from typing import List, Optional

from fipy.ngsi.entity import FloatAttr
from fipy.ngsi.headers import FiwareContext
from fipy.ngsi.orion import OrionClient
from fipy.sim.sampler import DevicePoolSampler
from ngsy import MachineStatus
from settings import (
    OPTIPLANT_SUB,
    ORION_EXTERNAL_BASE_URL,
    QUANTUMLEAP_SUB,
    ROUGHNATOR_SUB,
    TENANT,
)
from uri import URI


class SubMan:
    def __init__(self):
        self._orion = orion_client()

    def create_roughnator_sub(self):
        self._orion.subscribe(ROUGHNATOR_SUB)

    def create_quantumleap_sub(self):
        self._orion.subscribe(QUANTUMLEAP_SUB)

    def create_optiplant_sub(self):
        self._orion.subscribe(OPTIPLANT_SUB)

    def create_subscriptions(self) -> List[dict]:
        self.create_roughnator_sub()
        self.create_quantumleap_sub()
        self.create_optiplant_sub()
        return self._orion.list_subscriptions()


class MachineSampler(DevicePoolSampler):
    def __init__(self, pool_size: int, orion: Optional[OrionClient] = None):
        super().__init__(pool_size, orion if orion else orion_client())

    def new_device_entity(self) -> MachineStatus:
        seed = random.uniform(0, 1)  # nosec B311
        return MachineStatus(
            id="",
            # timestamp=DateTimeAttr.new('ksjdkjd'),
            uuid={"value": "46c6b056-c2b6-4180-a97b-4f231f4a7c23"},
            noise=FloatAttr.new(1.0335 + seed),
            vibration=FloatAttr.new(0.98201 + seed),
            humidity=FloatAttr.new(0.98201 + seed),
            motor_1_status=FloatAttr.new(0.98201 + seed),
            motor_1_rslr=FloatAttr.new(0.98201 + seed),
            motor_1_rslm=FloatAttr.new(0.98201 + seed),
            motor_1_voltage=FloatAttr.new(0.98201 + seed),
            motor_1_ampere=FloatAttr.new(0.98201 + seed),
            motor_2_status=FloatAttr.new(0.98201 + seed),
            motor_2_rslr=FloatAttr.new(0.98201 + seed),
            motor_2_rslm=FloatAttr.new(0.98201 + seed),
            motor_2_voltage=FloatAttr.new(0.98201 + seed),
            motor_2_ampere=FloatAttr.new(0.98201 + seed),
            motor_3_status=FloatAttr.new(0.98201 + seed),
            motor_3_rslr=FloatAttr.new(0.98201 + seed),
            motor_3_rslm=FloatAttr.new(0.98201 + seed),
            motor_3_voltage=FloatAttr.new(0.98201 + seed),
            motor_3_ampere=FloatAttr.new(0.98201 + seed),
            motor_4_status=FloatAttr.new(0.98201 + seed),
            motor_4_rslr=FloatAttr.new(0.98201 + seed),
            motor_4_rslm=FloatAttr.new(0.98201 + seed),
            motor_4_voltage=FloatAttr.new(0.98201 + seed),
            motor_4_ampere=FloatAttr.new(0.98201 + seed),
            motor_5_status=FloatAttr.new(0.98201 + seed),
            motor_5_rslr=FloatAttr.new(0.98201 + seed),
            motor_5_rslm=FloatAttr.new(0.98201 + seed),
            motor_5_voltage=FloatAttr.new(0.98201 + seed),
            motor_5_ampere=FloatAttr.new(0.98201 + seed),
        )


def orion_client(service_path: Optional[str] = None, correlator: Optional[str] = None) -> OrionClient:
    base_url = URI(ORION_EXTERNAL_BASE_URL)
    ctx = FiwareContext(service=TENANT, service_path=service_path, correlator=correlator)
    return OrionClient(base_url, ctx)
