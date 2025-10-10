from .core.text.multiline_choice import KD_MultilineTextChoice
from .core.text.env import KD_EnvironmentVariableGetter
from .core.int.always_seed import KD_AlwaysSeed
from .core.image.load_image import KD_LoadImageAndFilename
from .core.image.load_images import KD_LoadImagesFromFolder
from .utils import icon

NODE_CLASS_MAPPINGS = {
    "KesslerDev_MultilineTextChoice": KD_MultilineTextChoice,
    "KesslerDev_EnvironmentVariableGetter": KD_EnvironmentVariableGetter,
    "KesslerDev_AlwaysSeed": KD_AlwaysSeed,
    "KesslerDev_LoadImageAndFilename": KD_LoadImageAndFilename,
    "KesslerDev_LoadImagesFromFolder": KD_LoadImagesFromFolder,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KesslerDev_MultilineTextChoice": f"{icon} Multiline Text Choice",
    "KesslerDev_EnvironmentVariableGetter": f"{icon} Environment Variable Getter",
    "KesslerDev_AlwaysSeed": f"{icon} Always Seed",
    "KesslerDev_LoadImageAndFilename": f"{icon} Load Image And Filename",
    "KesslerDev_LoadImagesFromFolder": f"{icon} Load Images From Folder",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']