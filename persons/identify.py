import face_recognition
import glob
from PIL import Image, ImageDraw

image_of_sherlock = face_recognition.load_image_file('C:/users/shubh/Desktop/img/sherlock.jpg')
sherlock_face_encoding = face_recognition.face_encodings(image_of_sherlock)[0]

image_of_john = face_recognition.load_image_file('C:/users/shubh/Desktop/img/john.jpg')
john_face_encoding = face_recognition.face_encodings(image_of_john)[0]

image_of_mycroft = face_recognition.load_image_file('C:/users/shubh/Desktop/img/mycroft.jpg')
mycroft_face_encoding = face_recognition.face_encodings(image_of_mycroft)[0]

image_of_mrshudson = face_recognition.load_image_file('C:/users/shubh/Desktop/img/mrshudson.jpg')
mrshudson_face_encoding = face_recognition.face_encodings(image_of_mrshudson)[0]

image_of_mary = face_recognition.load_image_file('C:/users/shubh/Desktop/img/marys.jpg')
mary_face_encoding = face_recognition.face_encodings(image_of_mary)[0]

image_of_lestrade = face_recognition.load_image_file('C:/users/shubh/Desktop/img/lestrade.png')
lestrade_face_encoding = face_recognition.face_encodings(image_of_lestrade)[0]

image_of_molly = face_recognition.load_image_file('C:/users/shubh/Desktop/img/molly.jpg')
molly_face_encoding = face_recognition.face_encodings(image_of_molly)[0]

image_of_modi = face_recognition.load_image_file('C:/users/shubh/Desktop/img/modi.png')
modi_face_encoding = face_recognition.face_encodings(image_of_modi)[0]


#create array of encoings and name
known_face_encodings = [sherlock_face_encoding, john_face_encoding, mycroft_face_encoding, mrshudson_face_encoding, mary_face_encoding, lestrade_face_encoding, molly_face_encoding, modi_face_encoding]
known_face_names = ["Sherlock", "John", "Mycroft", "MrsHudson", "Mary", "Lestrade", "Molly", "Modi"]

#load face image to faces in
images = glob.glob('G:/django_projects/webapp/media/images/*.jpg')

for Test_image in images:
     test_image = face_recognition.load_image_file(Test_image)

#find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)
#convert to pil format
pil_image = Image.fromarray(test_image)
#create imagedraw instance
draw = ImageDraw.Draw(pil_image)
#loop through faces in test image

for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown Person"
    #if match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    #draw box
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))
    #draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0),
    outline=(0, 0, 0))
    draw.text((left+6, bottom-text_height-5), name, fill=(255, 255, 255, 255))

del draw

#display image
# pil_image.show()

pil_image.save('C:/users/shubh/django_projects/webapp/media/images/result.jpg')
