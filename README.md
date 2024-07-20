# Image Classification Using CNN 

## Overview

The Shoe Image Classification project aims to classify images of shoes into six predefined categories using a pre-trained EfficientNet model and custom CNN vanila architecture. The project includes data preprocessing, model training, evaluation, and deployment via a FastAPI application.

## Table of Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [Key Features](#key-features)
- [Use Cases](#use-cases)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Testing](#testing)
- [Contributing](#contributing)

## Purpose

The main objective of this project is to provide accurate image classification using a pre-trained EfficientNet model. It categorizes images into six distinct classes: Boots, Sneakers, Flip Flops, Loafers, Sandals, and Soccer Shoes.

## Key Features
- **Data Preprocessing:** Organizes and preprocesses the dataset, including image resizing and normalization.
- **Model Training:** Fine-tunes a pre-trained EfficientNet model on the shoe dataset.
- **Model Evaluation:** Assesses model performance using appropriate metrics.
- **Deployment:** Implements a FastAPI application for easy image classification.

## Use Cases
- **Shoe Classification:** Categorize images of shoes into predefined classes for various applications.
- **Content Analysis:** Analyze and classify shoe images for e-commerce, inventory management, and visual search.
- **Educational Purposes:** Serve as a learning tool for understanding transfer learning and EfficientNet in image classification.

## Technology Stack
- **Python:** Core programming language for the project.
- **TensorFlow & TensorFlow Hub:** Libraries for implementing and fine-tuning the EfficientNet model.
- **FastAPI:** Web framework for deploying the image classification model.
- **NumPy & Pandas:** Libraries for data manipulation and preprocessing.
- **OpenCV:** Library for image processing.

## Getting Started

### Requirements
Please refer to the [installation](https://github.com/itsguptaaman/image_classification_using_cnn/blob/main/installation.md) file for detailed installation instructions.

### Running the FastAPI Application

#### 1. Start the FastAPI server
```bash
uvicorn main:app --reload
```
### 2. Access the web interface
Open your browser and go to http://127.0.0.1:8000/docs to interact with the FastAPI application.

## Testing
Sample images for testing the model are provided in the test_images directory. Use these images to validate the model's performance via the FastAPI application.

## Sample Testing
To test the model, you can use the /predict endpoint by uploading images through the FastAPI web interface or using a tool like curl or Postman.
![Capture](https://github.com/user-attachments/assets/8fd4b1e6-bf98-401c-88cb-21c41c0bef03)

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your enhancements.
