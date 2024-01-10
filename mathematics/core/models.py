from django.db import models

class Report(models.Model):
      name=models.CharField(max_length=100)
      email=models.EmailField()
      date=models.DateTimeField(auto_now_add=True)
      links=models.URLField(max_length=500)
      message=models.TextField()
      reportfile=models.FileField(upload_to='userdata/report')

      class Meta:
            ordering=['-date']
      def __str__(self):
            return self.name
      
class Credit(models.Model):
      title=models.CharField(max_length=200)
      description=models.CharField(max_length=400)
      links=models.CharField(max_length=200)
      updated_on=models.DateTimeField(auto_now_add=True)

      class Meta:
            ordering=['-updated_on']
      def __str__(self):
            return self.title
      
class Feedback(models.Model):
      name=models.CharField(max_length=100)
      email=models.EmailField()
      updated_on=models.DateTimeField(auto_now_add=True)
      feedback_1=models.CharField(max_length=100)
      feedback_2=models.CharField(max_length=100)
      first_impression=models.CharField(max_length=500)
      improve_experience=models.CharField(max_length=500)
      message=models.TextField()
      links=models.URLField(max_length=200)

      class Meta:
            ordering=['-updated_on']
      def __str__(self):
            return self.name

class PiSearch(models.Model):
      number=models.BigIntegerField()
      date=models.DateTimeField(auto_now_add=True)
      
      def __int__(self):
        return self.number
      class Meta:
            ordering=['-date']