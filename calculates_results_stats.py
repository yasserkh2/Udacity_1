#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Yasser Khira
# DATE CREATED: 04/27/2025                                  
# REVISED DATE: 
# PURPOSE: Calculate statistics about the results of running the classifier on
#          the images. These statistics will help determine which model
#          architecture works best for classifying images.
#
##

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary containing statistics about the results
    """
    # Initialize the results statistics dictionary
    results_stats_dic = {
        'n_dogs_img': 0,        # number of dog images
        'n_match': 0,           # number of matches between pet & classifier labels
        'n_correct_dogs': 0,    # number of correctly classified dog images
        'n_correct_notdogs': 0, # number of correctly classified NON-dog images
        'n_correct_breed': 0    # number of correctly classified dog breeds
    }
    
    # Process through the results dictionary
    for key in results_dic:
        # When labels match exactly
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1
            
            # When pet image is a dog and labels match, counted as correct breed
            if results_dic[key][3] == 1:
                results_stats_dic['n_correct_breed'] += 1
        
        # When pet image is a dog
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            # When classifier correctly identifies image as dog
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
                
        # When pet image is NOT a dog
        else:
            # When classifier correctly identifies image as NOT a dog
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # Calculate total number of images
    results_stats_dic['n_images'] = len(results_dic)
    
    # Calculate number of not-a-dog images
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - 
                                         results_stats_dic['n_dogs_img'])
    
    # Calculate percentages
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / 
                                     results_stats_dic['n_images']) * 100.0
    
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / 
                                            results_stats_dic['n_dogs_img']) * 100.0
    
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / 
                                             results_stats_dic['n_dogs_img']) * 100.0
    
    # Handle case when no NON-dog images were submitted
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                   results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
    
    return results_stats_dic
