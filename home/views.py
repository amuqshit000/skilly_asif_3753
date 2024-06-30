from django.shortcuts import render
from django.views.generic import DetailView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .models import ShopList, PDFDatabase
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
import requests
from django.shortcuts import render
import PyPDF2
import spacy
from .models import CourseDatabase


def home(request):
    return render(request, "index.html")


def print_shop(request):
    shop = ShopList.objects.all()
    return render(request, "printshop.html", {'shop': shop})


def tools(request):
    return render(request, "tools.html")


def profile(request):
    list = PDFDatabase.objects.filter(senderusername=request.user)
    return render(request, "profile.html", {'list': list})


def qa(request):
    return render(request, "qa.html")


def shopkeeper(request):
    order = PDFDatabase.objects.filter(selectedshopusername=request.user)
    shop = ShopList.objects.filter(username=request.user)
    return render(request, "shopkeeper.html", {'order': order, 'shop': shop})


class SubmitPDF(DetailView):
    model = ShopList
    template_name = "submit_pdf.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(SubmitPDF, self).get_context_data(*args, **kwargs)
    #     context['comment_list'] = comment.objects.all()
    #     return context


def bkash(request):
    if request.method == "POST":
        transaction = request.POST['transaction']
        total_cost = request.POST['total_cost']
        total_page = request.POST['total_page']
        sender_name = request.POST['sender_name']
        email = request.POST['sender_email']

        # Get the last submitted PDFDatabase object for the current user
        last_pdf_database = PDFDatabase.objects.filter(
            senderusername=request.user.username).last()
        last_pdf_database.transaction = transaction
        last_pdf_database.total_cost = total_cost
        last_pdf_database.total_page = total_page
        last_pdf_database.save()

        # Redirect to the previous page
        messages.success(
            request, "Your file is successfully submitted. Please wait for payment confirmation. You can check the progress in your profile. Total pages: {} Total Cost: {} TAKA.".format(
                total_page, total_cost)

        )
       
     
        return redirect('profile')


def PDFDatabase_form(request):
    if request.method == "POST":
        senderusername = request.POST['username']
        sendername = request.POST['name']
        senderemail = request.POST['email']
        senderphone = request.POST['phone']
        selectedshopusername = request.POST['selectedshopusername']
        selectshopname = request.POST['selectshopname']
        file = request.FILES['file']

        # Save the uploaded file
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)

        # Get the file path
        filepath = fs.path(filename)

        # Count the total number of pages
        total_page = 0
        with open(filepath, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            total_page = len(pdf_reader.pages)
        total_cost = 0
        total_cost = total_page * 4

        # Save the file information
        pdf_database = PDFDatabase(
            senderusername=senderusername,
            sendername=sendername,
            senderemail=senderemail,
            senderphone=senderphone,
            selectedshopusername=selectedshopusername,
            selectshopname=selectshopname,
            file=filename,
            total_page=total_page  # Save the total pages count
        )
        pdf_database.save()

        return render(request, "bkash.html", {"total_cost": total_cost, "total_page": total_page, "sender_name": sendername, "sender_email": senderemail})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def complete_order(request, order_id):
    order = PDFDatabase.objects.get(pk=order_id)
    order.status = True
    order.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# AI Tools FREE


def assignment_front_page(request):
    return render(request, "assignmentfrontpage.html")


def lab_front_page(request):
    return render(request, "labfrontpage.html")


def check_assignment_plagirism(request):
    return render(request, "plagirism_checking.html")


def generate_front_page(request):
    if request.method == 'POST':
        # Retrieve the data from the template
        topic = request.POST.get('topic')
        course_code = request.POST.get('course_code')
        course_title = request.POST.get('course_title')
        course_teacher_name = request.POST.get('course_teacher_name')
        course_teacher_designation = request.POST.get(
            'course_teacher_designation')
        course_teacher_department = request.POST.get(
            'course_teacher_department')
        name = request.POST.get('name')
        iid = request.POST.get('iid')
        department = request.POST.get('department')
        date = request.POST.get('date')

        context = {
            'topic': topic,
            'course_code': course_code,
            'course_title': course_title,
            'course_teacher_name': course_teacher_name,
            'course_teacher_designation': course_teacher_designation,
            'course_teacher_department': course_teacher_department,
            'name': name,
            'iid': iid,
            'department': department,
            'date': date,
        }

    return render(request, "gaf.html", context)


def generate_lfront_page(request):
    if request.method == 'POST':
        # Retrieve the data from the template
        topic = request.POST.get('topic')
        course_code = request.POST.get('course_code')
        course_title = request.POST.get('course_title')
        course_teacher_name = request.POST.get('course_teacher_name')
        course_teacher_designation = request.POST.get(
            'course_teacher_designation')
        course_teacher_department = request.POST.get(
            'course_teacher_department')
        name = request.POST.get('name')
        iid = request.POST.get('iid')
        department = request.POST.get('department')
        date = request.POST.get('date')

        context = {
            'topic': topic,
            'course_code': course_code,
            'course_title': course_title,
            'course_teacher_name': course_teacher_name,
            'course_teacher_designation': course_teacher_designation,
            'course_teacher_department': course_teacher_department,
            'name': name,
            'iid': iid,
            'department': department,
            'date': date,
        }

    return render(request, "glf.html", context)


def grammar_check_view(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')

        # Make a request to the LanguageTool API
        url = 'https://api.textgears.com/check.php'
        params = {
            'text': text,
            'key': 'juM8JqYjEJSVhPUM',
            'tool': 'grammar',
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception if the request was unsuccessful
            data = response.json()

            # Process the API response
            if 'errors' in data:
                corrections = []
                corrected_passage = text

                for error in data['errors']:
                    incorrect_word = error['bad']
                    if 'better' in error and error['better']:
                        correct_word = error['better'][0]
                    else:
                        correct_word = '[No suggestions found]'
                    correction = {
                        'incorrect': incorrect_word,
                        'correct': correct_word
                    }
                    corrections.append(correction)

                    # Replace incorrect word with correct word in the corrected passage
                    corrected_passage = corrected_passage.replace(
                        incorrect_word, correct_word)

                if corrections:
                    message = 'Grammar corrections have been made.'
                else:
                    message = 'Everything is correct!'
            else:
                corrections = []
                message = 'No grammar issues found.'
                corrected_passage = text

            return render(request, 'plagirism_checking.html', {'message': message, 'corrections': corrections, 'corrected_passage': corrected_passage})

        except requests.exceptions.RequestException as e:
            message = f'Error: {str(e)}'
            return render(request, 'plagirism_checking.html', {'message': message, 'corrections': [], 'corrected_passage': ''})

    return render(request, 'plagirism_checking.html')


def course(request):
    return render(request, "course.html")


def academic_courses(request):
    academic_courses_list = CourseDatabase.objects.all()
    return render(request, "academic_courses.html", {"academic_courses": academic_courses_list})


def professional_courses(request):
    professional_courses_list = CourseDatabase.objects.all()
    return render(request, "professional_courses.html", {"professional_courses": professional_courses_list})


def course_details(request):
    if request.method == "GET":
        course_name = request.GET['course_name']
    course_list = CourseDatabase.objects.filter(course_name=course_name)
    return render(request, "course_details.html", {"course": course_list})
