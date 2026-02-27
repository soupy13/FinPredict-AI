// Inside form.addEventListener('submit', function(e) { ... })

fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(features)
})
.then(response => response.json())
.then(data => {
    if(data.success) {
        displayResult(data.isApproved, data.factors, features.Gender, features.Married);
    } else {
        alert("Error making prediction: " + data.error);
    }
    loadingState.classList.add('hidden');
    submitBtn.classList.remove('hidden');
})
.catch(err => {
    console.error("Backend Error:", err);
    loadingState.classList.add('hidden');
    submitBtn.classList.remove('hidden');
});