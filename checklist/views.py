from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests import auth
from .forms import QuestionnaireForm
from .models import VehicleUnit, VehicleType, Questionnaire
from datetime import datetime
from django.core.paginator import Paginator


def index(request):
    vehicle_type_list = VehicleType.objects.all()
    params = {
        'vehicle_type_list': vehicle_type_list,
    }
    return render(request, 'checklist/index.html', params)


def inside_vehicle_type(request):
    vehicle_type = request.GET.get('vehicle_type')
    vehicles_list = VehicleUnit.objects.filter(vehicle_type=vehicle_type)
    vehicle_type_name = VehicleType.objects.get(id=vehicle_type)

    params = {
        'vehicles_list': vehicles_list,
        'vehicle_type_name':vehicle_type_name
    }
    return render(request, 'checklist/inside_vehicle_type.html', params)


def questionnaire_new(request):
    vehicle_type = request.GET.get('vehicle_type')
    vehicle_type_name = VehicleType.objects.get(id=vehicle_type)
    vehicle_registred_number = request.GET.get('vehicle_registred_number')
    if request.method == "POST":
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.registred_number = vehicle_registred_number
            post.vehicle_type = vehicle_type_name
            post.published_date = datetime.now()
            post.save()
            return redirect('index')
    else:
        form = QuestionnaireForm()

    return render(request, 'checklist/questionnaire.html', {'form': form, 'vehicle_type_name':vehicle_type_name})


def result_list(request):
    result = Questionnaire.objects.all()
    paginator = Paginator(result, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    params = {
        'result': result,
        'contacts': contacts,
    }
    return render(request, 'checklist/result.html', params)


def specific_result_id(request):
    result_id = request.GET.get('result_id')
    vehicle_type_name = VehicleType.objects.get(id=result_id)

    result = Questionnaire.objects.get(id=result_id)
    params = {
        'result': result,
    }
    return render(request, 'checklist/specific_result_id.html', params)


def result_vehicle_type(request):
    vehicle_type = request.GET.get('vehicle_type')
    result = Questionnaire.objects.filter(vehicle_type=vehicle_type)
    params = {
        'result': result,
        'vehicle_type': vehicle_type
    }
    return render(request, 'checklist/result_vehicle_type.html', params)


def result_vehicle_id(request):
    registred_number = request.GET.get('registred_number')
    result = Questionnaire.objects.filter(registred_number=registred_number)
    params = {
        'result': result,
        'registred_number': registred_number,
    }
    return render(request, 'checklist/result_vehicle_id.html', params)


def result_by_user(request):
    user = request.GET.get('user')
    result = Questionnaire.objects.filter(user=user)
    params = {
        'result': result,
        'user': user
    }
    return render(request, 'checklist/result_by_user.html', params)
