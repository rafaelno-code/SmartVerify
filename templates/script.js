document.getElementById("uploadBtn").addEventListener("click", function() { 
    document.getElementById("imageInput").click();
});

document.getElementById("imageInput").addEventListener("change", function(event) { 
    const file = event.target.files[0];

    if (!file) return;

    const reader = new FileReader();

    reader.onload = function(e) {
        document.getElementById("imagePreview").src = e.target.result;
        document.getElementById("imagePreview").style.display = "block";
    };

    reader.readAsDataURL(file);

    predict(file); 
});


function predict(file) {
    if (!file) {
        alert("Please select an image first.");
        return;
    }

    const formData = new FormData();
    formData.append('image', file);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultText').textContent = `Prediction: ${data.class} (Confidence: ${data.confidence.toFixed(2)})`;
        document.body.style.overflow = "hidden";  // Lock scrolling
        document.getElementById("resultSection").style.display = "block"; // Show results
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('resultText').textContent = 'An error occurred while processing the image.';
        document.getElementById("resultSection").style.display = "block";
    });
}

document.getElementById("backBtn").addEventListener("click", function() {
    document.body.style.overflow = "auto"; // Unlock scrolling
    document.getElementById("resultSection").style.display = "none"; // Hide results
    document.getElementById("imagePreview").style.display = "none"; // Hide image preview
    document.getElementById('resultText').textContent = ""; // Clear result text
});
