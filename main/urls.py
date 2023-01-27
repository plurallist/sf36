from django.urls import path
from . import views

urlpatterns = [
    path("pacjenci/", views.pacjenci, name="pacjenci"),
    path("panel/", views.panel, name="panel"),
    path("new_sf36/", views.new_sf36, name="new_sf36"),
    path("results_sf36/", views.results_sf36, name="results_sf36"),
    path("", views.start, name="start"),
    path("patient/", views.choose_patient, name="patient"),
    path("create_patient/", views.create_patient, name="create_patient"),
    path("patient_created/", views.patient_created, name="patient_created"),
    path("your_results/", views.your_results, name="your_results"),
    path("all_results/", views.all_results, name="all_results"),
]