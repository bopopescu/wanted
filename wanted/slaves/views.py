from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from . import models


def ShowSl(req):
    return render(req, "main_sl.html")


class ListSlavesView(ListView):
    page_title = "Slaves"
    model = models.Slave

    # def get_queryset(self):
    #    return super().get_queryset().filter(account__user=self.request.user)

    def get_queryset(self):
        return super().get_queryset()  # .filter(account__user=self.request.user) .aggregate(sum=Sum('amount'))['sum']


class DetailSlaveView(DetailView):
    model = models.Slave

    def get_fname(self):
        return super().get_object().fname

    page_title = "דגדגדגד"


class CreateSlave(CreateView):
    model = models.Slave
    page_title = "create slave"
    fields = ['fname', 'lname', 'descr', 'cv']
    success_url = reverse_lazy('slaves:list')

#    form_class = forms.FormAddSlaveView
#    class Meta:
#        model = models.Slave
#       fields = '__all__'

# fields = '__all__'
# fields = ['fname']
# fields =[]
# exclude = []
