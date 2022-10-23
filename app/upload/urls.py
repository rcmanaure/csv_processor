from django.urls import path
from upload.views import (
    ChunkedUploadDemo,
    MyChunkedUploadView,
    MyChunkedUploadCompleteView,
    download_file,
)

urlpatterns = [
    path("", ChunkedUploadDemo.as_view(), name="chunked_upload"),
    path(
        "api/chunked_upload_complete/",
        MyChunkedUploadCompleteView.as_view(),
        name="api_chunked_upload_complete",
    ),
    path(
        "api/chunked_upload/", MyChunkedUploadView.as_view(), name="api_chunked_upload"
    ),
    path("download/", download_file, name="download"),
]
