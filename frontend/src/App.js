import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleFileUpload = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);

      try {
        const response = await axios.post('http://localhost:8000/api/upload/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        alert(response.data.message);
        console.log(response.data.file_path); // You can check the file path here
      } catch (error) {
        console.error('Error uploading file:', error);
        alert('Failed to upload file');
      }
    } else {
      alert('No file selected');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1 className="main-title">
          Virtual Try On Only on 
          <br />
          <span className="highlight-url">TryYourClothes.com</span>
        </h1>
        <p className="tagline">
          Snap a Pic, Choose an Outfit, 
          <br />
          <span className="highlight">Get a Virtual Fitting in Seconds!</span>
        </p>
        <button className="cta-button">Get Started</button>
        <p className="discount-banner">
          Bringing Fitting Rooms to Your Home
        </p>
        <div className="upload-section">
          <input type="file" id="file-upload" onChange={handleFileChange} />
          <label htmlFor="file-upload" className="upload-button">Choose File</label>
          <button className="upload-button" onClick={handleFileUpload}>Upload Photo</button>
        </div>
      </header>
    </div>
  );
}

export default App;
