from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, HttpResponse, render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, UpdateView, DeleteView

from app.contrib.mixins import AppContextMixin
from app.user.models import UserProfile
from .forms import WordForm
from .models import Word


@csrf_protect
def search(request):
    if request.is_ajax():
        words = request.POST.get("search_text").encode('utf-8')
        # print(words)
        objects = Word.objects.filter(name__icontains=words)
        objects |= Word.objects.filter(translation__icontains=words)
        objects |= Word.objects.filter(modified__icontains=words)

        return render(request, 'add_word/list_words.html', {'part_of_words': objects[:20]})
    else:
        return HttpResponse("Forbidden")


class AddWord(AppContextMixin, CreateView):
    model = Word
    success_url = 'english_words:dictionary'
    template_name = 'add_word/content.html'
    form_class = WordForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = UserProfile.objects.get(id=self.request.user.id)
        self.object.save()
        return redirect(self.success_url)

    def get_context_data(self, *args, **kwargs):
        kwargs = super(AddWord, self).get_context_data(*args, **kwargs)
        kwargs['part_of_words'] = Word.objects.all().order_by('-modified')[:20]
        return kwargs


class ChangeWord(AppContextMixin, UpdateView):
    form_class = WordForm
    model = Word
    template_name = 'add_word/content.html'

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        else:
            return 'english_words:dictionary'

    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())

    def get_object(self, queryset=None):
        try:
            instance = Word.objects.get(pk=self.kwargs['pk'])
        except ObjectDoesNotExist:
            return None
        return instance

    def get_context_data(self, *args, **kwargs):
        kwargs = super(ChangeWord, self).get_context_data(*args, **kwargs)
        kwargs['part_of_words'] = Word.objects.all().order_by('-modified')[:20]
        return kwargs


class DeleteWord(AppContextMixin, DeleteView):
    model = Word

    def get_success_url(self):
        url = self.request.META.get('HTTP_REFERER')
        return url
