from fpdf import FPDF
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 24)
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')
    def add_shirt_image(self):
        self.image('shirtificate.png',x=0, y=0)
    def add_name(self, name):
        self.set_font('Arial', 'B', 36)
        self.set_text_color(255, 255, 255)
        self.set_xy(10, 100)
        self.cell(0, 10, name, 0, 0, 'C')

def create_shirt(name):
    pdf = PDF(orientation="P", format='A4')
    pdf.add_page()
    pdf.add_shirt_image()
    pdf.add_name(name)
    pdf.output('shirtificate.pdf')

if __name__ == '__main__':
    name = input("Enter your name: ")
    create_shirt(name)
