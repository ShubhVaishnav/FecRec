from django.shortcuts import render, redirect
from .models import Characters, TestForm as TestFormModel
from .forms import TestForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic
import face_recognition
import glob
from PIL import Image, ImageDraw
import os.path


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'all_characters'
    def get_queryset(self):
        return Characters.objects.all()


def detail(request, character_id):
        character = get_object_or_404(Characters, pk=character_id)
        return render(request, 'detail.html', {'character': character})


def aboutus(request):
    return render(request, 'aboutus.html')


def test_image_view(request):
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/mainCode')
    else:
        form = TestForm()
    return render(request, 'inputimage.html', {'form': form})

# for displaying images

def display_test_image(request):
    if request.method == 'GET':
        # getting all the objects.
        Tests_images = TestFormModel.objects.all()
        return render(request, 'displaytestimg.html', {'Test_images': Tests_images})

def output(request):
    return render(request, 'output.html')

def countoutput(request):
    return render(request, 'countoutput.html')

def page1(request):
    return render(request, 'page1.html')

def mainCode(request):
    image_of_sherlock = face_recognition.load_image_file('C:/users/shubh/Documents/FaceRec/persons/static/img/sherlock.jpg')
    sherlock_face_encoding = face_recognition.face_encodings(image_of_sherlock)[0]

    image_of_john = face_recognition.load_image_file('C:/users/shubh/Documents/FaceRec/persons/static/img/john.jpg')
    john_face_encoding = face_recognition.face_encodings(image_of_john)[0]

    image_of_mycroft = face_recognition.load_image_file('C:/users/shubh/Documents/FaceRec/persons/static/img/mycroft.jpg')
    mycroft_face_encoding = face_recognition.face_encodings(image_of_mycroft)[0]

    image_of_mrshudson = face_recognition.load_image_file('C:/users/shubh/Documents/FaceRec/persons/static/img/mrshudson.jpg')
    mrshudson_face_encoding = face_recognition.face_encodings(image_of_mrshudson)[0]

    image_of_mary = face_recognition.load_image_file('C:/users/shubh/Documents/FaceRec/persons/static/img/marys.jpg')
    mary_face_encoding = face_recognition.face_encodings(image_of_mary)[0]

    image_of_lestrade = face_recognition.load_image_file('C:/users/shubh/Documents/FaceRec/persons/static/img/lestrade.png')
    lestrade_face_encoding = face_recognition.face_encodings(image_of_lestrade)[0]

    image_of_molly = face_recognition.load_image_file('C:/users/shubh/Documents/FaceRec/persons/static/img/molly.jpg')
    molly_face_encoding = face_recognition.face_encodings(image_of_molly)[0]

    # create array of encoings and name
    known_face_encodings = [sherlock_face_encoding, john_face_encoding, mycroft_face_encoding, mrshudson_face_encoding,
                            mary_face_encoding, lestrade_face_encoding, molly_face_encoding]
    known_face_names = ["Sherlock", "John", "Mycroft", "MrsHudson", "Mary", "Lestrade", "Molly"]

    # load face image to faces in
    images = glob.glob('C:/users/shubh/Documents/FaceRec/media/images/*.jpg')

    for Test_image in images:
        test_image = face_recognition.load_image_file(Test_image)

    # find faces in test image
    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)
    # convert to pil format
    pil_image = Image.fromarray(test_image)
    # create imagedraw instance
    draw = ImageDraw.Draw(pil_image)
    # loop through faces in test image

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown Person"
        # if match
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        # draw box
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))
        # draw label
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0),
                       outline=(0, 0, 0))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

    del draw
    # display image
    # pil_image.show()
    pil_image.save('C:/users/shubh/Documents/FaceRec/persons/static/resultImage/result.jpg')
    print('Success')
    if os.path.exists('C:/users/shubh/Documents/FaceRec/persons/static/resultImage/result.jpg'):
        return render(request, 'output.html')

def countCode(request):

    countImage = face_recognition.load_image_file("C:/users/shubh/Documents/FaceRec/media/images/*.jpg")
    face_location = face_recognition.face_locations(countImage)

    # array of coordinates of each face
    print(face_location)
    print(f'there are {len(face_location)} people')
    number = len(face_location)
    return render(request, 'countoutput.html', {'number': number})

