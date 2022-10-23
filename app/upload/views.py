from chunked_upload.views import ChunkedUploadCompleteView, ChunkedUploadView
from csv_processor import csv_processer
from django.views.generic.base import TemplateView

from .models import MyChunkedUpload


class ChunkedUploadDemo(TemplateView):
    template_name = "chunked_upload_demo.html"


class MyChunkedUploadView(ChunkedUploadView):

    model = MyChunkedUpload
    field_name = "the_file"

    def check_permissions(self, request):
        # Allow non authenticated users to make uploads
        pass


class MyChunkedUploadCompleteView(ChunkedUploadCompleteView):

    model = MyChunkedUpload

    def check_permissions(self, request):
        # Allow non authenticated users to make uploads
        pass

    def on_completion(self, uploaded_file, request):
        if uploaded_file.name.endswith(".csv"):
            csv_processer(uploaded_file)

    def get_response_data(self, chunked_upload, request):
        return {
            "message": (
                f"You successfully uploaded '{chunked_upload.filename}'"
                f" ({chunked_upload.offset} bytes)! and saved"
                f" in the DB with the ID {chunked_upload.upload_id}"
            )
        }
