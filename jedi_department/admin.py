from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from jedi_department.models import (Candidate, Planet, Jedi,
                                    Test, ListQuestions, Answer, Padawan)


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('email', 'name', 'planet', 'age')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('email', 'name', 'planet', 'age', 'is_active', 'is_admin')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'planet', 'is_admin', )
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', )}),
        ('Personal info', {'fields': ('name', 'planet', 'age', 'pass_test')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'planet', 'age', 'pass_test')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class ListQuestionsAdmin(admin.ModelAdmin):
    list_display = ('test', 'number', 'question')
    list_display_links = ('question',)


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'planet')


class JedaiAdmin(admin.ModelAdmin):
    list_display = ('name', 'planet')


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('test', 'candidate', 'text_answer', 'date_answer')


class PadawanAdmin(admin.ModelAdmin):
    list_display = ('jedi_id', 'candidate_id', 'active')

admin.site.register(Candidate, UserAdmin)
admin.site.unregister(Group)
# admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Planet)
admin.site.register(Jedi, JedaiAdmin)
admin.site.register(ListQuestions, ListQuestionsAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Padawan, PadawanAdmin)
