from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# from django.templatetags.static import static


class ArgUserProfile(models.Model):
    # Profile for website users
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    friends = models.ManyToManyField(
        'self',
        through='Friendship',
        symmetrical=False,
        related_name='friends_with'
    )

    def __str__(self):
        return self.user.username

    @property
    def name(self):
        if self.display_name:
            name = self.display_name
        else:
            name = self.user.username
        return name


class Friendship(models.Model):
    # Model to represent friendships between users
    from_user = models.ForeignKey(
        User,
        related_name='request_sent',
        on_delete=models.CASCADE
        )
    to_user = models.ForeignKey(
        User,
        related_name='request_received',
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=10,
        choices=[
            ('PENDING', 'Pending Approval'),
            ('ACCEPTED', 'Accepted'),
            ('REJECTED', 'Rejected'),
            ('BLOCKED', 'Blocked'),
        ],
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensure unique friendships
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"{self.from_user.username} -> {self.to_user.username} ({self.status})"
