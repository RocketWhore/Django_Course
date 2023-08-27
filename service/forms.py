from django import forms

from service.models import Client, Message

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'surname', 'email', 'comment')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя клиента',
                }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия клиента',
                }),

            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество клиента',
                }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта клиента',
                }),

            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш комментарий',
                'rows': 2,
                }),
        }


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('theme', 'body', 'mailing_time', 'periodicity', 'status', 'clients')

        widgets = {
            'theme': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема сообщения',
                }),

            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст сообщения',
                'rows': 2,
                }),
            'mailing_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
            }),
        }

