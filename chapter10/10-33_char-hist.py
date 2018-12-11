# Liang 10.33
from tkinter import *
import random

class CharHistogram:
    def __init__(self):
        NUMOFCHARS = 26
        self.width = 800
        self.height = 400
        self.canvasPadx = -40
        window = Tk()
        window.title('Histogram: Random Character Counts')

        # Canvas
        frame1 = Frame(window)
        frame1.pack()
        self.canvas = Canvas(frame1, width=self.width, height=self.height,
                             bd=self.canvasPadx, bg='white')
        self.canvas.pack()

        # a-z Character Labels
        frame2 = Frame(window)
        frame2.pack()
        for i in range(NUMOFCHARS):
            Label(frame2, text=chr(ord('a')+i)).grid(row=1, column=i+1, padx=self.width//100)

        # Button
        frame3 = Frame(window)
        frame3.pack()
        Button(frame3, text='Display Histogram', command=self.displayHist).pack()
        window.mainloop()
        
    def displayHist(self):
        self.clearCanvas()
        WSIZE = self.width/27.8
        HSIZE = self.height/7
        barWidth = self.width/WSIZE
        counts = 26 * [0]
        chars = []
        
        # Generate and count occurences of random generated chars
        for i in range(1000):
            chars.append(chr(97 + int(random.random() * (ord('z') - ord('`'))))) # '`' char before 'a'
        for j in range(len(chars)):
            counts[ord(chars[j]) - ord('a')] += 1
            
        # Draw histogram
        for k in range(len(counts)):
            self.canvas.create_line(barWidth*k, self.height,
                                    barWidth*k, self.height-self.height//HSIZE*counts[k], tags='line')
            self.canvas.create_line(barWidth*k, self.height-self.height//HSIZE*counts[k],
                                    barWidth*(k+1), self.height-self.height//HSIZE*counts[k], tags='line')
            self.canvas.create_line(barWidth*(k+1), self.height-self.height//HSIZE*counts[k],
                                    barWidth*(k+1), self.height, tags='line')

    def clearCanvas(self):
        self.canvas.delete('line')

CharHistogram()

    
