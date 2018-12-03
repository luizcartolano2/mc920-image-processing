import cv2
import numpy as np
from matplotlib.pyplot import imshow, show

######################################################################
# 	Method to read an image 										 #
#																	 #	
#    Parameters 													 #
#   ----------														 #
#	    filename : str 												 #
#	        The file location of the image 							 #
#																	 #
#   Returns 														 #
#    -------														 #
#	    list 														 #
#	        A list of ints with the matrix of pixels of the image.   #
######################################################################
def readImage(filename):
	# read the image
	image_matrix = cv2.imread(filename,1)
	img = image_matrix.astype(dtype='uint8')
	# return the image readed
	return img

def storeImage(filename, image_matrix):
	"""

		Method to store new images

	    Parameters
	    ----------
		    filename : str
		        The file location of the image
		    image_matrix : list
		    	A list of ints with the matrix of pixels of the image

	    Returns
	    -------
		    Nothing
    
    """

	cv2.imwrite(filename, image_matrix)

def rotateImage(imgMatrix, rotAngle):

	#	pega a altura e largura da imagem
	height, width = imgMatrix.shape[:2]
	# 	pega o ponto central da imagem
	centralPoint = (width / 2, height / 2)

	rotation = cv2.getRotationMatrix2D(centralPoint, rotAngle, 1.0)
	rotated = cv2.warpAffine(imgMatrix, rotation, (width, height))

	cv2.imshow("Rotacionado ", rotated)
 
	cv2.waitKey(0)

	return rotated