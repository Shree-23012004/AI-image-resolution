async function uploadImage() {
    const formData = new FormData(document.getElementById('uploadForm'));
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    const blob = await response.blob();
    const imgUrl = URL.createObjectURL(blob);
    document.getElementById('enhancedImage').src = imgUrl;
}

