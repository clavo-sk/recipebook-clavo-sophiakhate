from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage
from .forms import RecipeForm, ImageForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipe_form.html" 
    form_class = RecipeForm


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "image_form.html"
    form_class = ImageForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk': self.get_object().pk})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = ImageForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = self.get_object()
            recipe_image.save()
            return redirect(self.get_success_url())
        else:
            self.object_list = self.get_queryset(**kwargs)
            ctx = self.get_context_data(** kwargs)
            ctx['form'] = form
            return self.render_to_response(ctx)