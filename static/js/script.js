async function translateText() {

    const inputText =
        document.getElementById("inputText").value.trim();

    const sourceLanguage =
        document.getElementById("sourceLanguage").value;

    const targetLanguage =
        document.getElementById("targetLanguage").value;

    const outputText =
        document.getElementById("outputText");

    const status =
        document.getElementById("status");

    const translateBtn =
        document.getElementById("translateBtn");


    // Check empty input
    if (!inputText) {

        outputText.value = "";

        status.textContent =
            "⚠️ Please enter some text to translate.";

        return;
    }


    // Check same language
    if (sourceLanguage === targetLanguage) {

        outputText.value = inputText;

        status.textContent =
            "ℹ️ Source and target languages are the same.";

        return;
    }


    // Loading state
    translateBtn.disabled = true;

    translateBtn.textContent =
        "⏳ Translating...";

    status.textContent =
        "Translating...";

    outputText.value = "";


    try {

        const response = await fetch("/api/translate", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                text: inputText,

                source: sourceLanguage,

                target: targetLanguage

            })

        });


        const data = await response.json();


        // Handle API error
        if (!response.ok || !data.success) {

            throw new Error(
                data.error || "Translation failed."
            );
        }


        // Display translation
        outputText.value =
            data.translation;

        status.textContent =
            "✅ Translation completed successfully!";


    } catch (error) {

        console.error(
            "Translation Error:",
            error
        );

        outputText.value = "";

        status.textContent =
            "❌ " +
            (
                error.message ||
                "Unable to connect to the translation server."
            );

    } finally {

        translateBtn.disabled = false;

        translateBtn.textContent =
            "🔄 Translate";
    }
}


/* =========================================
   COPY TRANSLATION
========================================= */

async function copyTranslation() {

    const outputText =
        document.getElementById("outputText");

    const status =
        document.getElementById("status");


    if (!outputText.value.trim()) {

        status.textContent =
            "⚠️ Nothing to copy.";

        return;
    }


    try {

        await navigator.clipboard.writeText(
            outputText.value
        );

        status.textContent =
            "✅ Translation copied to clipboard!";


    } catch (error) {

        console.error(
            "Copy Error:",
            error
        );

        status.textContent =
            "❌ Unable to copy translation.";
    }
}


/* =========================================
   CLEAR
========================================= */

function clearText() {

    document.getElementById("inputText").value = "";

    document.getElementById("outputText").value = "";

    document.getElementById("status").textContent = "";

    document.getElementById("charCount").textContent = "0";
}


/* =========================================
   SWAP LANGUAGES
========================================= */

function swapLanguages() {

    const sourceLanguage =
        document.getElementById("sourceLanguage");

    const targetLanguage =
        document.getElementById("targetLanguage");

    const inputText =
        document.getElementById("inputText");

    const outputText =
        document.getElementById("outputText");

    const status =
        document.getElementById("status");


    // Swap languages
    const temporaryLanguage =
        sourceLanguage.value;

    sourceLanguage.value =
        targetLanguage.value;

    targetLanguage.value =
        temporaryLanguage;


    // Swap text
    const temporaryText =
        inputText.value;

    inputText.value =
        outputText.value;

    outputText.value =
        temporaryText;


    // Update character count
    document.getElementById("charCount").textContent =
        inputText.value.length;


    status.textContent =
        "🔄 Languages swapped successfully.";
}


/* =========================================
   CTRL + ENTER TRANSLATION
========================================= */

document
    .getElementById("inputText")
    .addEventListener("keydown", function (event) {

        if (event.ctrlKey && event.key === "Enter") {

            translateText();
        }
    });


/* =========================================
   CHARACTER COUNTER
========================================= */

const inputText =
    document.getElementById("inputText");

const charCount =
    document.getElementById("charCount");


inputText.addEventListener("input", function () {

    charCount.textContent =
        inputText.value.length;

});
