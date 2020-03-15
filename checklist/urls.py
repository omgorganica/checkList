from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import index, inside_vehicle_type, questionnaire_new, result_list, specific_result_id, result_vehicle_type, result_vehicle_id, result_by_user


urlpatterns = [
    path('', index, name='index'),
    path('vehicles/', inside_vehicle_type, name='inside_vehicle_type'),
    path('vehicles/questionnaire/new/', questionnaire_new, name='questionnaire_new'),
    path('result/', result_list, name='result'),
    path('specific_result/', specific_result_id, name='specific_result_id'),
    path('result_vehicle_type/', result_vehicle_type, name='result_vehicle_type'),
    path('result_vehicle_id/', result_vehicle_id, name='result_vehicle_id'),
    path('result_by_user/', result_by_user, name='result_by_user'),
    path('accounts/', include('django.contrib.auth.urls'))

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)