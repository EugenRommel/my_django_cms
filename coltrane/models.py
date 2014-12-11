from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
from markdown import markdown
from django.conf import settings
from taggit.managers import TaggableManager

class Category(models.Model):
    title = models.CharField(max_length=250, help_text="Maximum 250 characters")
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique")
    description = models.TextField()

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ("coltrane_category_details",
                (),
                {'slug': self.slug})


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ['title']}

class LiveEntryManager(models.Manager):
    def get_queryset(self):
        return super(LiveEntryManager, self).get_queryset().filter(status=self.model.LIVE_STATUS);

class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = ((LIVE_STATUS, 'Live'), (DRAFT_STATUS, 'Draft'), (HIDDEN_STATUS, "Hidden"))

    # Core fields
    title = models.CharField(max_length=250, help_text="Maximum 250 characters")

    excerpt = models.TextField(blank=True, help_text="A short summary for the entry. Optional")
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    # Fields to store generated HTML
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    # Metadata
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from title. Must be unique")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)

    # Categorization
    categories = models.ManyToManyField(Category)
    tags = TaggableManager()

    live = LiveEntryManager()
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Entries"
        ordering = ["-pub_date"]

    def __unicode__(self):
        return self.title

    def save(self):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save()

    @models.permalink
    def get_absolute_url(self):
        return ("coltrane_entry_details", (), {
            'year': self.pub_date.strftime("%Y"),
            'month': self.pub_date.strftime("%b").lower(),
            'day': self.pub_date.strftime("%d"),
            'slug': self.slug
        })

    def live_entry_set(self):
        from coltrane.models import Entry
        return self.entry_set.filter(status=Entry.LIVE_STATUS)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ['title']}
    #unique_for_date = ['pub_date']

class Link(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    description_html = models.TextField(editable=False, blank=True)
    url = models.URLField(unique=True)

    posted_by = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')
    tags = TaggableManager()

    enable_comments = models.BooleanField(default=True)
    post_elsewhere = models.BooleanField('Post to del.icio.us', default=True,
                                         help_text='If checked, this link will be posted both to your weblog and your delicious account')

    via_name = models.CharField('Via',
                                max_length=250,
                                blank=True,
                                help_text="The name of the person whose site you spotted the link on. Optional.")
    via_url = models.URLField('Via URL', blank=True,
                              help_text='The URL of the site where you spotted the link on. Optional.')

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def save(self):
        if self.description:
            self.description_html = markdown(self.description)
        if not self.id and self.post_elsewhere:
            import pydelicious
            from django.utils.encoding import smart_str
            pydelicious.add(settings.DELICIOUS_USER, settings.DELICIOUS_PASSWORD,
                            smart_str(self.url),
                            smart_str(self.title),
                            smart_str(self.tags))
        super(Link, self).save()

    @models.permalink
    def get_absolute_url(self):
        return ('coltrane_link_details', (), {'year': self.pub_date.strftime("%Y"),
                                              'month': self.pub_date.strftime("%b").lower(),
                                              'day': self.pub_date.strftime("%d"),
                                              'slug': self.slug
                                              })

class LinkAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ['title']}
    #unique_for_date =  ['pub_date']