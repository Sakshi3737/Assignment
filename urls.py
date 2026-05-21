from django.urls import path
from signals_app.views import *

urlpatterns = [
    path('sync/', sync_test),
    path('thread/', thread_test),
    path('transaction/', transaction_test),
]
