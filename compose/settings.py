# see docker-compose
ORION_EXTERNAL_BASE_URL = "http://10.172.209.202/orion/"  # k8s
ORION_EXTERNAL_BASE_URL = "http://localhost:1026"  # docker-compose
TENANT = "csic"
ROUGHNATOR_INTERNAL_BASE_URL = "http://roughnator:8000"
OPTIPLANT_INTERNAL_BASE_URL = "http://optiplant:5000"
QUANTUMLEAP_INTERNAL_BASE_URL = "http://quantumleap:8668"

ROUGHNATOR_SUB = {
    "description": "Notify Roughnator of changes to any entity.",
    "subject": {"entities": [{"idPattern": ".*"}]},
    "notification": {"http": {"url": f"{ROUGHNATOR_INTERNAL_BASE_URL}/updates"}},
}

OPTIPLANT_SUB = {
    "description": "Notify Optiplant of changes to any entity.",
    "subject": {"entities": [{"idPattern": ".*"}]},
    "notification": {"http": {"url": f"{OPTIPLANT_INTERNAL_BASE_URL}/prediction"}},
}


QUANTUMLEAP_SUB = {
    "description": "Notify QuantumLeap of changes to any entity.",
    "subject": {"entities": [{"idPattern": ".*"}]},
    "notification": {"http": {"url": f"{QUANTUMLEAP_INTERNAL_BASE_URL}/v2/notify"}},
}
