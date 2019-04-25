from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from users.models import User
from django import forms

class UserCreationForm(forms.ModelForm):

    first_password = forms.CharField(label='Password', widget=forms.PasswordInput)
    conf_password = forms.CharField(label='Confirm Your Password', widget=forms.PasswordInput)
    is_maintainer_chkbox = forms.BooleanField(
        label='Do you own/manage a restaurant?', 
        widget=forms.CheckboxInput,
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 
            'last_name', 'date_of_birth', 'first_password',
            'conf_password', 'is_maintainer_chkbox')

    def verify_password_entries(self):
        first_password = self.cleaned_data.get("first_password")
        conf_password = self.cleaned_data.get("conf_password")
        
        if first_password and conf_password and first_password != conf_password:
            raise forms.ValidationError("Woops! Your passwords don't match")
        
        return conf_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["first_password"])
        user.is_maintainer = self.cleaned_data["is_maintainer_chkbox"]
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth', 'is_maintainer')

    def clean_password(self):
        return self.initial["password"]

'''
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_of_birth', 'is_maintainer')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_maintainer',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'first_password', 'conf_password')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
#admin.site.register(User, UserAdmin)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)
'''

admin.site.register(User)

