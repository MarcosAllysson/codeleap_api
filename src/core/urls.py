from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("careers/", include("posts.urls")),
    # DOCUMENTATION
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

admin.site.site_header = "Codeleap"
admin.site.site_title = "Admin View"
admin.site.index_title = "Codeleap View"
