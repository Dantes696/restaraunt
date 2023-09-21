from django import forms
from .models import Reservation, Testimonial


class ReservationForm(forms.ModelForm):
    name = forms.CharField(label='Your Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Your Name'
        }
    ))

    email = forms.EmailField(label="Your Email", widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Your Email'
        }
    ))
    reservation_date = forms.DateTimeField(label="Date & Time",
                                           widget=forms.DateTimeInput(
                                               attrs={
                                                   'class': 'form-control datetimepicker-input',
                                                   'id': 'datetime',
                                                   'placeholder': 'Date & Time',
                                                   'data-target': '#date3',
                                                   'data-toggle': 'datetimepicker'
                                               }
                                           ))

    people = forms.IntegerField(label="No Of People", widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'people',
            'placeholder': 'No Of People'
        }
    ))

    request = forms.CharField(label="Special Request", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'message',
            'placeholder': 'Special Request',
            'style': 'height: 100px;'
        }
    ))

    class Meta:
        model = Reservation
        fields = (
            'name',
            'email',
            'reservation_date',
            'people',
            'request'
        )


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Your Name'
        }
    ))

    email = forms.EmailField(label="Your Email", widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Your Email'
        }
    ))

    subject = forms.CharField(label='Subject', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'subject',
            'placeholder': 'Subject'
        }
    ))
    message = forms.CharField(label="Message", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'message',
            'placeholder': 'Leave a message here',
            'style': 'height: 150px;'
        }
    ))


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(label='Your Name', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Your Name'
        }
    ))

    profession = forms.CharField(label="Your Profession", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Your Profession'
        }
    ))


    feedback = forms.CharField(label="Feedback", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'message',
            'placeholder': 'Feedback...',
            'style': 'height: 150px;'
        }
    ))

    photo = forms.FileField(label='Photo', widget=forms.FileInput(
        attrs={
            'type': 'file',
            'class': 'form-control',
            'id': 'subject',
            'placeholder': 'Photo'
        }
    ))

    class Meta:
        model = Testimonial
        fields = (
            'name',
            'profession',
            'feedback',
            'photo'
        )