
import cv2
import streamlit as st
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import mediapipe as mp

st.title('Object Detection App')
uploaded_image = st.file_uploader('Please, Upload an Image...', type = ['jpg', 'png', 'jpeg'])

MARGIN = 10  # pixels
ROW_SIZE = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
TEXT_COLOR = (255, 0, 0)  # red

def visualize(
    image,
    detection_result
) -> np.ndarray:
  for detection in detection_result.detections:
    # Draw bounding_box
    bbox = detection.bounding_box
    start_point = bbox.origin_x, bbox.origin_y
    end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
    cv2.rectangle(image, start_point, end_point, TEXT_COLOR, 3)

    # Draw label and score
    category = detection.categories[0]
    category_name = category.category_name
    probability = round(category.score, 2)
    result_text = category_name + ' (' + str(probability) + ')'
    text_location = (MARGIN + bbox.origin_x,
                     MARGIN + ROW_SIZE + bbox.origin_y)
    cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                FONT_SIZE, TEXT_COLOR, FONT_THICKNESS)

  return image


base_options = python.BaseOptions(model_asset_path='C:/Users/user/Downloads/efficientdet_lite0.tflite')
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.5)
detector = vision.ObjectDetector.create_from_options(options)

if uploaded_image is not None:
    file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype = np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    st.image(img, 'Uploaded Image', use_column_width = True)
    
    mp_image = mp.Image(image_format = mp.ImageFormat.SRGB, data = img)
    
    
    detection_result = detector.detect(mp_image)
    
    result = visualize(img, detection_result)
    
    st.image(result, use_column_width = True)
