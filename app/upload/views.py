import mimetypes
import os

from chunked_upload.views import ChunkedUploadCompleteView, ChunkedUploadView
from csv_processor import csv_processer
from django.http.response import HttpResponse
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
        """
        Placeholder method to define what to do when upload is complete.
        """
        file_id = uploaded_file.file
        file_id = str(file_id).split("/")
        file_id = file_id[4].split(".")
        file_id = file_id[0]

        if uploaded_file.name.endswith(".csv"):
            csv_processer(uploaded_file, file_id)

    def get_response_data(self, chunked_upload, request):
        """
        Data for the response. Should return a dictionary-like object.
        """
        return {
            "message": (
                f"You successfully uploaded '{chunked_upload.filename}'"
                f" ({chunked_upload.offset} bytes)! and saved"
                f" in the DB with the ID {chunked_upload.upload_id}."
                f" Cleaned File CSV with the ID {chunked_upload.upload_id}"
            )
        }


def download_file(request, file):
    """Download the csv file processed"""
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = file + ".csv"
    # Define the full file path
    filepath = BASE_DIR + "/csv_processed/" + filename
    # Open the file for reading content
    path = open(filepath, "r")
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response["Content-Disposition"] = "attachment; filename=%s" % filename
    # Return the response value
    return response
