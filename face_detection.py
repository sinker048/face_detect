import cv2

cap = cv2.VideoCapture(0)

# Create the haar cascade
facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detect face from image
    faces = facecascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30) 
    )

    print("There are {} faces".format(len(faces)))

    for(x,y,w, h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow()