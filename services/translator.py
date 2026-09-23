import os
import time

from google import genai


class TranslationService:

    # Try lightweight/high-volume model first.
    MODELS = [
        "gemini-3.5-flash-lite",
        "gemini-3.8-flash",
        "gemini-3.6-flash"
    ]

    LANGUAGE_NAMES = {
        "af": "Afrikaans",
        "ak": "Akan",
        "sq": "Albanian",
        "am": "Amharic",
        "ar": "Arabic",
        "hy": "Armenian",
        "as": "Assamese",
        "az": "Azerbaijani",
        "eu": "Basque",
        "be": "Belarusian",
        "bn": "Bengali",
        "bs": "Bosnian",
        "bg": "Bulgarian",
        "my": "Burmese",
        "ca": "Catalan",
        "ceb": "Cebuano",
        "zh-Hans": "Chinese (Simplified)",
        "zh-Hant": "Chinese (Traditional)",
        "hr": "Croatian",
        "cs": "Czech",
        "da": "Danish",
        "nl": "Dutch",
        "en": "English",
        "et": "Estonian",
        "fo": "Faroese",
        "fil": "Filipino",
        "fi": "Finnish",
        "fr": "French",
        "gl": "Galician",
        "ka": "Georgian",
        "de": "German",
        "el": "Greek",
        "gu": "Gujarati",
        "ha": "Hausa",
        "he": "Hebrew",
        "hi": "Hindi",
        "hu": "Hungarian",
        "is": "Icelandic",
        "id": "Indonesian",
        "ga": "Irish",
        "it": "Italian",
        "ja": "Japanese",
        "kn": "Kannada",
        "kk": "Kazakh",
        "km": "Khmer",
        "rw": "Kinyarwanda",
        "ko": "Korean",
        "ku": "Kurdish",
        "ky": "Kyrgyz",
        "lo": "Lao",
        "lv": "Latvian",
        "lt": "Lithuanian",
        "mk": "Macedonian",
        "ms": "Malay",
        "ml": "Malayalam",
        "mt": "Maltese",
        "mi": "Maori",
        "mr": "Marathi",
        "mn": "Mongolian",
        "ne": "Nepali",
        "no": "Norwegian",
        "or": "Odia",
        "om": "Oromo",
        "ps": "Pashto",
        "fa": "Persian",
        "pl": "Polish",
        "pt-BR": "Portuguese (Brazil)",
        "pt-PT": "Portuguese (Portugal)",
        "pa": "Punjabi",
        "qu": "Quechua",
        "ro": "Romanian",
        "rm": "Romansh",
        "ru": "Russian",
        "sr": "Serbian",
        "sd": "Sindhi",
        "si": "Sinhala",
        "sk": "Slovak",
        "sl": "Slovenian",
        "so": "Somali",
        "st": "Southern Sotho",
        "es": "Spanish",
        "sw": "Swahili",
        "sv": "Swedish",
        "tg": "Tajik",
        "ta": "Tamil",
        "te": "Telugu",
        "th": "Thai",
        "tn": "Tswana",
        "tr": "Turkish",
        "tk": "Turkmen",
        "uk": "Ukrainian",
        "ur": "Urdu",
        "uz": "Uzbek",
        "vi": "Vietnamese",
        "cy": "Welsh",
        "fy": "Western Frisian",
        "wo": "Wolof",
        "yo": "Yoruba",
        "zu": "Zulu"
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
            raise ValueError(
                f"Unsupported source language: {source}"
            )

        if target not in TranslationService.LANGUAGE_NAMES:
            raise ValueError(
                f"Unsupported target language: {target}"
            )

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
You are a professional multilingual translation engine.

Translate the following text from {source_language} to {target_language}.

STRICT RULES:

1. Return ONLY the translated text.
2. Do not provide explanations.
3. Do not add quotation marks.
4. Do not add labels such as "Translation:".
5. Preserve names, numbers and punctuation.
6. Preserve line breaks whenever possible.
7. Preserve URLs, email addresses and code when appropriate.
8. Translate naturally and accurately.
9. If the target language uses a non-Latin writing system, use its native script.
10. Do not transliterate the translation into English letters.

Source language:
{source_language}

Target language:
{target_language}

Text:
{text.strip()}
"""

        client = genai.Client(api_key=api_key)

        last_error = None

        for model in TranslationService.MODELS:

            try:

                print(
                    f"Trying Gemini model: {model}"
                )

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                translated_text = response.text

                if translated_text:
                    print(
                        f"Translation successful using: {model}"
                    )

                    return translated_text.strip()

                raise RuntimeError(
                    "Gemini returned an empty translation."
                )

            except Exception as error:

                last_error = error

                error_text = str(error)

                print(
                    f"Gemini model {model} failed: {error_text}"
                )

                # If this is a temporary service problem,
                # try the next available model.
                if (
                    "503" in error_text
                    or "UNAVAILABLE" in error_text
                    or "high demand" in error_text
                    or "429" in error_text
                    or "RESOURCE_EXHAUSTED" in error_text
                ):
                    time.sleep(1)
                    continue

                # For other errors, don't hide the real problem.
                break

        print(
            "All Gemini translation models failed:",
            last_error
        )

        raise RuntimeError(
            "Translation service is temporarily unavailable. "
            "Please try again."
        ) from last_error
