import pdb
import requests
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, UpdateView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Lending
from .forms import LendingForm, LendingAdminForm


class LendingCreateView(CreateView):
    model = Lending
    form_class = LendingForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # Consulta a la api
        api = "https://api.moni.com.ar/api/v4/scoring/pre-score/"
        headers = {"credential": "ZGpzOTAzaWZuc2Zpb25kZnNubm5u"}
        dni = form.cleaned_data.get('dni')
        url = api + str(dni)
        data = requests.get(url, headers=headers).json()
        # Si el prestamo es aprovado el estado del atributo pasa a True
        if data['status'] == 'approve':
            form.instance.status = True
            messages.success(self.request, 'Su prestamo ha sido aprobado :D')
        elif data['status'] == 'rejected':
            form.instance.status = False
            messages.warning(
                self.request, 'Su prestamo no ha sido aprobado :( ')
        else:
            form.instance.status = False
        # Si ocurre un error el estado del atributo pasa a verdadero
        if data['has_error'] == True:
            form.instance.error = True
            messages.error(self.request, 'Ocurrió un error')
        else:
            form.instance.error = False
        form.save()
        return self.render_to_response(self.get_context_data(request=self.request, form=form))


@method_decorator(login_required, name='dispatch')
class AdministrationView(TemplateView):
    template_name = 'admin/administration.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['lendings'] = Lending.objects.filter(is_active=True)
        return context


@method_decorator(login_required, name='dispatch')
class LendingUpdateView(UpdateView):
    model = Lending
    form_class = LendingAdminForm
    template_name = 'admin/lending_update_form.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('administration')


class LendingDeleteView(View):
    def get(self, request, slug, *args, **kwargs):
        try:
            lending = Lending.objects.get(slug=slug)
        except:
            lending = None
        context = {
            "lending": lending,
        }
        return render(request, 'admin/lending_confirm_delete.html', context)

    def post(self, request, slug, *args, **kwargs):
        try:
            lending = Lending.objects.get(slug=slug)
            lending.is_active = not lending.is_active
            lending.save()
        except:
            None
        return HttpResponseRedirect('/administration/')
