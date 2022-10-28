"""
Define the yaml loader interface
"""

try:
    import yaml

    HAS_YAML = (True,)
except ImportError as e:
    HAS_YAML = False, str(e)

__virtualname__ = "yaml"


def __virtual__(hub):
    return HAS_YAML


def load(hub, path):
    """
    use yaml to read in a file
    """
    try:
        with open(path, "rb") as fp_:
            return yaml.safe_load(fp_.read())
    except FileNotFoundError:
        pass
    return {}


def render(hub, val):
    """
    Take the string and render it in json
    """
    return yaml.safe_load(val)
