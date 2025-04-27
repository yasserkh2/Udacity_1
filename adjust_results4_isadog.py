#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Yasser Khira
# DATE CREATED: 04/27/2025                                 
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. 
#
##

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name.
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    # Create dictionary of dog names from dogfile
    dognames_dic = {}
    
    # Read dog names from file and add to dictionary
    with open(dogfile, "r") as f:
        for line in f:
            # Remove newline character and any leading/trailing whitespace
            dog_name = line.strip()
            
            # Add to dictionary if not already present
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1
                
            # Handle comma-separated breed names (e.g., "maltese dog, maltese terrier")
            if ',' in dog_name:
                for breed in dog_name.split(','):
                    breed = breed.strip()
                    if breed not in dognames_dic:
                        dognames_dic[breed] = 1

    # Adjust results_dic to include whether labels are dogs
    for key in results_dic:
        # Get pet and classifier labels
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]
        
        # Initialize is_dog values
        pet_is_dog = 1 if pet_label in dognames_dic else 0
        classifier_is_dog = 1 if classifier_label in dognames_dic else 0
        
        # Add values to results_dic
        results_dic[key].extend([pet_is_dog, classifier_is_dog])