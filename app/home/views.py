from datetime import date, datetime

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, HttpResponse, render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from app.contrib.mixins import AppContextMixin
from app.user.models import UserProfile
from .forms import TaskForm
from .models import Task


@csrf_protect
def search(request):
    if request.is_ajax():
        words = request.POST.get("search_text").encode('utf-8')
        # print(words)
        objects = Task.objects.filter(name__icontains=words)
        objects |= Task.objects.filter(description__icontains=words)
        return render(request, 'add_event/objects.html', {'all_events': objects})
    else:
        return HttpResponse("Forbidden")


class AddEvent(AppContextMixin, CreateView):
    model = Task
    success_url = 'home:add_event'
    template_name = 'add_event/content.html'
    form_class = TaskForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = UserProfile.objects.get(id=self.request.user.id)
        self.object.save()
        return redirect(self.success_url)

    def get_context_data(self, *args, **kwargs):
        kwargs = super(AddEvent, self).get_context_data(*args, **kwargs)
        kwargs['all_events'] = Task.objects.all()
        return kwargs


def get_events_today(today, objects):
    objects = objects.filter(notice=False)
    answer = objects.filter(repeat='never').filter(date=today)
    answer |= objects.filter(repeat='1day')

    for i in objects.filter(repeat='2day'):
        if (today - i.date).days % 2 == 0:
            answer |= objects.filter(pk=i.pk)
    for i in objects.filter(repeat='1wk'):
        if (today - i.date).days % 7 == 0:
            answer |= objects.filter(pk=i.pk)
    for i in objects.filter(repeat='2wks'):
        if (today - i.date).days % 14 == 0:
            answer |= objects.filter(pk=i.pk)
    answer |= objects.filter(repeat='mn').filter(date__day=today.day)
    answer |= objects.filter(repeat='yr').filter(date__month=today.month).filter(date__day=today.day)

    return answer


class GetTask(AppContextMixin, TemplateView):
    template_name = 'home/event_table.html'

    def diff_times(self, start, end):
        minutes = end.hour * 60 + end.minute - start.hour * 60 - start.minute
        return minutes

    def get_context_data(self, *args, **kwargs):
        required_date = self.request.GET.get('date')
        if required_date:
            required_date = datetime.strptime(required_date, '%d.%m.%Y')
        else:
            required_date = date.today()
        table = get_events_today(required_date, Task.objects.filter(user__user_id=self.request.user.id)).order_by(
            'time_notice').values()
        for i in range(len(table)):
            # print(table[i])
            start = table[i]['start']
            end = table[i]['end']
            table[i]['length'] = self.diff_times(start, end)
            # For range chart
            table[i]['start_minutes'] = start.hour * 60 + start.minute
            table[i]['time_now'] = datetime.today().time()

        kwargs['tasks'] = table
        kwargs['notices'] = Task.objects.filter(notice=True)
        kwargs['number_chart'] = self.request.session.get('chart', '0')
        kwargs['required_date'] = date.strftime(required_date, '%d.%m.%Y')
        kwargs['tab'] = self.request.GET.get('tab')
        return super(GetTask, self).get_context_data(*args, **kwargs)


class ChangeEvent(AppContextMixin, UpdateView):
    form_class = TaskForm
    model = Task
    template_name = 'add_event/content.html'

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        else:
            return 'home:add_event'

    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())

    def get_object(self, queryset=None):
        try:
            instance = Task.objects.get(pk=self.kwargs['pk'])
        except ObjectDoesNotExist:
            return None
        return instance

    def get_context_data(self, *args, **kwargs):
        kwargs = super(ChangeEvent, self).get_context_data(*args, **kwargs)
        kwargs['all_events'] = Task.objects.all()
        return kwargs


class DeleteEvent(AppContextMixin, DeleteView):
    model = Task

    def get_success_url(self):
        url = self.request.META.get('HTTP_REFERER')
        return url


def redirect_to_home(request):
    return redirect('home:current')
