def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if the classifier correctly 
    classified images 'as a dog' or 'not a dog', especially when not a match.
    Demonstrates if model architecture correctly classifies dog images even if
    it gets the breed wrong (not a match).
    
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifier labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog.
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    
    dogfile - A text file that contains names of all dogs from the classifier
              function and pet image files. This file has one dog name per line. 
              Dog names are all in lowercase with spaces separating the distinct 
              words of the dog name. (string - indicates text file's filename)
    
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    # Creates dognames list for quick matching to results_dic labels
    dognames_list = []

    # Reads in dognames from file, one name per line, & automatically closes file
    with open(dogfile, "r") as infile:
        # Reads in each line in the file and processes it
        for line in infile:
            # Remove any whitespace characters, like newline, and convert to lowercase
            line = line.strip().lower()
            
            # Add dogname to list if it doesn't already exist
            if line not in dognames_list:
                dognames_list.append(line)
            else:
                print(f"** Warning: Duplicate dog name '{line}' found in {dogfile}")

    # Add whether pet labels & classifier labels are dogs by appending
    # two items to the end of value(List) in results_dic.
    # List Index 3 = whether (1) or not (0) Pet Image Label is a dog
    # List Index 4 = whether (1) or not (0) Classifier Label is a dog
    for key in results_dic:
        # Normalize pet label to lowercase and remove extra spaces
        pet_label = results_dic[key][0].strip().lower()

        # Check if pet label is in dognames_list
        if pet_label in dognames_list:
            is_pet_a_dog = 1
        else:
            is_pet_a_dog = 0

        # Normalize classifier label and split into individual labels
        classifier_labels = results_dic[key][1].lower().split(',')
        is_classifier_a_dog = 0
        
        # Check if any classifier label is a dog
        for label in classifier_labels:
            label = label.strip()  # Remove any extra whitespace
            if label in dognames_list:
                is_classifier_a_dog = 1
                break

        # Append the results for whether pet and classifier labels are dogs
        results_dic[key].extend([is_pet_a_dog, is_classifier_a_dog])


# Main entry point for testing
if __name__ == "__main__":
    # Example dictionary of results for testing
    results_dic = {
        'Boston_terrier_02285.jpg': ['boston terrier', 'boston bull, boston terrier', 1],
        'German_shepherd_dog_04931.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1],
        'Basset_hound_01034.jpg': ['basset hound', 'basset, basset hound', 1],
        'cat_02.jpg': ['cat', 'tabby, tabby cat, cat', 1],
        'Great_pyrenees_05435.jpg': ['great pyrenees', 'great pyrenees', 1]
    }

    # Test dog names text file - make sure you have a text file named 'dognames.txt'
    dogfile = 'dognames.txt'

    # Example content of `dognames.txt`:
    # boston terrier
    # german shepherd dog
    # basset hound
    # great pyrenees

    # Adjust results_dic to include dog identification information
    adjust_results4_isadog(results_dic, dogfile)

    # Print out the adjusted results_dic for verification
    print("\nAdjusted Results Dictionary:")
    for key in results_dic:
        print(f"Filename: {key}")
        print(f"  Pet Label: {results_dic[key][0]}")
        print(f"  Classifier Label: {results_dic[key][1]}")
        print(f"  Match: {results_dic[key][2]}")
        print(f"  Pet Label is a Dog: {results_dic[key][3]}")
        print(f"  Classifier Label is a Dog: {results_dic[key][4]}\n")