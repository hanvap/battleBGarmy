from django.urls import path, include

from histproject.posts.views import CommentEditView, CommentDeleteView

urlpatterns = [
    path('comment/', include([
        path('<int:pk>/edit/', CommentEditView.as_view(), name='comment_edit'),
        path('<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete')
    ]))
]