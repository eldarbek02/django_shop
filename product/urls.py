from django.urls import path,include
from .views import CategoryView,ProductView
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register('categories', CategoryView)
router.register('product',ProductView)

urlpatterns = [
                path('', include(router.urls))
                ]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns = [
#                 path('categories/',CategoryView.as_view({'get':'list','post':'create'})),
#                 path('categories/<slug:pk>/',CategoryView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}))

# ]