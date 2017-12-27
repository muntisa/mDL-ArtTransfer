# coding: utf-8

## Coursera Deep Learning & Art: Neural Style Transfer
## https://www.coursera.org/learn/convolutional-neural-networks
## Modified by muntisa

# !!! This cod is not complete because you need the Coursera practice !!!
# (the Coursera script is based on Tensorflow)

import os, sys, time

# (Coursera) All imports 

# (Coursera) Function to compute the cost of content (C) using the hidden layer activations representing content of the image C and the hidden layer activations representing content of the generated image (G)

# (Coursera) Function to calculate Gram matrix used for style cost calculation

# (Coursera) Function to compute style cost for one layer using the hidden layer activations representing style of the image S and hidden layer activations representing style of the image G

# (Coursera) Function to computer the overall style cost from several chosen layers

# (Coursera) Function to compute the total cost function (content and style cost)

# (Coursera) Function to generate the image G using training iterations (I save only the last image)

# Setup to receive command line arguments
parser = argparse.ArgumentParser(description='Coursera implemenation of neural style transfer (modified by muntisa)')
parser.add_argument('content_image', metavar='content_image', type=str, help='Path to the content image to transform.')
parser.add_argument('style_image', metavar='style_image', type=str, help='Path to the style image to use.')
parser.add_argument('--output_image', metavar='output_path', type=str, default='generated.jpg', help='Path to store the generated image.')
parser.add_argument('--content_weight', type=float, default=10, help='Set content loss weight.')
parser.add_argument('--style_weight', help='Set style loss weight.', type=float, default=40.0)
parser.add_argument('--iterations', help='Set the number of iterations to run the optimizer for.', type=int, default=20)

#######################################
# The original script has no parameters, so I just place the most important ones
# Parse command line arguments
args = parser.parse_args()
content_image_path = args.content_image
style_image_path = args.style_image
output_image_path = args.output_image
content_weight = args.content_weight
style_weight = args.style_weight
iterations = args.iterations

print("-> Coursera Art Transfer DL ...")	

# To compare the other script execution time
start_time = time.time()
#######################################

# (Coursera) default layers:
STYLE_LAYERS = [
    ('conv1_1', 0.2),
    ('conv2_1', 0.2),
    ('conv3_1', 0.2),
    ('conv4_1', 0.2),
    ('conv5_1', 0.2)]

# (Coursera) Reset the graph, start interactive session, load, reshape, and normalize our "content" image

#######################################
# The original script is working only with content images of 300 by 400, other dimentions will raise errors!
# So, I just added an image redimension
new_shape = (300, 400)
content_image = scipy.misc.imresize(content_image, new_shape)
#######################################

# (Coursera) Load, reshape and normalize our "style" image (Claude Monet's painting):

#######################################
# Redimention the style image too using 300x400
style_image = scipy.misc.imresize(style_image, new_shape)
#######################################

# (Coursera) Initialize the "generated" image as a noisy image created from the content_image
# (Coursera) Load the VGG19 model from pretrained-model folder
# (Coursera) Assign the content image to be the input of the VGG model 
# (Coursera) Select the output tensor of layer conv4_2
# ....
# (Coursera) Compute the content cost
# ...
# (Coursera) Assign the input of the model to be the "style" image 
# (Coursera) Compute the style cost
# (Coursera) Train the model using Adam
# (Coursera) Generate an artistic image
##########################################
print("--- %s seconds ---" % (time.time() - start_time))

