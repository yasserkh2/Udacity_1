#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Yasser Khira
# DATE CREATED: 04/27/2025                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the function call within main.
#            -The CNN model architecture as model within classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary.
#
##
from classifier import classifier 
from os.path import join

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function.
    Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    # Process all files in the results_dic
    for key in results_dic:
        # Get the full path to the image file
        image_path = join(images_dir, key)
        
        # Use classifier function to classify the image
        model_label = classifier(image_path, model)
        
        # Process classifier label to match format of pet image labels
        # Convert to lowercase and remove leading/trailing whitespace
        model_label = model_label.lower().strip()
        
        # Get the pet image label (truth)
        truth = results_dic[key][0]
        
        # Compare labels and extend results_dic with classifier label and match status
        # Check if any of the classifier's terms exactly match the pet image label
        found_match = False
        # Split classifier label in case it contains multiple terms
        classifier_terms = [term.strip() for term in model_label.split(',')]
        
        # Check each term for an exact match
        for term in classifier_terms:
            if truth == term:
                found_match = True
                break
        
        # Extend results_dic with classifier label and match status
        if found_match:
            results_dic[key].extend([model_label, 1])
        else:
            results_dic[key].extend([model_label, 0])
