import os
import requests


class TranslationService:

    API_URL = (
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/gemini-2.5-flash:generateContent"
    )

    @staticmethod
    def translate(text, source, target):
        """Translate text using the Gemini API."""

        if not text or not text.strip():
            raise ValueError("Text cannot be empty.")

        if not source or not target:
            raise ValueError(
                "Source and target languages are required."
            )

        if source == target:
            return text

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "Gemini API key is not configured."
            )

        prompt = f"""
Translate the following text from {source} to {target}.

Return ONLY the translated text.
Do not add explanations, quotation marks, or labels.

Text:
{text.strip()}
"""

        response = requests.post(
            TranslationService.API_URL,
            headers={
                "Content-Type": "application/json",
                "x-goog-api-key": api_key
            },
            json={
                "contents": [
                    {
                        "parts": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ],
                "generationConfig": {
                    "temperature": 0
                }
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        try:
            translated_text = (
                data["candidates"][0]
                ["content"]["parts"][0]["text"]
                .strip()
            )
        except (KeyError, IndexError, TypeError):
            raise RuntimeError(
                "Gemini returned an invalid translation response."
            )

        if not translated_text:
            raise RuntimeError(
                "Gemini returned an empty translation."
            )

        return translated_text
