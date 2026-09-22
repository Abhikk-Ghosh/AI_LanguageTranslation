import requests


class TranslationService:

    API_URL = "https://api.mymemory.translated.net/get"

    @staticmethod
    def translate(text, source, target):
        """Translate text using the MyMemory Translation API."""

        if not text or not text.strip():
            raise ValueError("Text cannot be empty.")

        if not source or not target:
            raise ValueError(
                "Source and target languages are required."
            )

        if source == target:
            return text

        params = {
            "q": text.strip(),
            "langpair": f"{source}|{target}"
        }

        response = requests.get(
            TranslationService.API_URL,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        if "responseData" not in data:
            raise RuntimeError(
                "Invalid response from translation service."
            )

        translated_text = data["responseData"].get(
            "translatedText"
        )

        if not translated_text:
            raise RuntimeError(
                "Translation service returned no translation."
            )

        return translated_text
