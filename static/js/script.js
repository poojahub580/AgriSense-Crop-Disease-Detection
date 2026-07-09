document.addEventListener("DOMContentLoaded", () => {

    // ===============================
    // Progress Bar Animation
    // ===============================

    const progressBar = document.querySelector(".progress-bar");

    if (progressBar) {

        const finalWidth = progressBar.dataset.width;

        progressBar.style.width = "0%";

        setTimeout(() => {

            progressBar.style.width = finalWidth;

        }, 300);

    }

    // ===============================
    // Fade Animation
    // ===============================

    const sections = document.querySelectorAll(".section");

    sections.forEach((section, index) => {

        section.style.opacity = "0";
        section.style.transform = "translateY(25px)";

        setTimeout(() => {

            section.style.transition = "0.6s";
            section.style.opacity = "1";
            section.style.transform = "translateY(0px)";

        }, index * 150);

    });

    // ===============================
    // Button Hover Animation
    // ===============================

    document.querySelectorAll("button").forEach(button => {

        button.addEventListener("mouseenter", () => {

            button.style.transform = "scale(1.03)";

        });

        button.addEventListener("mouseleave", () => {

            button.style.transform = "scale(1)";

        });

    });

    // ===============================
    // Image Preview
    // ===============================

    const fileInput = document.getElementById("fileInput");
    const previewImage = document.getElementById("previewImage");
    const fileName = document.getElementById("fileName");
    const removeButton = document.getElementById("removeImage");

    if (fileInput && previewImage && fileName && removeButton) {

        fileInput.addEventListener("change", function () {

            const file = this.files[0];

            if (file) {

                fileName.textContent = "Selected File: " + file.name;

                const reader = new FileReader();

                reader.onload = function (event) {

                    previewImage.src = event.target.result;
                    previewImage.style.display = "block";
                    removeButton.style.display = "inline-block";

                };

                reader.readAsDataURL(file);

            }

        });

        removeButton.addEventListener("click", function () {

            fileInput.value = "";

            previewImage.src = "";
            previewImage.style.display = "none";

            removeButton.style.display = "none";

            fileName.textContent = "No image selected";

        });

    }

    // ===============================
    // Loading Animation
    // ===============================

    const form = document.getElementById("predictionForm");
    const predictButton = document.getElementById("predictButton");
    const loadingContainer = document.getElementById("loadingContainer");

    if (form && predictButton && loadingContainer) {

        form.addEventListener("submit", function () {

            predictButton.disabled = true;

            predictButton.innerHTML = "Analyzing Image...";

            loadingContainer.style.display = "block";

        });

    }

});