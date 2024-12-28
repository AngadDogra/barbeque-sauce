import cv2           # import the computer vision  library

camera = cv2.VideoCapture(0)           # Opens the default camera

# Height and Width
frameWidth = int (camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int (camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec --- wtf is a codec -> Q1
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frameWidth, frameHeight))

while True:
    ret, frame = camera.read()

    out.write(frame)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
out.release()
cv2.destroyAllWindows()
