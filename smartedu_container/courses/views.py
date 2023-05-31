from django.shortcuts import render
from . models import Course

# Create your views here.
def course_list(request):
    course_list = Course.objects.all().order_by('-date')
    print(course_list[0])
    context = {'courses': course_list}
    
    return render(request, 'courses.html', context)