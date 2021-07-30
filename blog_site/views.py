from django.shortcuts import render,redirect

from django.views import generic

from .models import Post, Document

from django.conf import settings

from django.core.files.storage import FileSystemStorage

from .forms import DocumentForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name='index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name='post_detail.html'

#def simple_upload(request):
  #  if request.method == 'POST' and request.FILES['myfile']:
   #     myfile = request.FILES['myfile']
   #     fs = FileSystemStorage()
    #    filename = fs.save(myfile.name, myfile)
     #   uploaded_file_url = fs.url(filename)
      #  return render(request,'/simple_upload.html', {
       #     'uploaded_file_url': uploaded_file_url
        #})
    #return render(request,'/simple_upload.html')

def model_form_upload(request):
    document_name = Document()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context= {
                'object':Document.objects.all()
            }
            return render(request,'file_upload_disp.html', context)
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })
