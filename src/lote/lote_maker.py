from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import TABLOID, A4
from reportlab.lib.utils import ImageReader
from lote.card_gen import CardGenerator
from copy import copy

from os.path import join
import argparse
import os
from os import system

from lote.templates.template_1 import Template1

class LoteMaker():

  def __init__(self):
    print('[ + ] LoteMaker running! [ + ]')

    self.args = self.parse_args()
    self.load_cards()
    self.load_template()
    #self.test()

    sets = []

    for i in range(0, 52):
      sets.append(CardGenerator(self.cards).generate_set())
    
    self.make(sets)
    #print(len(Template1.get_matrix()))
    #print(Template1.SLOTS_MATRIX)

  def make(self, sets):
      

    ratio = 730 / 440
    width = 59
    height = width * ratio

    output = PdfFileWriter()
    for index, set in enumerate(sets): # iterate sets to make the pages of pdf!
      packet = io.BytesIO()
      draw = canvas.Canvas(packet, pagesize=(450, 750))
      page_template = copy(self.pdf_template.getPage(0))

      for item in range(0, 16): # iterate the cards
        draw.drawImage(
          set[item].get('card'), 
          set[item].get('x'), 
          set[item].get('y'), 
          width=width,
          height=height)

      draw.save()

      packet.seek(0)
      new_pdf = PdfFileReader(packet)
      page_template.merge_page(new_pdf.getPage(0))

      output.addPage(page_template)
    
    output_stream = open(self.args.output, "wb")
    output.write(output_stream)
    output_stream.close()

    os.startfile(self.args.output)
        
    

  def test(self):
    packet = io.BytesIO()
    draw = canvas.Canvas(packet, pagesize=(450, 750))
    #draw.drawString(100, 100, "Hello world.")
    #draw.drawImage(img, 0, 0, width=65, preserveAspectRatio=True)
    ratio = 730 / 440
    width = 59
    height = width * ratio

    for i in range(0, 16):
      draw.drawImage(self.cards[i], Template1.SLOTS[i][0], Template1.SLOTS[i][1], width=width, height=height)
  

    '''
    draw.drawImage(ImageReader(self.cards[0]), 15.2, 16, width=width, height=height) #  [0, 3]
    draw.drawImage(ImageReader(self.cards[1]), 93.2, 16, width=width, height=height) #  [1, 3]
    draw.drawImage(ImageReader(self.cards[2]), 171.2, 16, width=width, height=height) # [2, 3]
    draw.drawImage(ImageReader(self.cards[3]), 249.2, 16, width=width, height=height) # [3, 3]

    draw.drawImage(ImageReader(self.cards[4]), 15.5, 126.886363, width=width, height=height) # [0, 2]
    draw.drawImage(ImageReader(self.cards[5]), 93.5, 126.886363, width=width, height=height) # [1, 2]
    draw.drawImage(ImageReader(self.cards[6]), 171.5, 126.886363, width=width, height=height) # [2, 2]
    draw.drawImage(ImageReader(self.cards[7]), 249.5, 126.886363, width=width, height=height) # [3, 2]

    draw.drawImage(ImageReader(self.cards[8]), 15.5, 237.772726, width=width, height=height) # [0, 1]
    draw.drawImage(ImageReader(self.cards[9]), 93.5, 237.772726, width=width, height=height) # [1, 1]
    draw.drawImage(ImageReader(self.cards[10]), 171.5, 237.772726, width=width, height=height) # [2, 1]
    draw.drawImage(ImageReader(self.cards[11]), 249.5, 237.772726, width=width, height=height) # [3, 1]

    draw.drawImage(ImageReader(self.cards[12]), 15.5, 349, width=width, height=height) # [0, 0]
    draw.drawImage(ImageReader(self.cards[13]), 93.5, 349, width=width, height=height) # [1, 0]
    draw.drawImage(ImageReader(self.cards[14]), 171.5, 349, width=width, height=height) # [2, 0]
    draw.drawImage(ImageReader(self.cards[15]), 249.5, 349, width=width, height=height) # [3, 0]
    '''

    draw.save()
    

    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    output = PdfFileWriter()
    
    page = self.pdf_template.getPage(0)
    page.merge_page(new_pdf.getPage(0))

    output.add_page(page)
    output_stream = open(self.args.output, "wb")
    output.write(output_stream)
    output_stream.close()

    os.startfile(self.args.output)

  def load_cards(self):
    print('[*] Cargando cartas...')

    if(not os.path.isdir(self.args.barajas)):
      print('[!] La carpeta {} no existe'.format(self.args.barajas))
      return
    
    self.cards = []
    for file in os.listdir(self.args.barajas):
      self.cards.append(join(self.args.barajas, file))

    print(f'[+] Cartas cargadas: {len(self.cards)}')

  def load_template(self):
    print('[*] Cargando plantilla...')
    
    if(not os.path.isfile(self.args.plantilla)):
      print('[!] La plantilla {} no existe'.format(self.args.plantilla))
      return

    self.pdf_template = PdfFileReader(open(self.args.plantilla, 'rb'))
    
  def parse_args(self):
    parser = argparse.ArgumentParser(description='Lote Maker')
    parser.add_argument('-b', '--barajas', help='Ruta de la carpeta que contiene las cartas', required=True)
    parser.add_argument('-p', '--plantilla', help='Ruta de la plantilla de las cartas', required=True)
    parser.add_argument('-o', '--output', help='Nombre del archivo que contendra las cartas generadas', required=True)
    parser.add_argument('-n', '--numero', help='Numero de cartas a generar', default=30)
    parser.add_argument('--nombre', help="Nombre de la novia")
    #parser.add_argument('--fecha', help="Fecha de la despedida de soltera")
    #parser.add_argument('--fecha-boda', help="Fecha de la boda")

    args = parser.parse_args()
    return args

if __name__ == '__main__':
  LoteMaker()