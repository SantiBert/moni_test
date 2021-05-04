from django.urls import path
from .views import (LendingCreateView,
                    AdministrationView,
                    LendingUpdateView,
                    LendingDeleteView)

urlpatterns = [
    path('', LendingCreateView.as_view(), name="index"),
    path('administration/', AdministrationView.as_view(), name="administration"),
    path('administration/update/<slug:slug>/',
         LendingUpdateView.as_view(), name="updateLending"),
    path('administration/delete/<slug:slug>/',
         LendingDeleteView.as_view(), name="deleteLending")
]
