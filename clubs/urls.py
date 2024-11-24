from django.http import HttpResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClubViewSet, MemberViewSet, AttendanceRecordViewSet

# DRF Router
router = DefaultRouter()
router.register(r'clubs', ClubViewSet)
router.register(r'members', MemberViewSet)
router.register(r'attendance', AttendanceRecordViewSet)

# 루트 URL 처리 View
def home(request):
    return HttpResponse("<h1>Welcome to the DCU Clubs API</h1><p>Visit <a href='/swagger/'>Swagger UI</a> for API documentation.</p>")

# URL Patterns
urlpatterns = [
    path('', home, name='home'),  # 루트 URL 처리
    path('api/', include(router.urls)),  # API 엔드포인트
]

