import os

from django.http import Http404, FileResponse, JsonResponse

from mini_backend import settings
import utils.response


def image(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        img_file = os.path.join(settings.IMAGE_DIR, md5 + '.jpeg')
        if not os.path.exists(img_file):
            return Http404()
        else:
            data = open(img_file, 'rb').read()
            print('return image: ' + img_file)
            return FileResponse(open(img_file, 'rb'), content_type='image/jpeg')


def image_text(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        img_file = os.path.join(settings.IMAGE_DIR, md5 + '.jpeg')
        if not os.path.exists(img_file):
            return utils.response.wrap_json_response(code=utils.response.ReturnCode.RESOURCES_NOT_EXISTS)
        else:
            response_data = {'name': md5 + '.jpeg', 'url': '/image?md5=%s' % (md5)}
            response = utils.response.wrap_json_response(data=response_data)
            return JsonResponse(data=response, safe=False)
