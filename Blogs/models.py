from uuid import uuid4
from django.utils import timezone
from django.db.models import Model
from django.db.models import CharField, TextField, BooleanField, UUIDField, DateTimeField


class BlogsModel(Model):
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
    title = CharField("Title", max_length=100, unique=True, blank=False, null=True)
    content = TextField("Content", max_length=200, blank=True, null=True)
    discoverable = BooleanField(help_text="Visible to public", default=True)
    publication_date = DateTimeField("Date published", default=timezone.now)
    _id = UUIDField("Blog ID(Sub-URL)", help_text="This entry is automatically generated", default=uuid4)
    def __str__(self):
        return self.title
