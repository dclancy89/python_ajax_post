from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, 'post/index.html')

def add_note(request):
	note = request.POST['note']
	post = '<div class="post">{}</div>'.format(note)
	return HttpResponse(post)
