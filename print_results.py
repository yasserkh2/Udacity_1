def print_results(results_dic, results_stats_dic, model, 
                    print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values).
    Parameters:
    results_dic - Dictionary with key as image filename and value as a List 
            (index) idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet image 'is-NOT-a' dog
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    results_stats_dic - Dictionary that contains the results statistics (either
                        a percentage or a count).
    model - Indicates which CNN model architecture was used for classification
            (string: 'resnet', 'alexnet', 'vgg').
    print_incorrect_dogs - True prints incorrectly classified dog images and 
                            False doesn't print anything (default).
    print_incorrect_breed - True prints incorrectly classified dog breeds and 
                            False doesn't print anything (default).
    Returns:
        None - simply printing results.
    """
    # Print general statistics and model used
    print(f"\n*** Results Summary for CNN Model Architecture: {model.upper()} ***")
    print(f"Number of Images: {results_stats_dic['n_images']}")
    print(f"Number of Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"Number of \"Not-a\" Dog Images: {results_stats_dic['n_notdogs_img']}")

    # Print percentages from results_stats_dic
    print("\n*** Results Statistics ***")
    for key in results_stats_dic:
        # Print only percentages (keys starting with 'pct')
        if key.startswith('pct'):
            print(f"{key.replace('pct_', '').capitalize()}: {results_stats_dic[key]:.2f}%")
    
    # Print incorrectly classified dogs if required
    if print_incorrect_dogs and (
        results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']
        != results_stats_dic['n_images']):
        print("\n*** Incorrectly Classified Dogs ***")
        for key in results_dic:
            # A dog classified as NOT-a-dog or vice versa
            if (results_dic[key][3] == 1 and results_dic[key][4] == 0) or (results_dic[key][3] == 0 and results_dic[key][4] == 1):
                print(f"Real: {results_dic[key][0]}  Classified as: {results_dic[key][1]}")

    # Print incorrectly classified breeds if required
    if print_incorrect_breed and results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
        print("\n*** Incorrectly Classified Dog Breeds ***")
        for key in results_dic:
            # A dog classified as the wrong breed (but still classified as a dog)
            if (results_dic[key][3] == 1 and results_dic[key][4] == 1 and results_dic[key][2] == 0):
                print(f"Real: {results_dic[key][0]}  Classified as: {results_dic[key][1]}")

if __name__ == "__main__":
    # Example results dictionary for testing
    results_dic = {
        'Boston_terrier_02285.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 1, 1],
        'German_shepherd_dog_04931.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1, 1, 1],
        'cat_01.jpg': ['cat', 'tabby', 0, 0, 0],
        'Great_pyrenees_05435.jpg': ['great pyrenees', 'kuvasz', 0, 1, 1],
        'Dalmatian_04068.jpg': ['dalmatian', 'coach dog', 0, 1, 1],
        'fox_01.jpg': ['fox', 'red fox', 0, 0, 0]
    }

    # Example results statistics dictionary for testing
    results_stats_dic = {
        'n_images': 6,
        'n_dogs_img': 4,
        'n_notdogs_img': 2,
        'n_match': 2,
        'n_correct_dogs': 3,
        'n_correct_notdogs': 2,
        'n_correct_breed': 2,
        'pct_match': 33.3,
        'pct_correct_dogs': 75.0,
        'pct_correct_breed': 50.0,
        'pct_correct_notdogs': 100.0
    }

    # Call the function to print the results
    print_results(results_dic, results_stats_dic, model='vgg', print_incorrect_dogs=True, print_incorrect_breed=True)
