from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from histproject.battles.models import Battle

UserC = get_user_model()

class Comment(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserC, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.battle.name}'

class Rating(models.Model):
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(UserC, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5, 'Стойноста трябва да бъде от 1 до 5'),
            MinValueValidator(1, 'Стойноста трябва да бъде от 1 до 5'),
        ],
    )  # Примерен рейтинг от 1 до 5

    class Meta:
        unique_together = (('battle', 'user'),)

    def __str__(self):
        return f'Rating {self.score} by {self.user_id.username} for {self.battle.name}'