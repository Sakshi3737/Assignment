from django.http import HttpResponse
from .models import TestModel
import threading
from django.db import transaction


# Question 1: Synchronous or Asynchronous
def sync_test(request):

    print("Before save")

    TestModel.objects.create(name="John")

    print("After save")

    return HttpResponse(
        "Check console output"
    )


# Question 2: Same thread or not
def thread_test(request):

    print(
        "Main Thread ID:",
        threading.current_thread().ident
    )

    TestModel.objects.create(name="Sam")

    return HttpResponse(
        "Check console output"
    )


# Question 3: Same transaction
def transaction_test(request):

    try:
        with transaction.atomic():

            TestModel.objects.create(
                name="Transaction Test"
            )

            raise Exception(
                "Rollback transaction"
            )

    except Exception:
        pass

    count = TestModel.objects.filter(
        name="Transaction Test"
    ).count()

    return HttpResponse(
        f"Records saved: {count}"
    )
