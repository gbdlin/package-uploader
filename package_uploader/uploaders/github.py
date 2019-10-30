from .base import BaseUploader


class GithubUploader(BaseUploader):
    uploader_name = 'github'
    RELEASE_GET_URL = 'https://api.github.com/repos/gbdlin/django-admin-toolbox/releases/tags/v{version}'
    RELEASE_CREATE_URL = 'https://api.github.com/repos/gbdlin/django-admin-toolbox/releases'
    ARTIFACT_UPLOAD_URL = '{release[upload_url]}?name={file.name}&label={file.label}'
    ARTIFACT_UPDATE_URL = '{file.url}'
    ARTIFACT_UPDATE_METHOD = 'patch'
    needs_upload_after_create = True
