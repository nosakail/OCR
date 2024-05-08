import cv2
import os


#if background is not darkened
def process_not_darkened_background(img_path):
    # read image
    img = cv2.imread(img_path)
    
    # Convert image in gray lvl
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresh
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    
    # Inverse colors
    inverted = cv2.bitwise_not(thresh)
    
    return(inverted)

#if background is darkened 
def process_background_darkened(img_path):
    img = cv2.imread(img_path)   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    # Apply inverse thresh
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)    
    inverted = cv2.bitwise_not(thresh)
    
    return inverted

#if low contrast
def ajust_low_contrast(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img_equalized = cv2.equalizeHist(img)

    return img_equalized

#if hight saturation
def ajust_hight_saturation(img_path):
    tab = []
    img = cv2.imread(img_path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    tab.append(gray_image)
    img_name = os.path.basename(img_path)
    result_img_path = os.path.join('img_to_process', f"{os.path.splitext(img_name)[0]}_result.png")
    cv2.imwrite(result_img_path, gray_image)
    tab.append(result_img_path)
    
    return tab

#Main fonction who apply filters to image in repertory, create,and stocke this image and in other repertory 
def improve_image(img_path):
    # Extract file name of img_path
    file_name = os.path.basename(img_path)
    # build new file name with result before the extension
    file_name_result = file_name.split('.')[0] + '_result.png'
    # build new path
    new_img_path = os.path.join('img_to_process', file_name_result)
    
    if get_saturation(img_path) > 127.23:
        if is_background_darkened(img_path):
            img = process_background_darkened(img_path)
            cv2.imwrite(new_img_path, img)
        else : 
            img = process_not_darkened_background(img_path)
            cv2.imwrite(new_img_path, img)
    else : 
        if is_low_contrast(img_path):
            img = ajust_low_contrast(img_path)
            cv2.imwrite(new_img_path, img)
        else :
            if is_background_darkened(img_path):
                img = process_background_darkened(img_path)
                cv2.imwrite(new_img_path, img)
            else : 
                img = process_not_darkened_background(img_path)
                cv2.imwrite(new_img_path, img)
