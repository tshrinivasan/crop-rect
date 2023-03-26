import cv2
import numpy as np
import uuid  
from argparse import ArgumentParser
from pdf2image import convert_from_path
from PyPDF2 import PdfWriter, PdfReader
import os

output_dir = "media"

def get_filename(path):
    print("path",os.path.basename(path))
    name = os.path.basename(path)
    return name.split('.')[0]


def crop_img(input_img):
    im = cv2.imread(input_img, 0)
    im1 = cv2.imread(input_img)

    output_dir = os.path.join(os.getcwd(),"output",get_filename(input_img))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  
    

    ret,thresh_value = cv2.threshold(im,180,255,cv2.THRESH_BINARY_INV)

    kernel = np.ones((5,5),np.uint8)
    dilated_value = cv2.dilate(thresh_value,kernel,iterations = 1)

    contours, hierarchy = cv2.findContours(dilated_value,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cordinates = []
    count = 0
    for cnt in contours:
        if cv2.contourArea(cnt) > 1000000 and cv2.contourArea(cnt) < 10000000:
            count+=1
            x,y,w,h = cv2.boundingRect(cnt)
            cordinates.append((x,y,w,h))
            #bounding the images
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            crop_img = im1[y:y+h, x:x+w]
            out_crop_img_path = os.path.join(output_dir,f"{get_filename(input_img)}_{count}.jpg")
            cv2.imwrite(out_crop_img_path,crop_img)




def convert_pdf_to_images(input_file):

    inputpdf = PdfReader(open(input_file, "rb"))
    for i in range(len(inputpdf.pages)):
        output = PdfWriter()
        output.add_page(inputpdf.pages[i])
        directory = os.path.join(os.getcwd(),output_dir,get_filename(input_file))

        if not os.path.exists(directory):
            os.makedirs(directory) 
            os.makedirs(os.path.join(directory,"img")) 

        output_filename = os.path.join(directory,f"{get_filename(input_file)}-{i}.pdf")

        with open(output_filename, "wb") as outputStream:
            output.write(outputStream)

        output_filename_img = os.path.join(directory,"img",f"{get_filename(output_filename)}.jpg")
        images = convert_from_path(output_filename)
        images[0].save(output_filename_img, 'JPEG')
        crop_img(output_filename_img)
    return directory,True

        # for i in range(len(images)):
        #     # Save pages as images in the pdf
        #     images[i].save('page'+ str(i) +'.jpg', 'JPEG')




def cropimage(input_file):
    if not output_file:
        parts = input_file.split('.')
        assert len(parts) > 1, "Can't automatically choose output name if there's no file extension!"
        output_file = '.'.join([*parts[:-1], 'cropped', parts[-1]])




if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--input', action='store', type=str,help="pdf file to autocrop")
    args = parser.parse_args()
    convert_pdf_to_images(args.input)