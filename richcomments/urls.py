from django.conf.urls import patterns, url

urlpatterns = patterns(
    'richcomments.views',
    url(
        r'^list/(?P<content_type>[\w-]+)/(?P<id>\d+)$',
        'list',
        name='render_comment_list'
    ),
)
