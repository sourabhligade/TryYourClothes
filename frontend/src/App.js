import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!selectedFile) {
      alert('Please select a file.');
      return;
    }
    const formData = new FormData();
    formData.append('file', selectedFile);

    // Here, you would typically make a POST request to your backend API
    // using fetch or Axios to handle the file upload.
    // Example using fetch:
    fetch('http://localhost:8000/api/upload/', {
      method: 'POST',
      body: formData,
    })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        alert('File uploaded successfully!');
        setSelectedFile(null); // Reset selected file state
      })
      .catch(error => {
        console.error('Error:', error);
        alert('Error uploading file.');
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Virtual Try On Only on TryYourClothes.com</h1>
        <p>Upload your photo to try on clothes.</p>
        <form onSubmit={handleSubmit}>
          <input type="file" onChange={handleFileChange} accept="image/*" />
          <button type="submit">Upload</button>
        </form>
      </header>
    </div>
  );
}

export default App;
