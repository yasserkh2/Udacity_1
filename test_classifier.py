#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/test_classifier.py
#                                                                             
# PROGRAMMER: Yasser Khira                                                    
# DATE CREATED: 04/27/2025                                  
# REVISED DATE: 
# PURPOSE: To demonstrate the proper usage of the classifier() function that 
#          is defined in classifier.py This function uses CNN model 
#          architecture that has been trained and can classify many types of
#          images. The only limitation is that the image must be a jpg or png
#          format.
#
# Usage: python test_classifier.py    -- will run program from commandline

# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# Defines a test image
test_image = "pet_images/Collie_03797.jpg"

# Defines a model architecture to be used for classification
model = "vgg"

# Demonstrates classifier() functions usage
print("\nResults from test_classifier.py\nImage:", test_image, "using model:",
      model, "was classified as a:", classifier(test_image, model))