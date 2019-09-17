from rest_framework import routers
from wordflash.wordflashapp.views import WordPairViewSet

router = routers.DefaultRouter()
router.register(r'wordpair', WordPairViewSet, base_name='wordpair')
urlpatterns = router.urls