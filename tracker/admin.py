from django.contrib import admin

# Register your models here.
from tracker.models import *


#  Changes the Django Amdin Panel 
admin.site.site_header ="Expense Tracker"
admin.site.site_title ="Expense Tracker"
admin.site.site_url="Expense Tracker"

admin.site.register(CurrentBalance)


@admin.action(description=["Mark selected Stories as CREDIT"])
def make_credit(modeladmin, request, queryset):
    queryset.update(expense_type="CREDIT")
# this class use to create data into tabular format in admin panel

class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display =[
        'amount',
        'current_balance',
        'expense_type',
        'description',
        'created_at',
        
        # Dynamic Field
        'Display_age',
    ]
    
    # Dynamic Field
    def Display_age(self,obj):
        if obj.amount > 0:
            return "Positive"
        return "Negative"
        
    actions =['make_credit']

    search_fields = ['expense_type' , 'description']
    ordering = ['created_at']
    list_filter = ["expense_type"]
    
    
admin.site.register(TrackingHistory , TrackingHistoryAdmin)

