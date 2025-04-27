from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()

    # Supported image file extensions
    valid_extensions = ('.jpg', '.jpeg', '.png')

    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for filename in in_files:
       
        # Skip files that don't match valid image extensions
        if filename.lower().endswith(valid_extensions):
            # Remove file extension and split on non-alphabetic characters
            pet_label = " ".join([word for word in filename.lower().replace('.jpg', '').replace('.jpeg', '').replace('.png', '').split('_') if word.isalpha()])

            # If filename doesn't already exist in dictionary, add it and its
            # pet label - otherwise print an error message indicating duplicate
            if filename not in results_dic:
                results_dic[filename] = [pet_label.strip()]
            else:
                print("** Warning: Duplicate files exist in directory:", filename)
                
    # Return the results_dic dictionary with filenames as keys and pet labels as values
    return results_dic

if __name__ == "__main__":
    import argparse

    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description="Extract pet labels from image filenames.")

    # Add argument for the image directory
    parser.add_argument('dir', type=str, help='Path to the folder of pet images')

    # Parse command-line arguments
    args = parser.parse_args()

    # Call the get_pet_labels function with the directory argument
    results = get_pet_labels(args.dir)

    # Print the results
    print(results)
