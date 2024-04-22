import easyocr

reader = easyocr.Reader(['fr'], gpu=False)
result = reader.readtext('ant.png')

#for (bbox, text, prob) in result:
  #print(text)

print(result)