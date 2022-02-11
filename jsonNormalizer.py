from itertools import product, chain
from collections import ChainMap


class JsonNormalizer:
    @classmethod
    def normalize(cls, json: list):
        return dict(ChainMap(*
                             [{item["name"]: item[key] for key in item.keys() if "Val" in key}
                              for item in json]))
