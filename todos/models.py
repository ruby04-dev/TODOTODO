from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Todo(models.Model):

    class Status(models.TextChoices):
        PENDING = None, _("Pending"),
        TODO = "1", _("To do"),
        WIP = "2", _("In pregress"),
        COMPLETED = "3", _("Completed"),

    content = models.CharField(_(""), max_length=255)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=4,
        choices=Status.choices,
        default=Status.TODO,
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='todos',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
