# mDL-ArtTransfer: Deep Learning Art Transfer using Multiple AIs (by muntisa)
# 
# Mix of scripts by Coursera, fchollet, anishathalye, ShafeenTejani
# General parameters:
# - content, style and output files are in separated folders
# - the number of iterations are the same for all the AIs
# Note: generated images (outputs) will have composed names as [content_name]_[style_name]_[iterations].jpg

import os, time

# set starting time
start_time = time.time()

print """
**************************************************************************
mDLArtTransfer: Deep Learning Art Transfer using Multiple AIs (by muntisa)
**************************************************************************
1) Coursera     : https://www.coursera.org/learn/convolutional-neural-networks
2) fchollet     : https://github.com/keras-team/keras/blob/master/examples/neural_style_transfer.py
3) anishathalye : https://github.com/anishathalye/neural-style
4) ShafeenTejani: https://github.com/ShafeenTejani/style-transfer
**************************************************************************
"""

# ====================================================
# PARAMETERS
# ====================================================
# please set the content, style and output folders 
ContentFolder   = "contents"  # folder with initial photos
StyleFolder     = "styles"    # folder with styles to use to modify initial photos
GeneratedFolder = "outputs"   # folder with generated photo by mixind content and style using AI art transfer

# please set the iterations
iter = 200  # number of iterations for all the AI scripts (1000 = default for anishathalye's AI)

# Set the lists with files
ContentFileList  = os.listdir(ContentFolder) # get all files in content folder
# ContentFileList = ["dog.jpg","dome.jpg","lion.jpg","london.jpg","puppy.jpg"] # use a specific list
StyleFileList    = os.listdir(StyleFolder)   # get all files in style folder
# StyleFileList = ["dora-maar-picasso.jpg","rain-princess-aframov.jpg","starry-night-van-gogh.jpg"] # use a specific list
# ====================================================

print "Content Folder =", ContentFolder
print "Style Folder   =", StyleFolder
print "Output Folder  =", GeneratedFolder

# for each image to modify use each style image to generate a new image
i = 0 # curent number of generated images
n = len(ContentFileList)*len(StyleFileList) # total number of generated files
for iContentFile in ContentFileList:
	sContentFile = os.path.join(ContentFolder, iContentFile) # join path with filename for content
	for iStyleFile in StyleFileList:
		print "\n\n==> ", "Content = ", iContentFile, "Style = ", iStyleFile
		sStyleFile   = os.path.join(StyleFolder, iStyleFile) # join path with filename for style
		
		# (1) Run Coursera's AI (https://www.deeplearning.ai/)
		# !!! if you didn't finish the course, you could disable the next 7 lines !!!
		sOutputFile  = os.path.join(GeneratedFolder, iContentFile[:-4]+"_"+iStyleFile[:-4]+"_Coursera_"+str(iter)+".jpg") # join path with filename for style
		sCmd = "python Coursera_ArtTransfer.py "+sContentFile+" "+sStyleFile+" --output_image "+sOutputFile+" --iterations "+str(iter)
		i+=1
		print "\n\n---> Running (1) - ", i, "from", n, ":",  sCmd
		time_AI1 = time.time()
		os.system(sCmd);
		print("... Execution time for (1): %s seconds" % (time.time() - time_AI1))
		
		# (2) Run fchollet's AI (https://github.com/keras-team/keras/blob/master/examples/neural_style_transfer.py)
		sOutputFile  = os.path.join(GeneratedFolder, iContentFile[:-4]+"_"+iStyleFile[:-4]+"_fchollet_"+str(iter)+".jpg") # join path with filename for style
		sCmd = "python fchollet_neural_style_transfer.py "+sContentFile+" "+sStyleFile+" "+sOutputFile+" --iter "+str(iter)
		i+=1
		print "\n\n---> Running (2) - ", i, "from", n, ":",  sCmd
		time_AI2 = time.time()
		os.system(sCmd);
		print("... Execution time for (2): %s seconds" % (time.time() - time_AI2))
		
		# (3) Run anishathalye's AI (https://github.com/anishathalye/neural-style)
		sOutputFile  = os.path.join(GeneratedFolder, iContentFile[:-4]+"_"+iStyleFile[:-4]+"_anishathalye_"+str(iter)+".jpg") # join path with filename for style
		sCmd = "python anishathalye_neural_style.py --content "+sContentFile+" --styles "+sStyleFile+" --output "+sOutputFile+" --iterations "+str(iter)
		i+=1
		print "\n\n---> Running (3) - ", i, "from", n, ":",  sCmd
		time_AI3 = time.time()
		os.system(sCmd);
		print("... Execution time for (3): %s seconds" % (time.time() - time_AI3))
		
		# (4) Run ShafeenTejani's AI (https://github.com/ShafeenTejani/style-transfer)
		sOutputFile  = os.path.join(GeneratedFolder, iContentFile[:-4]+"_"+iStyleFile[:-4]+"_ShafeenTejani_"+str(iter)+".jpg") # join path with filename for style
		# you should remove "--use-gpu" for cpu calculations
		sCmd = "python ShafeenTejani_run.py --content "+sContentFile+" --style "+sStyleFile+" --output "+sOutputFile+" --use-gpu --iterations "+str(iter) 
		i+=1
		print "\n\n---> Running (4) - ", i, "from", n, ":",  sCmd
		time_AI4 = time.time()
		os.system(sCmd);
		print("... Execution time (4): %s seconds" % (time.time() - time_AI4))

print("\n\nTotal Execution time of mDLArtTransfer: %s seconds" % (time.time() - start_time))
