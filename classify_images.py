import os
from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. 
    """
    # Iterate through all files in the results_dic to classify them
    for key in results_dic:
        
        # 3a. Get the full path of the image file
        image_path = os.path.join(images_dir, key)
        
        # Run the classifier function with the image path and model to get the classifier label
        # classifier() function takes in the image path and model type, and returns the model label
        model_label = classifier(image_path, model)

        # 3b. Process the classifier label
        # Convert to lowercase and remove leading/trailing whitespace
        model_label = model_label.lower().strip()
        
        # 3c. Check if the pet label is in the classifier label
        # Get the true label (pet image label) from the results_dic
        truth = results_dic[key][0].lower().strip()

        # If the pet label is in the classifier label, mark it as a match
        if truth in model_label:
            # If there's a match, add model_label and 1 to the results_dic[key] list
            results_dic[key].extend([model_label, 1])
        else:
            # If there's no match, add model_label and 0 to the results_dic[key] list
            results_dic[key].extend([model_label, 0])

        # Optional: Debugging output to monitor what is happening
        print(f"Image: {key}")
        print(f"  Pet Label: {truth}")
        print(f"  Classifier Label: {model_label}")
        print(f"  Match: {results_dic[key][2]}\n")

# Example usage
if __name__ == "__main__":
    import argparse

    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description="Classify pet images using a CNN model.")

    # Add argument for the image directory
    parser.add_argument('dir', type=str, help='Path to the folder of pet images')

    # Add argument for the CNN model architecture
    parser.add_argument('--arch', type=str, default='vgg', choices=['resnet', 'alexnet', 'vgg'],
                        help='The CNN model architecture to use for classification')

    # Parse command-line arguments
    args = parser.parse_args()

    # Example results_dic to simulate the input
    results_dic = {
        'Great_pyrenees_05367.jpg': ['great pyrenees'],

    }

    # Call the classify_images function with the test data
    classify_images(args.dir, results_dic, args.arch)

    # Print the updated results_dic to check the results
    for key in results_dic:
        print(f"Filename: {key}")
        print(f"  Pet Label: {results_dic[key][0]}")
        print(f"  Classifier Label: {results_dic[key][1]}")
        print(f"  Match: {results_dic[key][2]}")
    print(results_dic)
