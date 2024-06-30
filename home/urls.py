from django.urls import path
from .views import (
    home,
    shopkeeper,
    SubmitPDF,
    PDFDatabase_form,
    complete_order,
    generate_front_page,
    assignment_front_page,
    lab_front_page,
    generate_lfront_page,
    grammar_check_view,
    check_assignment_plagirism,
    bkash,
    print_shop,
    tools,
    profile,
    qa,
    course,
    academic_courses,
    professional_courses,
    course_details,

)

urlpatterns = [

    path('', home, name='home'),
    path('print_shop', print_shop, name='print_shop'),
    path('tools', tools, name='tools'),
    path('profile', profile, name='profile'),
    path('qa', qa, name='qa'),
    path('shopkeeper', shopkeeper, name='shopkeeper'),
    path('SubmitPDF/<int:pk>/', SubmitPDF.as_view(), name='SubmitPDF'),
    path('PDFDatabase_form', PDFDatabase_form, name='PDFDatabase_form'),
    path('complete_order/<int:order_id>/', complete_order, name='complete_order'),
    path('generate_front_page/', generate_front_page, name='generate_front_page'),
    path('assignment_front_page/', assignment_front_page, name='assignment_front_page'),
    path('lab_front_page/', lab_front_page, name='lab_front_page'),
    path('generate_lfront_page/', generate_lfront_page, name='generate_lfront_page'),
    path('grammar_check_view/', grammar_check_view, name='grammar_check_view'),
    path('check_assignment_plagirism/', check_assignment_plagirism, name='check_assignment_plagirism'),
    path('bkash/', bkash, name='bkash'),
    path('course/', course, name='course'),
    path('academic_courses/', academic_courses, name='academic_courses'),
    path('professional_courses/', professional_courses, name='professional_courses'),
    path('course_details/', course_details, name='course_details'),

]