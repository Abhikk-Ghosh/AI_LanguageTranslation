import requests
from urllib.parse import quote


class TranslationService:

    API_URLS = [
        "https://translate.plausibility.cloud/api/v1/{source}/{target}/{text}",
        "https://lingva.garudalinux.org/api/v1/{source}/{target}/{text}",
        "https://translate.projectsegfau.lt/api/v1/{source}/{target}/{text}",
        "https://lingva.lunar.icu/api/v1/{source}/{target}/{text}"
    ]

    @staticmethod
    def translate(text, source, target):
        """Translate text using Lingva public API instances."""

        if not text or not text.strip():
            raise ValueError("Text cannot be empty.")

        if not source or not target:
            raise ValueError(
                "Source and target languages are required."
            )

        if source == target:
            return text

        encoded_text = quote(text.strip(), safe="")

        last_error = None

        for api_template in TranslationService.API_URLS:

            api_url = api_template.format(
                source=source,
                target=target,
                text=encoded_text
            )

            try:
                response = requests.get(
                    api_url,
                    headers={
                        "User-Agent": "LinguaAI/1.0",
                        "Accept": "application/json"
                    },
                    timeout=15
                )

                response.raise_for_status()

                # Make sure the server actually returned JSON.
                content_type = response.headers.get(
                    "Content-Type",
                    ""
                ).lower()

                if "json" not in content_type:
                    last_error = (
                        f"Non-JSON response from {api_url}"
                    )
                    continue

                data = response.json()

                if "error" in data:
                    last_error = data["error"]
                    continue

                translated_text = data.get("translation")

                if translated_text:
                    return translated_text.strip()

                last_error = "No translation returned."

            except requests.RequestException as error:

                last_error = str(error)
                continue

            except ValueError as error:

                last_error = str(error)
                continue

        print(
            "Translation services failed:",
            last_error
        )

        raise RuntimeError(
            "Translation service is currently unavailable."
        )
