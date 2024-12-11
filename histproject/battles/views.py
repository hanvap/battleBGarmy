from django.contrib import messages
from django.core.paginator import Paginator

from django.db.models import Avg, Q
from django.shortcuts import  redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from histproject.battles.forms import BattleBaseForm, BattleEditForm, CountryForm
from histproject.battles.models import Battle, Country
from histproject.posts.forms import CommentForm, RatingForm
from histproject.posts.models import Rating


class ListBattleView(ListView):
    model = Battle
    template_name = 'battles/battle_list.html'
    context_object_name = 'battles'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Battle'] = Battle.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        if query:
            return Battle.objects.filter(
                Q(location__icontains=query) | Q(countries_involved__name__icontains=query)
            ).distinct()
        return Battle.objects.all()

class DetailBattleView(DetailView):
    model = Battle
    template_name = 'battles/battle_detail.html'
    context_object_name = 'battle'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['rating_form'] = RatingForm()


        comments = self.object.comments.all()
        paginator = Paginator(comments, 2)  # Показваме по 2 коментара на страница
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        context['comments'] = page_obj

        avg = Rating.objects.filter(battle=self.object).aggregate(Avg('score'))
        context['avg_score'] = avg['score__avg'] or 0
        context['page_obj'] = page_obj
        print(context)
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if 'content' in request.POST:
            return self.handle_comment(request)
        elif 'score' in request.POST:
            return self.handle_rating(request)
        return redirect('battle_detail', pk=self.object.pk)

    def handle_comment(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.battle = self.object
            comment.user = request.user
            comment.save()
            print(comment)
            messages.success(request, 'Коментарът е добавен успешно!')
        else:
            messages.error(request, 'Грешка при добавяне на коментар.')
        return redirect('battle_detail', pk=self.object.pk)

    def handle_rating(self, request):
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            existing_rating = Rating.objects.filter(battle=self.object, user=request.user).first()

            if existing_rating:
                messages.error(request, 'Вече сте оценили тази битка.')
                return redirect('battle_detail', pk=self.object.pk)
            rating = rating_form.save(commit=False)
            rating.battle = self.object
            rating.user = request.user
            rating.save()
            messages.success(request, 'Рейтингът е добавен успешно!')
        else:
            messages.error(request, 'Грешка при добавяне на рейтинг.')
        return redirect('battle_detail', pk=self.object.pk)






class CreateBattleView(CreateView):
    model = Battle
    template_name = 'battles/battle_create.html'
    form_class = BattleBaseForm
    success_url = reverse_lazy('battle_list')


class UpdateBattleView(UpdateView):
    model = Battle
    form_class = BattleEditForm
    template_name = 'battles/battle_edit.html'
    success_url = reverse_lazy('battle_list')


class DeleteBattleView(DeleteView):
    model = Battle
    template_name = 'battles/battle_delete.html'
    success_url = reverse_lazy('battle_list')


class CreateCountryView(CreateView):
    model = Country
    form_class = CountryForm
    template_name = 'battles/country_create.html'
    success_url = reverse_lazy('battle_create')
