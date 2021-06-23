# $ pip install pdf2docx
from pdf2docx import Converter
pdf_file = 'D:/gitvip/python3_template/model/file/如何系统思考 by 邱昭良 [邱昭良] (z-lib.org).pdf'
docx_file = './sample.docx'
# https://dothinking.github.io/pdf2docx/quickstart.convert.html


# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()
