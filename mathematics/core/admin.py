from django.contrib import admin
from core import models

class ReportAdmin(admin.ModelAdmin):
    list_display=('date','name','email')
    search_fields=['message','name','email']

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('updated_on','message')
    #list_filter=['']
    search_fields=['message']
class PiSearchAdmin(admin.ModelAdmin):
    list_display=('date','number')

admin.site.register(models.Credit)
admin.site.register(models.Report,ReportAdmin)
admin.site.register(models.Feedback,FeedbackAdmin)
admin.site.register(models.PiSearch,PiSearchAdmin)