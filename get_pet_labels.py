#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Yasser Khira
# DATE CREATED: 04/27/2025                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames of the image files.
    The pet image labels are used to check the accuracy of the classifier function's labels.
    
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Create list of files in directory
    in_files = listdir(image_dir)
    
    # Create empty dictionary for results
    results_dic = dict()
   
    # Process each file in the directory
    for filename in in_files:
        # Skip hidden files (starting with .)
        if not filename.startswith('.'):
            # Extract pet label from filename
            # Split filename by '_' and remove file extension
            name_parts = filename.lower().split('_')
            
            # Initialize pet label as empty list to store words
            label_words = []
            
            # Process each part and keep only alphabetic words
            for part in name_parts:
                # Remove file extension if present
                word = part.split('.')[0]
                # Only keep parts that are purely alphabetic
                if word.isalpha():
                    label_words.append(word)
            
            # Create pet label by joining words with space
            pet_label = ' '.join(label_words)

            # Add to dictionary only if filename doesn't already exist
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                print("** Warning: Duplicate files exist in directory:", filename)
 
    return results_dic
