import json

from fipy.wait import wait_for_orion
from helper import MachineSampler, SubMan, orion_client


def wait_on_orion():
    wait_for_orion(orion_client())


def create_subscriptions():
    man = SubMan()
    orion_subs = man.create_subscriptions()
    formatted = json.dumps(orion_subs, indent=4)
    print("Current subscriptions in Orion:")
    print(formatted)


def send_machine_entities():
    sampler = MachineSampler(pool_size=2)
    try:
        sampler.sample(samples_n=1000, sampling_rate=2.5)
    except Exception as e:
        print(e)


wait_on_orion()
create_subscriptions()
send_machine_entities()
