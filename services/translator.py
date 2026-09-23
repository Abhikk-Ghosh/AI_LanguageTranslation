import requests


class TranslationService:

    API_URL = "https://translate.argosopentech.com/translate"

    @staticmethod
    def translate(text, source, target):
        """Translate text using the LibreTranslate API."""

        if not text or not text.strip():
            raise ValueError("Text cannot be empty.")

        if not source or not target:
            raise ValueError(
                "Source and target languages are required."
            )

        if source == target:
            return text

        payload = {
            "q": text.strip(),
            "source": source,
            "target": target,
            "format": "text"
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(
            TranslationService.API_URL,
            json=payload,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        translated_text = data.get("translatedText")

        if not translated_text:
            raise RuntimeError(
                "Translation service returned no translation."
            )

        return translated_text.strip()
