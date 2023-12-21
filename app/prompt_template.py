summarizer_prompt = """
Write a concise summary of the following text extracted from a web page:


"{text}"


CONCISE SUMMARY:
"""

highlighter_prompt = """
Given the following raw html extracted from a web page, highlight the 
most important words and sentences in the context of the webpage using 
html <b> tags while preserving the original html structure:


"{text}"


HIGHLIGHTED HTML:
"""


def apply_prompt_template(prompt_type: str, text_from_html: str) -> str:
    """
    Apply a prompt template based on the given prompt type.

    Args:
        prompt_type (str): The type of prompt template to apply.
        text_from_html (str): The text extracted from HTML.

    Returns:
        str: The formatted prompt template.

    Raises:
        Exception: If the prompt type is not found.
    """
    if prompt_type == "summarizer":
        return summarizer_prompt.format(text=text_from_html)
    elif prompt_type == "highlighter":
        return highlighter_prompt.format(text=text_from_html)
    else:
        raise Exception(f"Prompt type {prompt_type} not found.")
