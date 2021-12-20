from django.db import models

# Create your models here.
class Transaction(models.Model):
    book_qrId = models.CharField(max_length=100)
    book_location=models.FloatField()
    customer_location=models.FloatField()
    prev_node=models.FloatField()
    next_node=models.FloatField()
    server_command=models.CharField(max_length=20)
    compass_value=models.FloatField()
    book_found=models.BooleanField()
    book_fetching=models.BooleanField()
    play_time=models.FloatField()