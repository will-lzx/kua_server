import json
import logging
import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from weixin.models import Qiukua, Zan, Kua

logger = logging.getLogger(__name__)


@csrf_exempt
def getinfo(request):
    files_dict = {}
    return HttpResponse(json.dumps(files_dict), content_type='application/json')


@csrf_exempt
def save_qiu_kua(request):
    content = request.POST.get('content', None)
    owner = request.POST.get('openid', None)
    money = request.POST.get('money', None)
    status = False
    createtime = int(time.time())
    try:
        qiuKua = Qiukua()
        qiuKua.content = content
        qiuKua.owner = owner
        qiuKua.money = money
        qiuKua.status = status
        qiuKua.createtime = createtime
        qiuKua.save()
        result = {'status': False}
    except Exception as ex:
        logger.error('save qiukua failed:' + str(ex))
        result = {'status': False}
    return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def get_hot(request):
    qiuKua = Qiukua.objects.values('id').filter(status=False)
    hot_dict = {}
    for item in qiuKua:
        kua = Kua.objects.filter(qiuKua=item['id'])
        zan = Zan.objects.filter(kua__in=kua)
        hot_dict[item['id']] = len(zan)

    qiuKua = Qiukua.objects.filter(status=False, id__in=hot_dict.keys())
    return HttpResponse(json.dumps(qiuKua), content_type='application/json')

