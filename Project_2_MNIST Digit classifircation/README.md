# MNIST Handwritten Digit Classification Using a Neural Network

## Overview

This project implements a handwritten digit classification system using the **MNIST dataset** and a fully connected neural network built with **TensorFlow/Keras**.

The notebook:
- Loads MNIST through `keras.datasets.mnist`.
- Uses 60,000 training images and 10,000 test images.
- Works with grayscale images of size **28 × 28 pixels**.
- Scales pixel values by dividing by 255.
- Builds a Keras Sequential neural network with two hidden Dense layers.
- Trains the model for **10 epochs** using the Adam optimizer.
- Evaluates the model on unseen test data.
- Generates predictions and a confusion matrix.
- Includes a predictive system that accepts an image path, converts the image to grayscale, resizes it to 28 × 28, normalizes it, and predicts the digit.

## Results

| Metric | Result |
|---|---:|
| Training images | 60,000 |
| Test images | 10,000 |
| Image size | 28 × 28 |
| Number of classes | 10 (digits 0–9) |
| Training epochs | 10 |
| Final training accuracy reported in notebook | **99.16%** |
| Test accuracy | **97.04%** (reported as 97.1% in notebook text) |
| Sample external-image prediction | **3** |

The supplied `3-digit.PNG` sample is processed by the predictive system and is classified as **3** in the notebook.

## Model Architecture

The notebook defines the following network:

```text
Input image: 28 × 28
        │
        ▼
Flatten
        │
        ▼
Dense(50, activation="relu")
        │
        ▼
Dense(50, activation="relu")
        │
        ▼
Dense(10, activation="sigmoid")
        │
        ▼
Predicted class scores for digits 0–9
```

The notebook compiles the model with:
- **Optimizer:** Adam
- **Loss:** sparse categorical crossentropy
- **Metric:** accuracy

> Note: This README documents the architecture exactly as implemented in the supplied notebook. The final layer uses sigmoid, rather than changing the implementation to another activation.

## Dataset

The project uses the MNIST handwritten digit dataset provided by Keras.

- Training set: `X_train` shape `(60000, 28, 28)`
- Training labels: `Y_train` shape `(60000,)`
- Test set: `X_test` shape `(10000, 28, 28)`
- Test labels: `Y_test` shape `(10000,)`
- Labels range from **0 to 9**.

## Preprocessing

The notebook performs the following preprocessing:

1. Load MNIST.
2. Confirm the image dimensions.
3. Scale pixel intensities:
   ```python
   X_train = X_train / 255
   X_test = X_test / 255
   ```
4. For a user-supplied image:
   - Read the image with OpenCV.
   - Convert it to grayscale.
   - Resize it to 28 × 28.
   - Divide pixel values by 255.
   - Reshape it to `(1, 28, 28)` before prediction.

## Training

The model is trained with:

```python
model.fit(X_train, Y_train, epochs=10)
```

Training accuracy increases from approximately **85.14%** in epoch 1 to **99.16%** in epoch 10, while training loss decreases from **0.5167** to **0.0282**.

## Evaluation

The notebook evaluates the model with:

```python
loss, accuracy = model.evaluate(X_test, Y_test)
```

The recorded test accuracy is approximately **97.04%**.

A 10 × 10 confusion matrix is also generated to inspect class-level prediction performance.

## Predictive System

The notebook includes a reusable prediction flow:

```python
input_image = cv2.imread(input_image_path)
grayscale = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)
input_image_resize = cv2.resize(grayscale, (28, 28))
input_image_resize = input_image_resize / 255
image_reshaped = np.reshape(input_image_resize, [1, 28, 28])

input_prediction = model.predict(image_reshaped)
input_pred_label = np.argmax(input_prediction)
```

The supplied sample image is recognized as digit **3**.

## Technologies Used

- Python
- NumPy
- Matplotlib
- Seaborn
- OpenCV (`cv2`)
- PIL
- TensorFlow / Keras
- Google Colab utilities used in the notebook

## Running the Project

### Recommended: Google Colab

The notebook uses Google Colab-specific functionality such as `cv2_imshow`, `/content/...` paths, and Google Drive mounting.

1. Open the `.ipynb` file in Google Colab.
2. Run the cells from top to bottom.
3. Allow MNIST to download when prompted.
4. For the predictive system, provide the path to a digit image.

### Local Python environment

Install the main dependencies:

```bash
pip install numpy matplotlib seaborn opencv-python pillow tensorflow
```

Then open the notebook in Jupyter or another compatible notebook environment. Some Colab-specific commands may need to be replaced when running locally.

## Project Structure

```text
MNIST_Digit_Classification/
├── MNIST_Digit_classification_using_Neural_Networks.ipynb
├── 3-digit.PNG
├── README.md
├── Project_Documentation.docx
└── MNIST_Digit_Classification_Presentation.pptx
```

## Limitations

- The project is designed around MNIST-style 28 × 28 grayscale digits.
- A user-supplied image may not behave like an MNIST image if its background, stroke thickness, orientation, cropping, or contrast differs significantly.
- The predictive system performs resizing and normalization but does not include a more advanced segmentation/alignment pipeline.
- The notebook is primarily structured for Google Colab.

## Future Scope

Possible improvements include:
- Replacing the dense network with a CNN for stronger image-feature extraction.
- Adding a small web interface for image upload and prediction.
- Saving/loading the trained model instead of retraining every session.
- Adding preprocessing for centering and foreground/background normalization.
- Reporting precision, recall, and F1-score per digit.
- Packaging the model as an API or lightweight desktop/web application.

## Author

**Project:** MNIST Handwritten Digit Classification Using Neural Networks  
**Implementation:** Python + TensorFlow/Keras

