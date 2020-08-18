import json
from shublang.shublang import evaluate


def traverse_specs(specs, data):
    """Given a specs object, it will evaluate all the shublang expressions found,
    populating it with `data` and returning the newly filled object.
    """
    for key in specs:
        if isinstance(key, str):
            if specs[key]:
                specs[key] = evaluate(specs[key], [data])
        else:
            specs[key] = traverse_specs(specs[key], data)

    return specs


def get_resource_data(name):
    with open(f"tests/resources/{name}", "r") as f:
        data = json.loads(f.read())

    return data
