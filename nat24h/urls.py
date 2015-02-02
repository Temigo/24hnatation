from django.conf.urls import patterns, include, url
from rest_framework import routers

from django.contrib import admin
admin.autodiscover()

# import permission
# permission.autodiscover()

from nat24h_api.models.profile import UserViewSet, ProfileViewSet, GroupViewSet
from nat24h_api.models.activity import ActivityViewSet, TeamViewSet
from nat24h_api.models.filrouge import TimeSlotViewSet, TimeSlotSubscriptionViewSet


router = routers.DefaultRouter()

router.register('user', UserViewSet)
router.register('profile', ProfileViewSet)
router.register('group', GroupViewSet)

router.register('activity', ActivityViewSet)
router.register('team', TeamViewSet)

router.register('slot', TimeSlotViewSet)
router.register('slotsubscription', TimeSlotSubscriptionViewSet)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^', include(router.urls)),
)
