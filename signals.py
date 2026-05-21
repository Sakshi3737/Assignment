from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel
import threading
import time

@receiver(post_save, sender=TestModel)
def signal_receiver(sender, instance, **kwargs):

    print("Signal started")

    print("Signal Thread ID:",
          threading.current_thread().ident)

    time.sleep(5)

    print("Signal finished")
