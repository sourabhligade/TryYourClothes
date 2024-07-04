# TryYourClothes.com

## Overview
TryYourClothes.com is a web application that allows users to virtually try on clothes. Users can upload their own photos and clothing images to see how they look together.

<img width="1440" alt="readme1" src="https://github.com/sourabhligade/TryYourClothes/assets/65074119/4ca76865-9ea8-4599-96bc-f8857b913bed">
<img width="1440" alt="readme2" src="https://github.com/sourabhligade/TryYourClothes/assets/65074119/70ccab46-c93b-4350-a6ff-3d5b905897d3">



## Setup

### Prerequisites
- Python 3.x
- Node.js and npm (for the frontend)
- Django
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sourabhligade/TryYourClothes.git
    ```

2. Navigate to the project directory:
    ```sh
    cd tryyourclothes
    ```

3. Install backend dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Install frontend dependencies:
    ```sh
    cd api/src
    npm install
    cd ../..
    ```

5. Run database migrations:
    ```sh
    python manage.py migrate
    ```

6. Start the Django development server:
    ```sh
    python manage.py runserver
    ```

7. Start the React development server:
    ```sh
    cd api/src
    npm start
    cd ../..
    ```

## Usage

1. Open your web browser and go to `http://localhost:3000`.
2. Upload your photo and a clothing photo.
3. Click "Try On" to see the result.

## Integrating DeepFashion

### Backend

1. Clone the DeepFashion repository:
    ```sh
    git clone https://github.com/sourabhligade/TryYourClothes.git
    ```

2. Follow the instructions in the DeepFashion repository to set up the model.

3. Update `virtualtryon/views.py` to integrate DeepFashion API for image processing.

### Frontend

1. Ensure the frontend correctly sends images to the backend and displays results returned by the DeepFashion model.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgements

- DeepFashion Team for their model and dataset.

