from django.contrib import admin
from django.urls import path, include
from LMSapp import views
from LMSapp.views import home,signup,Login,studentHome
from LMSapp.views import teacherSignup,teacherLogin,teacherHome
from LMSapp.views import course_list,add_course,edit_course_data,DeleteData
from LMSapp.views import lesson_list,add_lesson,edit_lesson_data,DeleteLessonData
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('',views.home, name ='home'),
     path('studentSignup/',views.signup, name ='studentSignup'),
     path('studentLogin/',views.Login, name ='studentLogin'),
     path('studentHome',views.studentHome, name='studentHome'),

      path('teacherSignup/',views.teacherSignup, name ='teacherSignup'),
     path('teacherLogin/',views.teacherLogin, name ='teacherLogin'),
     path('teacherHome',views.teacherHome, name='teacherHome'),

     path('teacherHome/course_list',views.course_list, name='course_list'),
     path('teacherHome/course_list/add_course',views.add_course, name='add_course'),
     path('teacherHome/course_list/edit_course_data/<int:pk>', views.edit_course_data, name='edit_course_data'),
     path('teacherHome/course_list/DeleteData/<int:pk>', views.DeleteData, name='DeleteData'),

     path('teacherHome/lesson_list',views.lesson_list, name='lesson_list'),
      path('teacherHome/lesson_list/add_lesson',views.add_lesson, name='add_lesson'),
     path('teacherHome/lesson_list/edit_lesson_data/<int:pk>', views.edit_lesson_data, name='edit_lesson_data'),
     path('teacherHome/lesson_list/DeleteLessonData/<int:pk>', views.DeleteLessonData, name='DeleteLessonData'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)