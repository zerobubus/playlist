from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Playlist
from .forms import PlaylistForm
from django.shortcuts import render
import music.forms
import account.forms
import account.views


@login_required
def index(request):

    playlist = Playlist.objects.filter(user=request.user)

    return render(
        request,
        "index.html",
        {"playlist": playlist}
    )


@login_required
def playlist_view(request, playlist_id):

    playlist = get_object_or_404(Playlist, id=playlist_id)

    return render(
        request,
        "playlist_view.html",
        {"playlist": playlist}
    )


@login_required
def confirm_delete(request, playlist_id):

    playlist = get_object_or_404(Playlist, id=playlist_id)

    return render(
        request,
        "playlist_confirm.html",
        {"playlist": playlist}
    )


@login_required
def playlist_delete(request, playlist_id):

    playlist = get_object_or_404(Playlist, id=playlist_id)
    playlist.delete()
    return redirect("index")


@login_required
def new_post(request):

    form = PlaylistForm(request.POST or None, files=request.FILES or None)
    if not form.is_valid():
        return render(request, "new_post.html", {"form": form})
    post = form.save(commit=False)
    post.user = request.user
    post.save()
    form.save_m2m()
    return redirect("index")


@login_required()
def post_edit(request, playlist_id):

    post = Playlist.objects.get(
        id=playlist_id, user__username=request.user.username)
    if request.user != post.user:
        return redirect(f"/playlist/{playlist_id}")
    form = PlaylistForm(request.POST or None, instance=post)
    if not form.is_valid():
        return render(
            request,
            "post_new.html",
            {"post": post,
             "form": form}
        )
    post = form.save(commit=False)
    post.user = request.user
    post.save()
    form.save_m2m()
    return redirect("index")


class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm


class SignupView(account.views.SignupView):

    form_class = music.forms.SignupForm

    def after_signup(self, form):

        super(SignupView, self).after_signup(form)
