document.querySelector("#input-buttons button").addEventListener("click", predict);

function predict() {
    const imageInput = document.getElementById('imageInput');//can change name
    const file = imageInput.files[0];

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
        //can change name
        document.getElementById('result').textContent = `Prediction: ${data.class} (Confidence: ${data.confidence.toFixed(2)})`;
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'An error occurred while processing the image.';
    });
}
