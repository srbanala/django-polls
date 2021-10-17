from django.urls import path

from . import views
app_name='polls'
urlpatterns = [
        path('polls/',views.Indexview.as_view(),name='index'),
	path('polls/<int:question_id>/',views.detail,name='detail'),
 	path('polls/<int:question_id>/results/',views.results,name='results'),
	path('polls/<int:question_id>/vote/',views.vote,name='vote'),
		
	]