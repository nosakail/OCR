#keep best ocr result and show image
def apply_best_result(img_path, imp_img_path):
    
    reader = easyocr.Reader(['en'], gpu=False)
    
    
    base_img = cv2.imread(img_path)
    imp_img = cv2.imread(imp_img_path)
    
    results = reader.readtext(base_img)
    results2 = reader.readtext(imp_img)
    
    performance_base_img = np.mean([r[2] for r in results])
    performance_imp_img = np.mean([r[2] for r in results2])
    
    
    
    
    
    if performance_base_img > performance_imp_img:
        for result in results:
            bbox, res, score = result
            
            # Conversion
            bbox = np.array(bbox, dtype=np.int32)
            
            cv2.rectangle(base_img, tuple(bbox[0]), tuple(bbox[2]), (0, 255, 0), 5)
            cv2.putText(base_img, res, tuple(bbox[0]), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
            
        # Convertir l'image en RGB (OpenCV lit les images en BGR par défaut)
        annotated_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
            
        # Retourner l'image annotée
        return annotated_img
        
    else :
        for result in results2:
            bbox, res, score = result
            
            # Conversion
            bbox = np.array(bbox, dtype=np.int32)
            
            cv2.rectangle(base_img, tuple(bbox[0]), tuple(bbox[2]), (0, 255, 0), 5)
            cv2.putText(base_img, res, tuple(bbox[0]), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
            
        # Convertir l'image en RGB (OpenCV lit les images en BGR par défaut)
        annotated_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
            
        # Retourner l'image annotée
        return annotated_img


def show(base_img, res_img):
    col1.write("Original Image :camera:")
    col1.image(base_img)

    col2.write("Fixed Image :wrench:")
    col2.image(res_img)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download the result", convert_image(res_img), "your_result_image.png", "image/png")

