from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

from histproject.battles.models import Country, Battle
from histproject.posts.models import Comment

User = get_user_model()

class DetailProfileViewTests(TestCase):

    def setUp(self):
        # Създайте държава
        self.country = Country.objects.create(name='Bulgaria')  # Създайте Country обект
        # Създайте битка
        self.battle = Battle.objects.create(
            name='Battle Name',
            date='2024-11-29',
            location='Сливница',
            result='win',
            description='Сливница',
            latitude=42.324500,
            longitude=23.234500,
            image_url=''
        )
        self.battle.countries_involved.add(self.country)  # Добавете страната след създаването на битката

        # Създайте тестов потребител
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Създайте тестови потребители за детайла
        self.detail_user = User.objects.create_user(username='detailsuser', password='testpassword')

        # Създайте коментари с battle_id
        Comment.objects.create(user=self.detail_user, content='First comment', battle=self.battle)
        Comment.objects.create(user=self.detail_user, content='Second comment', battle=self.battle)

    def test_detail_view_redirects_if_not_logged_in(self):
        self.client.logout()  # Изход от тестовия потребител
        response = self.client.get(reverse('profile_detail', kwargs={'pk': self.detail_user.pk}))
        self.assertRedirects(response, f'/accounts/login/?next=/accounts/profile/{self.detail_user.pk}/')

    def test_detail_view_renders_correct_template(self):
        response = self.client.get(reverse('profile_detail', kwargs={'pk': self.detail_user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile_detail.html')

    def test_detail_view_context_data(self):
        response = self.client.get(reverse('profile_detail', kwargs={'pk': self.detail_user.pk}))
        self.assertEqual(response.context['comment_count'], 2)  # Проверка на правилния брой коментари



    def test_detail_view_displays_correct_comment_count(self):
        response = self.client.get(reverse('profile_detail', kwargs={'pk': self.detail_user.pk}))
        self.assertEqual(response.context['comment_count'], 2)  # Проверка на правилния брой коментари



