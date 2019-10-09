import face_recognition
from PIL import Image, ImageDraw

image_of_ps = face_recognition.load_image_file('./img/known/Piyas Sir.jpeg')
ps_face_encoding = face_recognition.face_encodings(image_of_ps)[0]

image_of_tm = face_recognition.load_image_file('./img/known/Tahira Madam.jpeg')
tm_face_encoding = face_recognition.face_encodings(image_of_tm)[0]

#create array of encoding and names

known_face_encodings = [
    ps_face_encoding,
    tm_face_encoding
]

known_face_names = [
    "Piyas Sir",
    "Tahira Madam"
]

# Load test image to find faces in
test_image = face_recognition.load_image_file('./img/group/team-1.jpeg')

#find faces in the test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image,face_locations)

# covert to PIL format
pil_image = Image.fromarray(test_image)

#create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for(top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings,face_encoding)

    name = "Unknown"

    if True in matches:  #if faces matches
        first_match_index = matches.index(True) 
        name = known_face_names[first_match_index]
    

    #draw Box
    draw.rectangle(((left,top),(right,bottom)),outline=(0,0,1))

    #draw label
    text_width,text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10),(right,bottom)),fill=(0,0,1),outline=(0,0,1))
    draw.text((left+6,bottom - text_height - 5),name,fill=(255,255,255,255))

del draw
# Display image
pil_image.show()