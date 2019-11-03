import cv2, cvlib, tensorflow

class Imager:
    def __init__(self):
        print('Initializing Imager')
        self.cam = cv2.VideoCapture(0)

    def capture_img(self):
        s, img = self.cam.read()
        return img

    def open_img(self, fileName):
        return cv2.imread(fileName)

    def process_img(self, img):
        faces, confidences = cvlib.detect_face(img)

        if not len(confidences):
            return None
        
        faceCrop = faces[confidences.index(max(confidences))]
        width = faceCrop[2] - faceCrop[0]
        height = faceCrop[3] - faceCrop[1]
        
        #"""
        zoom = 0.1
        faceCrop[0] += width * zoom
        faceCrop[1] += height * zoom
        faceCrop[2] -= width * zoom
        faceCrop[3] -= height * zoom
        width = faceCrop[2] - faceCrop[0]
        height = faceCrop[3] - faceCrop[1]

        idealRatio = 3/4
        # Too narrow, expand width to .75 height
        if width / height > idealRatio:
            centerX = faceCrop[0] + width / 2
            faceCrop[0] = centerX - height * idealRatio / 2
            faceCrop[2] = centerX + height * idealRatio / 2
            
        # Too wide, expand height
        else:
            centerV = faceCrop[1] + height / 2
            faceCrop[1] = centerV - width / idealRatio / 2
            faceCrop[3] = centerV + width / idealRatio / 2
            
        """
        if width > height:
            centerV = faceCrop[1] + height / 2
            faceCrop[1] = centerV - width / 2
            faceCrop[3] = centerV + width / 2
        else:
            centerX = faceCrop[0] + width / 2
            faceCrop[0] = centerX - height / 2
            faceCrop[2] = centerX + height / 2
        """
        
        if min(faceCrop) < 0 or faceCrop[2] >= len(img[0]) or faceCrop[3] >= len(img):
            return None

        faceCrop = [int(dimension) for dimension in faceCrop]        
        img = img[faceCrop[1]:faceCrop[3], faceCrop[0]:faceCrop[2]]
        #img = cv2.resize(img, (128, 128))
        #img = cv2.resize(img, (96, 128))
        img = cv2.resize(img, (192, 256))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        return img

    def log_img(self, img, fileName):
        cv2.imwrite(fileName, img)

    def show_img(self, img):
        cv2.imshow("MLTonin",img)
        cv2.waitKey(1)
