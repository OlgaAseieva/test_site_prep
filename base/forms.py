from django import forms
from .models import UserReservation

class UserReservationForm(forms.ModelForm):

   name = forms.CharField(
       max_length=50,
       widget=forms.TextInput(attrs={
           'type' : 'text',
           'name' : 'name',
           'class' : 'form-control',
           'id': 'name',
           'placeholder' : 'Your Name',
           'data - rule' : 'minlen:4',
           'data-msg': "Please enter at least 4 chars"
       })
   )
   phone = forms.CharField(max_length=15,
                         widget=forms.TextInput(attrs={'type' :"text", 'class': "form-control",
                                                       'name' : "phone",'id' : "phone", 'placeholder' : "Your Phone",
                                                       'data-rule': "minlen:4", 'data-msg' : "Please enter at least 4 chars",
                                                       'required': 'required'
       }))
   plan_date = forms.DateTimeField(
                             widget=forms.DateInput(attrs={'type': "text", 'name': "date", 'class' : "form-control",
                                                           'id':"date", 'placeholder' : "Date", 'data-rule' : "minlen:4",
                                                           'data - msg':"Please enter at least 4 chars"
                        }))
   person = forms.ImageField(widget=forms.NumberInput(attrs={'type':"number", 'class': "form-control",
                                                             'name' : "people", 'id' : "people", 'placeholder' : "# of people",
                                                             'data-rule' : "minlen:1", 'data-msg': "Please enter at least 1 chars"
   }))

   message = forms.CharField(max_length=400,
                         widget=forms.TextInput(attrs={"type" : 'message', 'name' : 'message', 'class' : 'form-control',
                                                      'rows':"6", 'placeholder' : 'Message', 'required': 'required'  }))


   class Meta:

        model = UserReservation
        fields = ('name', 'phone', 'person', 'plan_date', 'message')
