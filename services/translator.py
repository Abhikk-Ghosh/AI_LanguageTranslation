import requests


class TranslationService:

    API_URLS = [
        "https://libretranslate.de/translate",
        "https://translate.terraprint.co/translate",
        "https://translate.api.skitzen.com/translate",
        "https://trans.zillyhuhn.com/translate"
    ]

    @staticmethod
    def translate(text, source, target):
        """Translate text using LibreTranslate public mirrors."""

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
            "Content-Type": "application/json",
            "User-Agent": "LinguaAI/1.0"
        }

        last_error = None

        for api_url in TranslationService.API_URLS:

            try:

                response = requests.post(
                    api_url,
                    json=payload,
                    headers=headers,
                    timeout=15
                )

                if response.status_code == 429:
                    last_error = "Rate limit reached"
                    continue

                if response.status_code >= 500:
                    last_error = (
                        f"Server error: {response.status_code}"
                    )
                    continue

                response.raise_for_status()

                data = response.json()

                translated_text = data.get("translatedText")

                if translated_text:
                    return translated_text.strip()

                last_error = "No translation returned."

            except requests.RequestException as error:

                last_error = str(error)
                continue

            except (ValueError, TypeError) as error:

                last_error = str(error)
                continue

        print("Translation services failed:", last_error)

        raise RuntimeError(
            "All translation services are currently unavailable."
        )
