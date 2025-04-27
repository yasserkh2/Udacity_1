# Pre-trained Image Classifier for Dog Breed Identification

This project uses pre-trained CNN models to classify dog breeds in images. It compares the performance of three different architectures: VGG, ResNet, and AlexNet.

## Project Overview

The classifier can:
- Identify dog breeds from images
- Distinguish between dogs and non-dogs
- Compare accuracy across different CNN architectures
- Process both individual images and batch directories

## Model Performance Comparison

Based on testing with 40 images (30 dogs, 10 non-dogs):

### VGG (Best Performance)
- Overall Accuracy: 87.50%
- Dog Detection: 100%
- Not-Dog Detection: 100%
- Breed Classification: 93.33%

### ResNet
- Overall Accuracy: 82.50%
- Dog Detection: 100%
- Not-Dog Detection: 90%
- Breed Classification: 90%

### AlexNet
- Overall Accuracy: 75.00%
- Dog Detection: 100%
- Not-Dog Detection: 100%
- Breed Classification: 80%

## Requirements

All required dependencies are listed in `requirements.txt`. The main requirements are:
- Python 3.x
- PyTorch >= 2.7.0
- torchvision >= 0.22.0
- PIL (Python Imaging Library) >= 10.4.0

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Pre-trained-Image-Classifier-to-Identify-Dog-Breeds
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
source venv/Scripts/activate  # For Git Bash
# OR
venv\Scripts\activate.bat     # For Command Prompt

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Note: The first run will take longer as it downloads the model weights for VGG, ResNet, and AlexNet.

## Usage

Basic command structure:
```bash
python check_images.py --dir [image_directory] --arch [model_architecture] --dogfile dognames.txt
```

### Testing with Different Models

1. Testing with VGG (Best accuracy):
```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```
Expected results:
- Match: ~87.5%
- Correct dogs: 100%
- Correct breed: ~93.3%
- Correct not-dogs: 100%
- Runtime: ~8 seconds

2. Testing with ResNet (Balanced performance):
```bash
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt
```
Expected results:
- Match: ~82.5%
- Correct dogs: 100%
- Correct breed: ~90.0%
- Correct not-dogs: 90%
- Runtime: ~2 seconds

3. Testing with AlexNet (Fastest):
```bash
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt
```
Expected results:
- Match: ~75.0%
- Correct dogs: 100%
- Correct breed: ~80.0%
- Correct not-dogs: 100%
- Runtime: ~1 second

### Testing with Your Own Images

To test with your own images:
1. Place your images in the uploaded_images/ directory
2. Run any of the above commands, replacing pet_images/ with uploaded_images/
```bash
python check_images.py --dir uploaded_images/ --arch vgg --dogfile dognames.txt
```

Parameters:
- `--dir`: Directory containing images to classify (pet_images/ or uploaded_images/)
- `--arch`: Model architecture to use (vgg, resnet, or alexnet)
- `--dogfile`: File containing valid dog names (dognames.txt)

Note: The first run for each model will take longer as it downloads the model weights.

## Project Structure

- `check_images.py`: Main script that runs the classification
- `classifier.py`: Contains the pre-trained model implementations
- `get_pet_labels.py`: Extracts labels from image filenames
- `classify_images.py`: Classifies images using the selected model
- `adjust_results4_isadog.py`: Adjusts results based on dog/not-dog classification
- `calculates_results_stats.py`: Calculates classification statistics
- `print_results.py`: Formats and displays results

## Common Classification Challenges

1. Similar Breed Confusion:
   - Beagle vs. various hounds
   - Great Pyrenees vs. Kuvasz

2. Breed-Specific Accuracy:
   - Most accurate: German Shepherd, Saint Bernard
   - Most challenging: Beagle, Great Pyrenees

## Best Practices

1. Image Quality:
   - Use clear, well-lit images
   - Center the subject in the frame
   - Minimize background distractions

2. Model Selection:
   - Use VGG for highest overall accuracy
   - Use ResNet for balance of speed and accuracy
   - Use AlexNet for fastest processing

## Results

This project had two main objectives:
1. Identifying which pet images are of dogs and which aren't
2. Classifying the breeds of dogs for the images that are of dogs

### Results Table

| CNN Model Architecture | % Match | % Correct Dogs | % Correct Breed | % Correct Not-Dogs | Time (seconds) |
|----------------------|---------|----------------|-----------------|-------------------|----------------|
| VGG                  | 87.5%   | 100%          | 93.3%          | 100%             | 8              |
| ResNet              | 82.5%   | 100%          | 90.0%          | 90%              | 2              |
| AlexNet             | 75.0%   | 100%          | 80.0%          | 100%             | 1              |

### Analysis

1. Dog vs Non-Dog Classification:
   - Both VGG and AlexNet achieved 100% accuracy in distinguishing dogs from non-dogs
   - ResNet had one misclassification (identified a cat as a dog)

2. Breed Classification:
   - VGG performed best with 93.3% accuracy
   - ResNet followed with 90.0% accuracy
   - AlexNet had the lowest accuracy at 80.0%

3. Processing Time:
   - AlexNet was fastest (1 second)
   - ResNet was moderately fast (2 seconds)
   - VGG took longest (8 seconds)

### Best Model Architecture

VGG emerged as the best model architecture because:
- Perfect accuracy (100%) in distinguishing dogs from non-dogs
- Highest breed classification accuracy (93.3%)
- Most reliable overall performance despite longer processing time

The trade-off for VGG's superior accuracy is longer processing time, while AlexNet offers faster processing but lower accuracy. ResNet provides a middle ground but occasionally misclassifies non-dogs as dogs.

## Contributing

Feel free to submit issues and enhancement requests!
