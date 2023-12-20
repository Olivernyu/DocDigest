from app.prompt_template import apply_prompt_template


def test_apply_prompt_template():
    # Test case 1: prompt_type is "summarizer"
    prompt_type = "summarizer"
    text_from_html = "Lorem ipsum dolor sit amet."
    expected_output = '\nWrite a concise summary of the following text extracted from a web page:\n\n\n"Lorem ipsum dolor sit amet."\n\n\nCONCISE SUMMARY:\n'  # noqa
    assert apply_prompt_template(prompt_type, text_from_html) == expected_output

    # Test case 2: prompt_type is "highlighter"
    prompt_type = "highlighter"
    expected_output = '\nGiven the following raw html extracted from a web page, highlight the \nmost important words and sentences in the context of the webpage using \nhtml <b> tags while preserving the original html structure:\n\n\n"Lorem ipsum dolor sit amet."\n\n\nHIGHLIGHTED HTML:\n'  # noqa
    assert apply_prompt_template(prompt_type, text_from_html) == expected_output

    # Test case 3: prompt_type is unknown
    prompt_type = "unknown"
    try:
        apply_prompt_template(prompt_type, text_from_html)
        assert False, "Exception not raised for unknown prompt_type"
    except Exception as e:
        assert str(e) == "Prompt type unknown not found."
