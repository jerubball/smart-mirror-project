# https://www.superdatascience.com/opencv-face-recognition/

# this function will read all persons' training images, detect face from each image
# and will return two lists of exactly same size, one list
# of faces and another list of labels for each face
import os
import cv2
import numpy as np
import time

faces = None
labels = None
face_recognizer = None
home_dir = 'C:\\Users\\Timmy .LAPTOP-VEVB5SPR\Desktop\\'

#function to detect face using OpenCV
def detect_face(img):
    #convert the test image to gray scale as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #load OpenCV face detector, I am using LBP which is fast
    #there is also a more accurate but slow: Haar classifier
    #face_cascade = cv2.CascadeClassifier('faces/lbpcascade_frontalface_improved.xml')
    face_cascade = cv2.CascadeClassifier('faces/lbpcascade_frontalface.xml')
    
    #let's detect multiscale images(some images may be closer to camera than others)
    #result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    #if no faces are detected then return original img
    if (len(faces) == 0):
        print("face not found")
        return None, None
    
    #under the assumption that there will be only one face,
    #extract the face area
    (x, y, w, h) = faces[0]
    return gray[y:y+w, x:x+h], faces[0]

def prepare_training_data(data_folder_path):
    # ------STEP-1--------
    # get the directories (one directory for each subject) in data folder
    dirs = os.listdir(data_folder_path)
    
    # list to hold all subject faces
    faces = []
    # list to hold labels for all subjects
    labels = []
    
    # let's go through each directory and read images within it
    for dir_name in dirs:
        print (dir_name)
        
        # our subject directories start with letter 's' so
        # ignore any non-relevant directories if any
        if not dir_name.startswith("s"):
            continue;
        
        # ------STEP-2--------
        # extract label number of subject from dir_name
        # format of dir name = slabel
        # , so removing letter 's' from dir_name will give us label
        label = int(dir_name.replace("s", ""))
        
        # build path of directory containing images for current subject subject
        # sample subject_dir_path = "training-data/s1"
        subject_dir_path = data_folder_path + "/" + dir_name
        
        # get the images names that are inside the given subject directory
        subject_images_names = os.listdir(subject_dir_path)
        
        # ------STEP-3--------
        # go through each image name, read image,
        # detect face and add face to list of faces
        for image_name in subject_images_names:
            # ignore system files like .DS_Store
            if image_name.startswith("."):
                continue;
            
            # build image path
            # sample image path = training-data/s1/1.pgm
            image_path = subject_dir_path + "/" + image_name
            
            # read image
            image = cv2.imread(image_path)
            
            # display an image window to show the image
            cv2.imshow("Training on image...", image)
            cv2.waitKey(100)
            # detect face
            # detect face
            face, rect = detect_face(image)
        
        # ------STEP-4--------
        # for the purpose of this tutorial
        # we will ignore faces that are not detected
            if face is not None:
                # add face to list of faces
                faces.append(face)
                # add label for this face
                labels.append(label)
            
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            cv2.destroyAllWindows()
    
    return faces, labels

# function to draw rectangle on image
# according to given (x, y) coordinates and
# given width and heigh
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


# function to draw text on give image starting from
# passed (x, y) coordinates.
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

# this function recognizes the person in image passed
# and draws a rectangle around detected face with name of the
# subject
def predict(test_img):
    # make a copy of the image as we don't want to change original image
    img = test_img.copy()
    # detect face from the image
    face, rect = detect_face(img)
    #print(face)
    
    # predict the image using our face recognizer
    label = face_recognizer.predict(face)
    print(label)
    # get name of respective label returned by face recognizer
    label_text = labels[label[0]] #subjects[label]
    
    # draw a rectangle around face detected
    draw_rectangle(img, rect)
    # draw name of predicted person
    # draw_text(img, label_text, rect[0], rect[1] - 5)
    
    return img

def do_processing():
    global faces
    global labels
    
    # let's first prepare our training data
    # data will be in two lists of same size
    # one list will contain all the faces
    # and the other list will contain respective labels for each face
    print("Preparing data...")
    faces, labels = prepare_training_data("faces/train")
    print("Data prepared")
    # print total faces and labels
    print("Total faces: ", len(faces))
    print("Total labels: ", len(labels))
    print(labels)
    np.save('faces.npy', faces)
    np.save('labels.npy', labels)

def do_training():
    global faces
    global labels
    global face_recognizer
    
    faces = np.load('faces.npy')
    labels = np.load('labels.npy')
    # create our LBPH face recognizer
    face_recognizer = cv2.createLBPHFaceRecognizer()
    # or use EigenFaceRecognizer by replacing above line with
    #face_recognizer = cv2.face.createEigenFaceRecognizer()
    # or use FisherFaceRecognizer by replacing above line with
    #face_recognizer = cv2.face.createFisherFaceRecognize()
    
    #face_recognizer = cv2.face.createFisherFaceRecognize()
    #face_recognizer = cv2.face_EigenFaceRecognizer.create()
    #face_recognizer = cv2.face_LBPHFaceRecognizer.create()
    face_recognizer.train(faces, np.array(labels))

def do_prediction():
    global faces
    global labels
    global face_recognizer
    
    print("Predicting images...")
    
    test_files = [{'title':'one', 'path':'faces/test.jpg'},
    {'title':'two', 'path':'faces/test1.jpg'},
    {'title':'three', 'path':'faces/test2.jpg'},
    {'title':'four', 'path':'faces/test3.jpg'},
    #{'title':'five', 'path':'faces/test4.jpg'},
    {'title':'six', 'path':'faces/test5.jpg'}]
    
    for pair in test_files:
        #load test images
        test_img_temp = cv2.imread(pair['path'])
        pair['img'] = test_img_temp
        #perform a prediction
        pair['predict'] = predict(test_img_temp)
    
    print("Prediction complete")
    
    for pair in test_files:
        #display all images
        cv2.imshow(pair['title'], pair['predict'])
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


