import os
from index.models import NepSection, NepCourse


def handle_upload_videos(request):
    upload_path = 'media/' + request.POST['cour_id'] + '/' + request.FILES['file'].name
    dir_path = 'static/media/' + request.POST['cour_id'] + '/'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open('static/' + upload_path, 'wb+') as file_handler:
        for chunk in request.FILES['file'].chunks():
            file_handler.write(chunk)

    return {'status': 'SUCCESS',
            'path': upload_path}


def handle_reupload_videos(request):
    sect_obj = NepSection.objects.get(pk=request.POST['sect_id'])
    upload_path = 'media/' + str(sect_obj.sect_cour_id) + '/' + request.FILES['file'].name

    with open('static/' + upload_path, 'wb+') as file_handler:
        for chunk in request.FILES['file'].chunks():
            file_handler.write(chunk)

    sect_obj.sect_media = upload_path
    sect_obj.save()

    return {'status': 'SUCCESS'}

def handle_cour_image(request):
    cour_obj = NepCourse.objects.get(pk=request.POST['cour_id'])

    cour_obj.cour_image = request.FILES['file']
    cour_obj.save()
    return {'status': 'SUCCESS'}
