def calculates_results_stats(results_dic):
    # Initialize statistics dictionary
    results_stats_dic = {
        'n_images': 0,
        'n_dogs_img': 0,
        'n_notdogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0
    }
    
    # Iterate through the results dictionary to calculate the statistics
    for key in results_dic:
        # Print the current entry for debugging
        print(f"Processing {key}: {results_dic[key]}")
        
        # Increment the number of images
        results_stats_dic['n_images'] += 1

        # Increment match count if pet label matches classifier label
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # Check if pet image label is a dog
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1

            # Increment correct dog classification count
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1

            # Increment correct breed classification count if there is a match
            if results_dic[key][2] == 1:
                results_stats_dic['n_correct_breed'] += 1
        else:
            # Increment not-dog image count
            results_stats_dic['n_notdogs_img'] += 1
            
            # Increment correct not-dog classification count
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculate percentages
    if results_stats_dic['n_images'] > 0:
        results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0
    else:
        results_stats_dic['pct_match'] = 0.0

    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0
        results_stats_dic['pct_correct_breed'] = 0.0

    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    return results_stats_dic


# Main entry point for testing
if __name__ == "__main__":
    # Example results dictionary for testing
    results_dic = {'Boston_terrier_02285.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 1, 1], 'German_shepherd_dog_04931.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1, 0, 0], 'Basset_hound_01034.jpg': ['basset hound', 'basset, basset hound', 1, 0, 0], 'cat_02.jpg': ['cat', 'tabby, tabby cat, cat', 1, 0, 0], 'Great_pyrenees_05435.jpg': ['great pyrenees', 'great pyrenees', 1, 0, 0], 'Boston_terrier_02303.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 1, 1], 'German_shorthaired_pointer_04986.jpg': ['german shorthaired pointer', 'german shorthaired pointer', 1, 0, 0], 'Golden_retriever_05195.jpg': ['golden retriever', 'golden retriever', 1, 1, 1], 'Miniature_schnauzer_06884.jpg': ['miniature schnauzer', 'miniature schnauzer', 1, 0, 0], 'Collie_03797.jpg': ['collie', 'collie', 1, 0, 0], 'Golden_retriever_05223.jpg': ['golden retriever', 'golden retriever', 1, 1, 1], 'gecko_80.jpg': ['gecko', 'tailed frog, bell toad, ribbed toad, tailed toad, ascaphus trui', 0, 0, 0], 'Great_pyrenees_05367.jpg': ['great pyrenees', 'kuvasz', 0, 0, 0], 'Beagle_01125.jpg': ['beagle', 'beagle', 1, 0, 0], 'Basenji_00974.jpg': ['basenji', 'basenji', 1, 0, 0], 'Golden_retriever_05182.jpg': ['golden retriever', 'golden retriever', 1, 1, 1], 'Poodle_07927.jpg': ['poodle', 'standard poodle, poodle', 1, 0, 0], 'Cocker_spaniel_03750.jpg': ['cocker spaniel', 'cocker spaniel, english cocker spaniel, cocker', 1, 0, 0], 'Dalmatian_04068.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'great_horned_owl_02.jpg': ['great horned owl', 'ruffed grouse, partridge, bonasa umbellus', 0, 0, 0], 'Golden_retriever_05257.jpg': ['golden retriever', 'golden retriever', 1, 1, 1], 'Beagle_01170.jpg': ['beagle', 'walker hound, walker foxhound', 0, 0, 0], 'cat_01.jpg': ['cat', 'lynx', 0, 0, 0], 'Saint_bernard_08010.jpg': ['saint bernard', 'saint bernard, st bernard', 1, 0, 0], 'Poodle_07956.jpg': ['poodle', 'standard poodle, poodle', 1, 0, 0], 'Basenji_00963.jpg': ['basenji', 'basenji', 1, 0, 0], 'fox_squirrel_01.jpg': ['fox squirrel', 'fox squirrel, eastern fox squirrel, sciurus niger', 1, 0, 0], 'Great_dane_05320.jpg': ['great dane', 'great dane', 1, 0, 0], 'Saint_bernard_08036.jpg': ['saint bernard', 'saint bernard, st bernard', 1, 0, 0], 'skunk_029.jpg': ['skunk', 'skunk, polecat, wood pussy', 1, 0, 0], 'Dalmatian_04037.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'gecko_02.jpg': ['gecko', 'banded gecko, gecko', 1, 0, 0], 'polar_bear_04.jpg': ['polar bear', 'ice bear, polar bear, ursus maritimus, thalarctos maritimus', 1, 0, 0], 'Dalmatian_04017.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'Boston_terrier_02259.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 1, 1], 'Rabbit_002.jpg': ['rabbit', 'wood rabbit, cottontail, cottontail rabbit, rabbit', 1, 0, 0], 'Beagle_01141.jpg': ['beagle', 'beagle', 1, 0, 0], 'Boxer_02426.jpg': ['boxer', 'boxer', 1, 0, 0], 'German_shepherd_dog_04890.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1, 0, 0], 'cat_07.jpg': ['cat', 'egyptian cat, cat', 1, 0, 0]}


    # Call the function to calculate the statistics
    results_stats = calculates_results_stats(results_dic)
    
    # Print the statistics for debugging
    print("\nCalculated Results Stats:")
    for key, value in results_stats.items():
        print(f"{key}: {value}")
    print(results_stats)
