#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#                                                                             
# PROGRAMMER: Yasser Khira
# DATE CREATED: 04/27/2025
# REVISED DATE: 
# PURPOSE: This is the main program that runs the image classification project.
#          It uses a pre-trained CNN model to classify pet images and compares
#          these classifications to the true identity of the pets in the images.
#
##

# Imports python modules
import os
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def main():
    """
    Main program function for the Pet Image Classification Project
    Parameters:
        None - simply using argparse module to create & store command line arguments
    Returns:
        None - simply running the program.
    """
    # Start the timer
    start_time = time()
    
    # Get input arguments
    in_arg = get_input_args()

    # Function that checks command line arguments using in_arg  
    check_command_line_arguments(in_arg)

    # Create the results dictionary
    results = get_pet_labels(in_arg.dir)
    
    # Function that checks Pet Images in the results Dictionary using results    
    check_creating_pet_image_labels(results)

    # Classify images and update results dictionary
    classify_images(in_arg.dir, results, in_arg.arch)

    # Function that checks Results Dictionary using results    
    check_classifying_images(results)    

    # Adjust results to determine if classifier correctly classified images as 'a dog' or 'not a dog'
    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)

    # Calculate results stats
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)

    # Print summary results, incorrect classifications of dogs and breeds
    print_results(results, results_stats, in_arg.arch, True, True)
    
    # Calculate running time
    end_time = time()
    tot_time = end_time - start_time

    # Print runtime in hours, minutes, seconds format
    hours = int((tot_time / 3600))
    minutes = int((tot_time % 3600) / 60)
    seconds = int((tot_time % 3600) % 60)
    
    print("\n** Total Elapsed Runtime:",
          "{}:{}:{}".format(str(hours).zfill(2),
                           str(minutes).zfill(2),
                           str(seconds).zfill(2)))

# Call to main function to run the program
if __name__ == "__main__":
    main()