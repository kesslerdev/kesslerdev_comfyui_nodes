class KD_MultilineTextChoice:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Input: Multiline text string with a default empty value
                "prepend_text": ("STRING", {"default": ""}),
                "multiline_text": ("STRING", {"multiline": True, "default": ""}),
                "append_text": ("STRING", {"default": ""}),
                "wrap_index": ("BOOLEAN", {"default": True, "tooltip": "When enabled, the selected line wraps around the lines list length (e.g., 15 → 5 for 10 items)."}),
                # Input: Line number to select (1-based index), default is 1
                "selected_line_number": ("INT", {"default": 1, "min": 1, "max": 9999999}),
            },
        }

    DESCRIPTION = "Select a line from a multiline text input."
    RETURN_TYPES = ("INT", "INT", "STRING")
    # Names for the returned values
    RETURN_NAMES = ("selected_line", "total_lines", "selected_text")
    # Function to process the inputs
    FUNCTION = "process"
    # Category under which this node will appear in the UI
    CATEGORY = "Utility"

    def process(self, prepend_text, multiline_text, append_text, wrap_index, selected_line_number):
        # Split the input text into a list of non-empty, trimmed lines
        choices = [line.strip() for line in multiline_text.splitlines() if line.strip()]

        # Initialize default return values
        selected_line = 0
        total_lines = len(choices)
        selected_text = ""

        # Check if the selected line number is within the valid range
        if 1 <= selected_line_number <= len(choices):
            # Set the selected_line to the selected line number
            selected_line = selected_line_number
            # Retrieve the text of the selected line (adjusting for 0-based index)
            selected_text = choices[selected_line_number - 1]
        else:
            if wrap_index and len(choices) > 0:
                # Wrap the selected line number within the range of available lines
                wrapped_index = (selected_line_number - 1) % len(choices)
                selected_line = wrapped_index + 1
                selected_text = choices[wrapped_index]
            else:
                # If the selected line number is out of range, return defaults
                selected_line = 0
                selected_text = ""

        selected_text = f"{prepend_text} {selected_text} {append_text}".strip()
        return (selected_line, total_lines, selected_text)
