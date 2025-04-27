#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Yasser Khira
# DATE CREATED: 04/27/2025                                   
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    Returns:
     parse_args() - Data structure that stores the command line arguments object
    """
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(
        description='Process images using a CNN model to classify pet images.'
    )
    
    # Add arguments with type checking and help messages
    parser.add_argument('--dir', 
                       type=str, 
                       default='pet_images/',
                       help='path to the folder containing pet images')
    
    parser.add_argument('--arch', 
                       type=str, 
                       default='vgg',
                       choices=['vgg', 'alexnet', 'resnet'],
                       help='CNN model architecture (vgg, alexnet, or resnet)')
    
    parser.add_argument('--dogfile', 
                       type=str, 
                       default='dognames.txt',
                       help='text file containing valid dog names')
    
    # Return parsed argument collection
    return parser.parse_args()
