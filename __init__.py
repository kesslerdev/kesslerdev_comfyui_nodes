from .text.multiline_choice import MultilineTextChoice
from .text.env import EnvironmentVariableGetter

NODE_CLASS_MAPPINGS = {
    "KesslerDev_MultilineTextChoice": MultilineTextChoice,
    "KesslerDev_EnvironmentVariableGetter": EnvironmentVariableGetter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KesslerDev_MultilineTextChoice": "Multiline Text Choice (Kesslerdev)",
    "KesslerDev_EnvironmentVariableGetter": "Environment Variable Getter (Kesslerdev)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']