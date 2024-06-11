from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Course
from .models import Lesson
from .models import UserProfile

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def home(request):
    return render(request, 'Home.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user.save()
         # Creating the user profile
        user_profile = UserProfile(user=user, role=role)
        user_profile.save()
        return redirect('studentLogin')

    return render(request, 'studentSignup.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('studentHome')

    return render(request, 'studentLogin.html')

def studentHome(request):
    search_query = request.GET.get('search', '')

    if search_query:
        course_data = Course.objects.filter(course_name__icontains=search_query)
    else:
        course_data = Course.objects.all()

    paginator = Paginator(course_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'studentHome.html', { 'page_obj': page_obj, 'search_query': search_query })

 
def teacherSignup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user.save()
         # Creating the user profile
        user_profile = UserProfile(user=user, role=role)
        user_profile.save()
        return redirect('teacherLogin')

    return render(request, 'teacherSignup.html')

def teacherLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('teacherHome')

    return render(request, 'teacherLogin.html')

def teacherHome(request):
    return render(request, 'teacherHome.html')

@login_required
def course_list(request):
    user = request.user
    search_query = request.GET.get('search', '')

    if search_query:
        course_data = Course.objects.filter(teacher_id=user, course_name__icontains=search_query)
    else:
        course_data = Course.objects.filter(teacher_id=user)

    paginator = Paginator(course_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'course_list.html', { 'page_obj': page_obj, 'search_query': search_query })



@login_required
def add_course(request):
    if request.method == 'POST':
        course_name = request.POST['course_name']
        description = request.POST['description']
        duration = request.POST['duration']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        category = request.POST['category']
        level = request.POST['level']
        price = request.POST['price']
        language = request.POST['language']     

        teacher_id = request.user

        courseData = Course(course_name=course_name, description=description,duration=duration,start_date=start_date,end_date=end_date, category=category,level=level,price=price,language=language,teacher_id=teacher_id)
        courseData.save()
        return redirect('course_list')

    return render(request,'add_course.html')


def edit_course_data(request, pk):
    course = get_object_or_404(Course, id=pk)

    if request.method == 'POST':
        course.course_name = request.POST['course_name']
        course.description = request.POST['description']
        course.duration = request.POST['duration']
        course.start_date = request.POST['start_date']
        course.end_date = request.POST['end_date']
        course.category = request.POST['category']
        course.level = request.POST['level']
        course.price = request.POST['price']
        course.language = request.POST['language']   
        course.save()

        return redirect('course_list')

    return render(request, 'edit_course_data.html', {'edit': course})

def DeleteData(request,pk):
    delete=Course.objects.get(id=pk)
    delete.delete()
    return redirect('course_list')


@login_required
def lesson_list(request):
    user = request.user
    search_query = request.GET.get('search', '')

    if search_query:
        lesson_data = Lesson.objects.filter(teacher=user, title__icontains=search_query)
    else:
        lesson_data = Lesson.objects.filter(teacher=user)

    paginator = Paginator(lesson_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'lesson_list.html', { 'page_obj': page_obj, 'search_query': search_query })



@login_required
def add_lesson(request):
    if request.method == 'POST':
        content = request.POST['content']
        title = request.POST['title']
        course_id = request.POST['course_id'] 
        teacher = request.user
        course = Course.objects.get(id=course_id)
 

        lessonData = Lesson(content=content, title=title, course_id=course, teacher=teacher)
        lessonData.save()
        return redirect('lesson_list')
    
    return render(request, 'add_lesson.html')



def edit_lesson_data(request, pk):
    lesson = get_object_or_404(Lesson, id=pk)

    if request.method == 'POST':
        lesson.lesson_name = request.POST['lesson_name']
        lesson.description = request.POST['description']
        lesson.duration = request.POST['duration']
        lesson.start_date = request.POST['start_date']
        lesson.end_date = request.POST['end_date']
        lesson.category = request.POST['category']
        lesson.level = request.POST['level']
        lesson.price = request.POST['price']
        lesson.language = request.POST['language']   
        lesson.save()

        return redirect('lesson_list')

    return render(request, 'edit_lesson_data.html', {'edit': lesson})

def DeleteLessonData(request,pk):
    delete=Lesson.objects.get(id=pk)
    delete.delete()
    return redirect('lesson_list')