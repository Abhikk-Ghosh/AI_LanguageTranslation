from services.translator import TranslationService


def test_same_language():

    result = TranslationService.translate(
        "Hello",
        "en",
        "en"
    )

    assert result == "Hello"


def test_english_to_hindi():

    result = TranslationService.translate(
        "Hello",
        "en",
        "hi"
    )

    assert result


def test_empty_text():

    try:

        TranslationService.translate(
            "",
            "en",
            "hi"
        )

        assert False

    except ValueError as error:

        assert str(error) == "Text cannot be empty."


def test_missing_language():

    try:

        TranslationService.translate(
            "Hello",
            "",
            "hi"
        )

        assert False

    except ValueError as error:

        assert str(error) == (
            "Source and target languages are required."
        )
