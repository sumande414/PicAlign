from PIL import Image
import docx
from docx.shared import Inches,Cm


def generate_docx(filepaths, preset):
    doc = docx.Document()

    for sec in doc.sections:
        sec.top_margin = Cm(0.5)
        sec.bottom_margin = Cm(0.5)
        sec.left_margin = Cm(0.5)
        sec.right_margin = Cm(0.5)

    para = doc.add_paragraph()
    run = para.add_run()



    for file in filepaths:
        img = Image.open(file)
        k = img.width/img.height
        run.add_picture(file,width=Inches(preset*k), height=Inches(preset))
        run.add_text(" ")

    doc.save("PicAlign_output.docx")



