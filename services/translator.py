import os

from google import genai


class TranslationService:

    MODEL = "gemini-3.8-flash"

    LANGUAGE_NAMES = {
        "en": "English",
        "hi": "Hindi",
        "bn": "Bengali (India)",
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
You are a professional translation engine.

Translate the text below from {source_language} to {target_language}.

STRICT REQUIREMENTS:
- Return ONLY the translation.
- Do not explain the translation.
- Do not add quotation marks.
- Do not add labels such as "Translation:".
- Preserve names, numbers and punctuation.
- Preserve line breaks when possible.
- If the target language is Bengali, write the result using Bengali script (বাংলা), not English letters.
- If the target language is Bengali (India), use natural standard Indian Bengali.
- Do not transliterate Bengali into English.
- Translate the meaning accurately and naturally.

Source language: {source_language}
Target language: {target_language}

Text:
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
