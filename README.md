# Format Flip - Flask Image Editing Webpage

Welcome to Format Flip, a Flask-based image editing webpage that allows you to easily convert images between different formats and apply grayscale transformations. This web application supports various image formats, including 'png', 'webp', 'jpg', 'jpeg', and 'gif'.

## Features

1. **Format Conversion:** Convert images from one format to another seamlessly.
   - Supported Formats: 'png', 'webp', 'jpg', 'jpeg', 'gif'

2. **Grayscale Transformation:** Apply grayscale transformation to images for a monochromatic effect.

## Getting Started

Follow these instructions to set up and run the Format Flip web application on your local machine.

### Prerequisites

Before you begin, ensure that you have the following software installed on your machine:

- [Python](https://www.python.org/downloads/): The project is built using Python.
- [Git](https://git-scm.com/): Version control system to clone the repository.

### Clone the Repository

1. Open your terminal or command prompt.

2. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Ammar-h22/format-flip.git
    ```

### Navigate to the Project Directory

1. Change into the project directory:

    ```bash
    cd Format-Flip
    ```

### Set Up a Virtual Environment (Optional but recommended)

1. Create a virtual environment to isolate project dependencies:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

### Install Dependencies

1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Set the Flask app:

    - On Windows:

        ```bash
        set FLASK_APP=app.py
        ```

    - On macOS/Linux:

        ```bash
        export FLASK_APP=app.py
        ```

2. Run the Flask app:

    ```bash
    flask run
    ```

3. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the Format Flip web application.

## Usage

1. Upload an image file of supported formats.
2. Choose the desired output format or apply grayscale transformation.
3. Click the "Convert" button to process the image.
4. Download the converted image.

### Contributing

If you'd like to contribute to Format Flip, please fork the repository and create a pull request. Any contributions are welcome!
