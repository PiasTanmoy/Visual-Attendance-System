import face_recognition

image_of_ps = face_recognition.load_image_file('./img/known/Piyas Sir.jpeg')
ps_face_encoding = face_recognition.face_encodings(image_of_ps)[0]

unknown_image = face_recognition.load_image_file('./img/unknown/ps4.jpeg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

#compare faces
results = face_recognition.compare_faces([ps_face_encoding],unknown_face_encoding)

if results[0]:
    print('Face Matched')
else:
    print('Not Matched')