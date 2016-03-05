from qa.views import test

urlpatterns = patterns( 'qa.views',
	url(r'^$','error',name='test'),
	url(r'^login/','error',name='login'),
	url(r'^sigup/','error',name='sigup'),
	url(),
	url(r'^ask/','error',name='ask'),
	url(r'^popular','error',name='popular'),
	url(r'^new','error',name='new'),	
	)
