from django.contrib import admin

from .models import Question,Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date","question_text"]
    inlines = [ChoiceInline]

    # This is powefull
    list_display = ("question_text","pub_date","was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:  # Check if the user is an admin user
            # Custom logic for saving when added/modified from admin
            # For example, you can add a flag to the object or do other actions
            obj.is_added_from_admin = True
        super().save_model(request, obj, form, change)

    



# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
