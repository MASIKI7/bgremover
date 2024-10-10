from django.shortcuts import render, redirect
from django.http import HttpResponse  # Import HttpResponse
from rembg import remove
from PIL import Image
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
import os


def removebg(request):
    URL = "http://127.0.0.1:8000/images/"
    if request.method == 'POST':
        form = request.FILES['image']
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        print(f'Uploaded file path: {fs.path(filename)}')
        input_path = fs.path(filename)
        file_names, file_extension = os.path.splitext(image.name)  # Split the file name and extension
        print(f'Uploaded file name: {filename}')
        output_path = "myapp/static/images/"+file_names+"removebg-innoAI.png"
        input_paths =  "myapp/static/images/"+filename
        inputs = Image.open(input_path)
        output = remove(inputs)
        saveinput = filename
        inputs.save(input_paths)
        output.save(output_path)
        remove_file = "images/"+file_names+"removebg-innoAI.png"
        print("LAST ONE I THINK: "+uploaded_file_url)
        context = {
            'output': remove_file
            'input':
        }


        return render(request,'bgremove.html', context)
        
    else:
        print("Bye")

def upload_success(request):
    return render(request, 'upload_success.html')



def home(request):
    # input_path = '/home/janmferoyal/Documents/DR BANZI.jpeg'
    # output_path = "output.png"
    # inputs = Image.open(input_path)
    # output = remove(inputs)
    # output.save(output_path)
    return render(request,  'home.html')
