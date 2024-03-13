import pathlib, json


def load_color_mapping(path: pathlib.Path) -> dict:
    with path.open() as cmap:
        result = json.load(cmap)
    return result
