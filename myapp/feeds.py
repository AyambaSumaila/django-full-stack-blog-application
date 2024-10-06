import markdown
from django.contrib.syndication.views import Feed 
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = "My Blog"
    link = reverse_lazy('myapp:post_list')
    description = "Latest posts from my blog."
    
    
    def items(self):
        return Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-publish')[:5]
        
        
    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)
    
    
    def item_pubdate(self, item):
        return item.publish
    
    
        