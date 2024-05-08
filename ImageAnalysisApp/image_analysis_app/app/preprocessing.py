from colorthief import ColorThief
import cv2



#determine if background is darkened
def is_background_darkened(img_path):
    ct = ColorThief(img_path)
    dominent_color = ct.get_color(quality=1)
    
    # Convert color in gray lvl
    gray = np.dot(dominent_color[0:3], [0.299, 0.587, 0.114])

    # Determine
    if gray > 128:
        print(gray)
        return False

    else:
        print(gray)
        return True
        
#determine low contrast
def is_low_contrast(img_path):
    img = cv2.imread(img_path)
    Y = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)[:,:,0]
    
    # compute min and max of Y
    min = np.min(Y)
    max = np.max(Y)
    
    # compute contrast
    contrast = (max-min)/(max+min)
    if contrast < 0.5 :
        return True 
    else :
        return False
        
# get saturation
def get_saturation(img_path):
    img = cv2.imread(img_path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    saturation = img_hsv[:, :, 1].mean()
    return saturation  

 


