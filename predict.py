# 'pip install -r req.txt' install dependencies


import tensorflow.keras
import numpy as np
import cv2
import os

# Load the model
model = tensorflow.keras.models.load_model('model/keras_model.h5')

def process(image):
	# Create the array of the right shape to feed into the keras model
	# The 'length' or number of images you can put into the array is
	# determined by the first position in the shape tuple, in this case 1.
	
	data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

	# Make sure to resize all images to 224, 224 otherwise they won't fit in the array
	image = cv2.flip(image, 1)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	image = cv2.resize(image,(224, 224))

	# Normalize the image
	normalized_image_array = (image.astype(np.float32) / 127.0) - 1

	# Load the image into the array
	data[0] = normalized_image_array

	return data

def predict(data):
	prediction = model.predict(data)
	return prediction

def main():
    # Load your model onto your Coral Edgetpu
    DEBRIS = "Debris Detected"
    NO_DEBRIS = "No Debris"


    cap = cv2.VideoCapture('http://192.168.43.216:8000/stream.mjpg')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Classify and display image
        
        results = predict(process(frame))
        if results[0][0] > 0.98:
        	print(DEBRIS)
        	debris = 'mosquitto_pub -h 192.168.43.216 -t "test" -m "1"'
        	os.system(debris)
        	cv2.putText(frame, DEBRIS, (0,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA) 
        else:
        	print(NO_DEBRIS)
        	no_debris = 'mosquitto_pub -h 192.168.43.216 -t "test" -m "0"'
        	os.system(no_debris)
        	cv2.putText(frame, NO_DEBRIS, (0,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
