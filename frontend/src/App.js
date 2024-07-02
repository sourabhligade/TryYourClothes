// App.js

import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [userPhoto, setUserPhoto] = useState(null);
  const [clothingPhoto, setClothingPhoto] = useState(null);

  const handleUserPhotoChange = (event) => {
    setUserPhoto(event.target.files[0]);
  };

  const handleClothingPhotoChange = (event) => {
    setClothingPhoto(event.target.files[0]);
  };

  const handleFileUpload = async () => {
    if (userPhoto && clothingPhoto) {
      const formData = new FormData();
      formData.append('user_photo', userPhoto);
      formData.append('clothing_photo', clothingPhoto);

      try {
        const response = await axios.post('http://localhost:8000/api/upload/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        alert(response.data.message);
      } catch (error) {
        console.error('Error uploading file:', error);
        alert('Failed to upload file');
      }
    } else {
      alert('Please select both photos.');
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
        
        {/* How Does It Work Section */}
        <section className="how-it-works">
          <h2 className="section-header">How Does It Work?</h2>
          <p className="how-it-works-description">
            Upload your photo, select a clothing item, and see how it looks on you instantly!
          </p>
        </section>

        {/* Example images with explanations */}
        <div className="example-images">
          <div className="example-image-container">
            <img src="http://localhost:8000/media/example_images/real_girl.png" alt="Real Girl Example" className="example-image" />
            <p className="image-description">Your Photo</p>
          </div>
          <div className="plug-sign">&#10148;</div>
          <div className="example-image-container">
            <img src="http://localhost:8000/media/example_images/avatar_clothing.png" alt="Avatar with Clothing Example" className="example-image" />
            <p className="image-description">Clothing Photo</p>
          </div>
          <div className="arrow-sign">&#8594;</div>
          <div className="example-image-container">
            <img src="http://localhost:8000/media/example_images/result_image.png" alt="Result  Example" className="example-image bold-image" />
            <p className="image-description">Result Image</p>
          </div>
        </div>

        {/* File upload section */}
        <div className="upload-section">
          <label htmlFor="user-photo-upload" className="upload-button">Choose Your Photo</label>
          <input type="file" id="user-photo-upload" onChange={handleUserPhotoChange} style={{ display: 'none' }} />
          <label htmlFor="user-photo-upload" className="choose-file-button">Choose File</label>
          <label htmlFor="clothing-photo-upload" className="upload-button">Choose Clothing Photo</label>
          <input type="file" id="clothing-photo-upload" onChange={handleClothingPhotoChange} style={{ display: 'none' }} />
          <label htmlFor="clothing-photo-upload" className="choose-file-button">Choose File</label>
          <button className="upload-button" onClick={handleFileUpload}>Try On</button>
        </div>
      </header>
    </div>
  );
}

export default App;
