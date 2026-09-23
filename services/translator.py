import os

from google import genai


class TranslationService:

    MODEL = "gemini-3.8-flash"

    LANGUAGE_NAMES = {
        "en": "English",
        "hi": "Hindi",
        "bn": "Bengali",
        "fr": "French",
        "de": "German",
        "es": "Spanish",
        "it": "Italian",
        "pt": "Portuguese",
        "ru": "Russian",
        "ja": "Japanese",
        "ko": "Korean",
        "ar": "Arabic",
        "zh": "Chinese"
    }

    @staticmethod
    def translate(text, source, target):
        """Translate text using the Google Gemini API."""

        if not text or not text.strip():
            raise ValueError("Text cannot be empty.")

        if not source or not target:
            raise ValueError(
                "Source and target languages are required."
            )

        if source not in TranslationService.LANGUAGE_NAMES:
            raise ValueError("Unsupported source language.")

        if target not in TranslationService.LANGUAGE_NAMES:
            raise ValueError("Unsupported target language.")

        # No API request is required for the same language.
        if source == target:
            return text.strip()

        api_key = os.getenv("GEMINI_API_KEY", "").strip()

        if not api_key:
            raise RuntimeError(
                "Gemini API key is not configured."
            )

        source_language = TranslationService.LANGUAGE_NAMES[source]
        target_language = TranslationService.LANGUAGE_NAMES[target]

        prompt = f"""
Translate the following text from {source_language} to {target_language}.

Important rules:
1. Return ONLY the translated text.
2. Do not add explanations.
3. Do not add quotation marks.
4. Preserve the original meaning.
5. Preserve names, numbers, punctuation and formatting whenever appropriate.
6. Do not translate code, URLs or email addresses unnecessarily.

Text to translate:
{text.strip()}
"""

        try:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model=TranslationService.MODEL,
                contents=prompt
            )

            translated_text = response.text

            if not translated_text:
                raise RuntimeError(
                    "Gemini returned an empty translation."
                )

            return translated_text.strip()

        except Exception as error:
            print("Gemini Translation Error:", error)

            raise RuntimeError(
                "Translation service is currently unavailable."
            ) from error
