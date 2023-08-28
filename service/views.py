from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, UpdateView, CreateView, DeleteView, DetailView

from service.forms import ClientForm, MessageForm
from service.models import *


class HomeView(TemplateView):
    template_name = 'service/index.html'


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self, *args, **kwargs):
        queryset = Client.objects.filter(user=self.request.user)
        return queryset


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    permission_required = 'service.change_message'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_manager"] = self.request.user.groups.filter(name='manager').exists()
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = Message.objects.filter(user=self.request.user)
        if self.request.user.groups.filter(name='manager').exists():
            queryset = Message.objects.all()
        return queryset

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("service:clients")


    def form_valid(self, form):
        client = form.save(commit=False)
        client.user = self.request.user
        client.save()
        return super().form_valid(form)


class ClientUpdateViev(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("service:clients")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("service:clients")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'message/message_detail.html'

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     if settings.CACHE_ENABLED:
    #         key = f'log_list_{self.object.pk}'
    #         log_list = cache.get(key)
    #         if log_list is None:
    #             log_list = self.object.log_set.all()
    #             cache.set(key, log_list)
    #     else:
    #         log_list = self.object.log_set.all()
    #     context_data['logs'] = log_list
    #
    #     return context_data


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} {email} {message}')
#     context = {
#         'title': "Контакты"
#     }
#     return render(request, 'mailing/contact.html', context)


# def main(request):
#     clients = len(Client.objects.all().distinct('email'))
#     article = Article.objects.filter(is_published=True).order_by('?')
#     mailing = len(Mailing.objects.all())
#     mailing_active = len(Mailing.objects.filter(status=2))
#     context = {
#         'title': "Главная",
#         'article': article[:3],
#         'mailing': mailing,
#         'mailing_active': mailing_active,
#         'clients': clients
#     }
#     return render(request, 'mailing/main.html', context)


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    permission_required = 'message.add_message'
    success_url = reverse_lazy('service:list')

    # def form_valid(self, form):
    #     tz = pytz.timezone('Europe/Moscow')
    #     clients = [client.email for client in Client.objects.filter(user=self.request.user)]
    #     new_mailing = form.save()
    #
    #     if new_mailing.mailing_time <= datetime.now(tz):
    #         mail_subject = new_mailing.massage.body if new_mailing.massage is not None else 'Рассылка'
    #         message = new_mailing.massage.theme if new_mailing.massage is not None else 'Вам назначена рассылка'
    #         try:
    #             send_mail(mail_subject, message, settings.EMAIL_HOST_USER, clients)
    #             log = Log.objects.create(date_attempt=datetime.now(tz), status='Успешно', answer='200', mailing=new_mailing)
    #             log.save()
    #         except smtplib.SMTPDataError as err:
    #             log = Log.objects.create(date_attempt=datetime.now(tz), status='Ошибка', answer=err, mailing=new_mailing)
    #             log.save()
    #             #raise err
    #         except smtplib.SMTPException as err:
    #             log = Log.objects.create(date_attempt=datetime.now(tz), status='Ошибка', answer=err, mailing=new_mailing)
    #             log.save()
    #             #raise err
    #         except Exception as err:
    #             log = Log.objects.create(date_attempt=datetime.now(tz), status='Ошибка', answer=err, mailing=new_mailing)
    #             log.save()
    #             #raise err
    #         new_mailing.status = 3
    #         if new_mailing.user is None:
    #             new_mailing.user = self.request.user
    #         new_mailing.save()
    #
    #     return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    permission_required = 'message.change_message'
    success_url = reverse_lazy('service:list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    permission_required = 'message.delete_message'
    success_url = reverse_lazy('service:list')


@permission_required('service.change_message')
def ActivateMessage(request, pk):
    mailsettings = Message.objects.get(pk=pk)
    mailsettings.is_active = False if mailsettings.is_active else True
    mailsettings.save()
    return redirect('service:list')
