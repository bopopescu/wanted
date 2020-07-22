from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from . import models


def ShowSl(req):
    return render(req, "main_sl.html")


class ListSubordinatesView(ListView):
    page_title = "Subordinates"
    model = models.Subordinate

    # def get_queryset(self):
    #    return super().get_queryset().filter(account__user=self.request.user)

    def get_queryset(self):
        return super().get_queryset()  # .filter(account__user=self.request.user) .aggregate(sum=Sum('amount'))['sum']


class DetailSubordinateView(DetailView):
    model = models.Subordinate

    def get_fname(self):
        return super().get_object().fname

    page_title = "דגדגדגד"


class CreateSubordinate(CreateView):
    model = models.Subordinate
    page_title = "create subordinate"
    fields = ['fname', 'lname', 'descr', 'cv']
    success_url = reverse_lazy('subordinates:list')

#    form_class = forms.FormAddSubordinateView
#    class Meta:
#        model = models.Subordinate
#       fields = '__all__'

# fields = '__all__'
# fields = ['fname']
# fields =[]
# exclude = []
