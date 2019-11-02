from imager import Imager
#from other import Model

def main():
    myImager = Imager()
    #myModel = Model()
    while True: 
        img = myImager.get_img()
        if not img is None:
            myImager.show_img(img)
            #result = myModel.process(img)
        
if __name__ == '__main__':
    main()
