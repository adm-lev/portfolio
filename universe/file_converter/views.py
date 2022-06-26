from django.shortcuts import render
from django.views import generic
from django.core.files.storage import FileSystemStorage
import os
import cv2
import pytesseract
from pdf2image import convert_from_path
import fitz
import docx
from django.conf import settings



MEDIA = r'/home/devlev/portfolio/universe/media'

def index(request):
    """

    :param request:
    :return:
    """

    return render(request, 'file_converter/index.html')


def load_files(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['my_file1']
        fs = FileSystemStorage()
        filename = fs.save(os.path.join('converter', 'files', file.name), file)
        file_url = fs.url(filename)
        name = file.name
        extention = ''
        res_text = ''

        if name.endswith('docx'):
            extention = 'word document'
        elif name.endswith('pdf'):
            pages = convert_from_path(filename, 100)
            pages[0].save('out.jpg', 'JPEG')

            imgcv = cv2.imread(request.FILES['my_file1'])

            imgcv = cv2.cvtColor(imgcv, cv2.COLOR_BGR2RGB)

            res_text = pytesseract.image_to_string(imgcv)

        elif name.endswith('jpeg'):
            # img = cv2.imread('/home/devlev/portfolio/universe/media/converter/files/222.jpeg')
            img = cv2.imread(os.path.join(settings.MEDIA_ROOT, 'converter/files/', file.name))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # cv2.imshow('Result', img)
            # cv2.waitKey(0)
            # print(img)
            res_text = pytesseract.image_to_string(img)

        return render(
            request,
            'file_converter/load_file.html',
            {
                'file_url': file_url,
                'file_name': file.name,
                'type': extention,
                'res_text': res_text,
            }
        )
    return render(request, 'file_converter/load_file.html')


def test():

    img = cv2.imread('/home/devlev/portfolio/universe/media/converter/files/111.jpeg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2.imshow('Result', img)
    # cv2.waitKey(0)

    return pytesseract.image_to_string(img)


def test2():
    file = fitz.open('/home/devlev/portfolio/universe/media/converter/files/clients.pdf')

    # doc = docx.Document()

    for pageNum, page in enumerate(file.pages(), start=1):
        text = page.get_text()
        print(text)
        # doc.add_paragraph(text)
        # doc.save('test.docx')
        if pageNum == 1:
            break

        return text



# test2()

