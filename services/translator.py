import requests


class TranslationService:

    API_URL = "https://translate.googleapis.com/translate_a/single"

    @staticmethod
    def translate(text, source, target):
        """Translate text using Google Translate's web endpoint."""

        if not text or not text.strip():
            raise ValueError("Text cannot be empty.")

        if not source or not target:
            raise ValueError(
                "Source and target languages are required."
            )

        if source == target:
            return text

        params = {
            "client": "gtx",
            "sl": source,
            "tl": target,
            "dt": "t",
            "q": text.strip()
        }

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(
            TranslationService.API_URL,
            params=params,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        if not data or not data[0]:
            raise RuntimeError(
                "Translation service returned no translation."
            )

        translated_parts = []

        for item in data[0]:
            if item and item[0]:
                translated_parts.append(item[0])

        translated_text = "".join(translated_parts).strip()

        if not translated_text:
            raise RuntimeError(
                "Translation service returned no translation."
            )

        return translated_text
