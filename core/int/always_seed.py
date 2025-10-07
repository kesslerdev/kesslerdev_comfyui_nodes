# wildcard trick is taken from pythongossss's
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any_typ = AnyType("*")

import random

class KD_AlwaysSeed:

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"signal": ("STRING", {"default": ""}) }}

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("dyna_seed",)
    FUNCTION = "seedint"
    OUTPUT_NODE = True
    CATEGORY = "Utility"

    @staticmethod
    def seedint(signal):
        return (random.randint(0, 0xffffffffffffffff),)