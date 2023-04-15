from django.urls import path,include, re_path
from rest_framework.routers import DefaultRouter
from .views import (register,verify_email,
                    loginuser,
                    logout_user,
                    register_by_google,
                    reset_password,
                    reset_password_confirm,
                    CategoryViewSet,
                    SectionViewSet,
                    SubSectionViewSet,
                    ArticleViewSet,
                    VideoViewSet,
                    SubtitlesViewSet,
                    ReviewViewSet,
                    ReviewApi,UserViewSet)

router = DefaultRouter()
router.register('User',UserViewSet,basename='User')
router.register('Sections', SectionViewSet,basename='sections')
router.register('SubSections', SubSectionViewSet,basename='subsections')
router.register('Articles', ArticleViewSet,basename='articles')
router.register('Category', CategoryViewSet,basename='category')
router.register('Videos', VideoViewSet,basename='videos')
router.register('Subtitles', SubtitlesViewSet,basename='Subtitles')
router.register('Reviews', ReviewViewSet,basename='reviews')

urlpatterns = [
    path('Viewsets/', include(router.urls)),
    path('register/',register,name='register'),
    path('login/', loginuser,name='login'),
    path('create-review/', ReviewApi.as_view(), name='create-review'),
    path('logout/', logout_user, name='logout'),
    path('verifyemail/', verify_email, name='verifyemail'),
    path('reset_password/',reset_password,name='reset_password'),
    path('reset_password_confirm/',reset_password_confirm,name='reset_password_confirm'),
    # http://127.0.0.1/api/register-by-access-token \google-oauth2
    re_path('google_register/' + r'social/(?P<backend>[^/]+)/$',register_by_google),

]