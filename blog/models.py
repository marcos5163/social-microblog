from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.postgres.fields import ArrayField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True, unique=True
    )
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


class Account(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Profile(BaseModel):
    account_profile = models.OneToOneField(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    display_picture = models.URLField(max_length=500)
    bio = models.CharField(max_length=200)
    location = models.CharField(max_length=100)


class ProfileFollowOthers(BaseModel):
    profile_which_follow_other = models.OneToOneField(
        Profile, related_name="profile_which_follow_other", on_delete=models.CASCADE
    )
    followed_profile = models.ForeignKey(
        Profile, related_name="followed_profile", on_delete=models.SET_NULL, null=True
    )


class OthersFollowProfile(BaseModel):
    profile_which_gets_followed = models.OneToOneField(
        Profile, related_name="profile_which_gets_followed", on_delete=models.CASCADE
    )
    following_profile = models.ForeignKey(
        Profile, related_name="following_profile", on_delete=models.SET_NULL, null=True
    )


class Like(BaseModel):
    liked_profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)


class Blog(BaseModel):
    blog_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog_text = models.CharField(max_length=100, default="")
    blog_image = ArrayField(models.URLField(max_length=500), size=5)
    blog_like = models.ForeignKey(Like, on_delete=models.SET_NULL, null=True)
    comment = models.ForeignKey("self", on_delete=models.CASCADE)
