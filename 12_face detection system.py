import cv2
import face_recognition
import numpy as np

def capture():
    video_capture = cv2.VideoCapture(0)
    known_face = []
    known_names = []



    while True:
        ret, frame = video_capture.read()



        rgb_frame = frame[:, :, ::-1]  
        face_locations = face_recognition.face_locations(rgb_frame)


        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
           
            name = "Unknown"
            if len(known_face) > 0:
                matches = face_recognition.compare_faces(known_face, face_encoding)
                if True in matches:


                    first_match_index = matches.index(True)
                    name = known_names[first_match_index]

        
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()


    cv2.destroyAllWindows()