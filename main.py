from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter
import PIL
import cv2
from tkinter import filedialog

#
class App:
    def __init__(self):
        super().__init__()
        self.root = tkinter.Tk()
        self.root.geometry("400x400")
        self.root.minsize(800,500)
        self.root.maxsize(800,500)
        self.panelA = None
        self.panelB = None
        # initialize the window toolkit along with the two image panels
        def borderprocessing():
            return 1

        def segmentation():
            return 1
            # gray = cv2.cvtColor(panelA.image, cv2.COLOR_BGR2GRAY)
            # ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        def select_image():
            path = filedialog.askopenfilename()
            # ensure a file path was selected
            if len(path) > 0:
                # load the image from disk, convert it to grayscale, and detect
                # edges in it
                image = cv2.imread(path)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                edged = cv2.Canny(gray, 50, 100)
                # OpenCV represents images in BGR order; however PIL represents
                # images in RGB order, so we need to swap the channels
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                # convert the images to PIL format...
                image = Image.fromarray(image)
                edged = Image.fromarray(edged)
                # ...and then to ImageTk format
                image = ImageTk.PhotoImage(image)
                edged = ImageTk.PhotoImage(edged)
                # if the panels are None, initialize them
                if self.panelA is None or self.panelB is None:
                    # the first panel will store our original image
                    self.panelA = Label(image=image)
                    self.panelA.image = image
                    self.panelA.pack(side="left", padx=10, pady=10)
                    # while the second panel will store the edge map
                    self.panelB = Label(image=edged)
                    self.panelB.image = edged
                    self.panelB.pack(side="right", padx=10, pady=10)
                    self.segmbtn['state'] = tkinter.NORMAL
                    self.brdrbtn['state'] = tkinter.NORMAL
                # otherwise, update the image panels
                else:
                    # update the pannels
                    self.panelA.configure(image=image)
                    self.panelB.configure(image=edged)
                    self.panelA.image = image
                    self.panelB.image = edged

        self.chooseImgBtn = Button(self.root, text="Select an image", command=select_image)
        self.segmbtn = Button(self.root, text="Segmentation", command=segmentation)
        self.brdrbtn = Button(self.root, text="Borderline processing", command=borderprocessing)
        self.chooseImgBtn.pack(expand=1, fill=X)
        self.segmbtn.pack(expand=1, fill=X)
        self.brdrbtn.pack(expand=1, fill=X)
        if self.panelA is None:
            self.segmbtn['state'] = tkinter.DISABLED
            self.brdrbtn['state'] = tkinter.DISABLED
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.root.title("Yo")
    app.root.mainloop()
