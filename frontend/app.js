const API_URL =
    "http://127.0.0.1:8000/predict";


const imageInput =
    document.getElementById(
        "imageInput"
    );


const preview =
    document.getElementById(
        "preview"
    );


const previewContainer =
    document.getElementById(
        "previewContainer"
    );


const fileName =
    document.getElementById(
        "fileName"
    );


const predictButton =
    document.getElementById(
        "predictButton"
    );


const loading =
    document.getElementById(
        "loading"
    );


const result =
    document.getElementById(
        "result"
    );


const prediction =
    document.getElementById(
        "prediction"
    );


const confidence =
    document.getElementById(
        "confidence"
    );


const error =
    document.getElementById(
        "error"
    );


// ======================================
// Image selection
// ======================================

imageInput.addEventListener(
    "change",
    function () {

        const file =
            imageInput.files[0];


        if (!file) {

            return;

        }


        // File name

        fileName.textContent =
            file.name;


        // Image preview

        const imageURL =
            URL.createObjectURL(
                file
            );


        preview.src =
            imageURL;


        previewContainer
            .classList
            .remove("hidden");


        // Enable prediction

        predictButton.disabled =
            false;


        // Reset result

        result
            .classList
            .add("hidden");


        error
            .classList
            .add("hidden");

    }
);


// ======================================
// Prediction
// ======================================

predictButton.addEventListener(
    "click",
    async function () {

        const file =
            imageInput.files[0];


        if (!file) {

            showError(
                "Please select an image."
            );

            return;

        }


        // Hide previous results

        result
            .classList
            .add("hidden");


        error
            .classList
            .add("hidden");


        // Show loading

        loading
            .classList
            .remove("hidden");


        predictButton.disabled =
            true;


        try {

            // ==================================
            // Create FormData
            // ==================================

            const formData =
                new FormData();


            formData.append(
                "file",
                file
            );


            // ==================================
            // Send request to FastAPI
            // ==================================

            const response =
                await fetch(
                    API_URL,
                    {
                        method: "POST",
                        body: formData
                    }
                );


            // ==================================
            // Check response
            // ==================================

            if (!response.ok) {

                throw new Error(
                    `API Error: ${response.status}`
                );

            }


            // ==================================
            // Convert response to JSON
            // ==================================

            const data =
                await response.json();


            console.log(
                "API Response:",
                data
            );


            // ==================================
            // Display prediction
            // ==================================

            prediction.textContent =
                data.prediction;


            confidence.textContent =
                (
                    data.confidence * 100
                ).toFixed(2) + "%";


            result
                .classList
                .remove("hidden");


        }

        catch (err) {

            console.error(
                err
            );


            showError(
                "Could not connect to the AI API. " +
                "Make sure FastAPI is running."
            );

        }

        finally {

            loading
                .classList
                .add("hidden");


            predictButton.disabled =
                false;

        }

    }
);


// ======================================
// Error function
// ======================================

function showError(message) {

    error.textContent =
        message;

    error
        .classList
        .remove("hidden");

}