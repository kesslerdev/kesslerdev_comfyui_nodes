from .core.text.multiline_choice import KD_MultilineTextChoice
from .core.text.env import KD_EnvironmentVariableGetter
from .core.int.always_seed import KD_AlwaysSeed

NODE_CLASS_MAPPINGS = {
    "KesslerDev_MultilineTextChoice": KD_MultilineTextChoice,
    "KesslerDev_EnvironmentVariableGetter": KD_EnvironmentVariableGetter,
    "KesslerDev_AlwaysSeed": KD_AlwaysSeed
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KesslerDev_MultilineTextChoice": "KD Multiline Text Choice",
    "KesslerDev_EnvironmentVariableGetter": "KD Environment Variable Getter",
    "KesslerDev_AlwaysSeed": "KD Always Seed"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']