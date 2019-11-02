import cv2, cvlib, tensorflow

class Imager:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)

    def get_img(self):
        s, img = self.cam.read()
        faces, confidences = cvlib.detect_face(img)
        faceCrop = faces[confidences.index(max(confidences))]

        width = faceCrop[2] - faceCrop[0]
        height = faceCrop[3] - faceCrop[1]

        if width > height:
            centerV = faceCrop[1] + height / 2
            faceCrop[1] = int(centerV - width / 2)
            faceCrop[3] = int(centerV + width / 2)
        else:
            centerX = faceCrop[0] + width / 2
            faceCrop[0] = int(centerX - height / 2)
            faceCrop[2] = int(centerX + height / 2)

        img = img[faceCrop[1]:faceCrop[3], faceCrop[0]:faceCrop[2]]
        img = cv2.resize(img, (128, 128))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        #cv2.imwrite("filename.jpg",img)
        #cv2.namedWindow("cam-test")
        #cv2.imshow("cam-test",img)
        return img
