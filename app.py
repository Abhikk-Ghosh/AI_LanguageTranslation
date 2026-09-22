from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from services.translator import TranslationService


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/translate", methods=["POST"])
def translate():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "error": "Invalid request."
            }), 400

        text = data.get("text", "").strip()
        source = data.get("source", "").strip()
        target = data.get("target", "").strip()

        if not text:
            return jsonify({
                "success": False,
                "error": "Please enter text to translate."
            }), 400

        if not source or not target:
            return jsonify({
                "success": False,
                "error": "Please select source and target languages."
            }), 400

        translated_text = TranslationService.translate(
            text,
            source,
            target
        )

        return jsonify({
            "success": True,
            "translation": translated_text
        })

    except ValueError as error:

        return jsonify({
            "success": False,
            "error": str(error)
        }), 400

    except Exception as error:

        print("Translation Error:", error)

        return jsonify({
            "success": False,
            "error": "Translation service is currently unavailable."
        }), 500


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )