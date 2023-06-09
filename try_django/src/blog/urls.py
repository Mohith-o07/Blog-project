
from django.urls import path
from .views import(
    blog_post_detail_view,
    blog_post_update_view,
    blog_post_delete_view,
    blog_post_list_view
    )
urlpatterns = [
    path('',blog_post_list_view),
    path('<str:slug>/',blog_post_detail_view),
    path('<str:slug>/edit/',blog_post_update_view),
    path('<str:slug>/delete/',blog_post_delete_view),
    #re_path(r'blog/(?P<post_id>\d+)/$',blog_post_details_page),
    #                ?P<slug>\w+
]
