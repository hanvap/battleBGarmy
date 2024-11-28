from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView


from histproject.posts.forms import EditCommentForm
from histproject.posts.models import Comment


class CommentEditView(UpdateView):
    model = Comment
    form_class = EditCommentForm
    template_name = 'posts/comment_edit.html'

    def get_success_url(self):
        return reverse('battle_detail', args=[self.object.battle.id])




class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'posts/comment_delete.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('battle_detail', args=[self.object.battle.id])

