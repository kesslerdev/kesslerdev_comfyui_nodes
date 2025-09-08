from .text.multiline_choice import MultilineTextChoice

NODE_CLASS_MAPPINGS = {
    "KesslerDev_MultilineTextChoice": MultilineTextChoice
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KesslerDev_MultilineTextChoice": "Multiline Text Choice (Kesslerdev)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']