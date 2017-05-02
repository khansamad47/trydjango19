from django.contrib import admin

# Register your models here.
from .models import Post

# This class is used to modify the admin display of the models
# of this application
class PostModelAdmin(admin.ModelAdmin):
    # This controls what will be displayed at the row of each entry
    list_display = ["title", "timestamp","updated"]
    
    # Which column is clickable
    list_display_links = ["updated"]

    # Adds filter to the columns
    list_filter = ["updated", "timestamp"]

    # Add searchability
    search_fields = ["title","content"]

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
