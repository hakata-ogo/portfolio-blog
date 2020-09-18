from django.db import models

# Create your models here.
class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Post(models.Model):
    """Model definition for Post."""

    # TODO: Define fields here
    title = models.CharField(max_length=120)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='posts')


    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comment(models.Model):
    """Model definition for Comment."""

    # TODO: Define fields here
    
    author = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'



