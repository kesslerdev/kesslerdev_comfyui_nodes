class KD_EnvironmentVariableGetter:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "var_name": ("STRING", {"default": "", "tooltip": "Name of the environment variable to get."}),
            },
        }

    DESCRIPTION = "Get the value of an environment variable."
    RETURN_TYPES = ("STRING",)
    # Names for the returned values
    RETURN_NAMES = ("value",)
    # Function to process the inputs
    FUNCTION = "process"
    # Category under which this node will appear in the UI
    CATEGORY = "Utility"

    def process(self, var_name):
        import os
        selected_text = os.getenv(var_name, "")
        return (selected_text,)
