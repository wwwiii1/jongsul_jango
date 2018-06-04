import errno
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from keras.layers import Flatten
from keras.models import load_model
from PIL import Image
import os
import time
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from django.core.files.storage import FileSystemStorage
from check.models import UserLog
from django.contrib.auth.models import User
import keras


# Create your views here.
class checkPageView(TemplateView):
    template_name = 'check/check.html'

    def get_context_data(self, **kwargs):
        context = super(checkPageView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        #판단 알고리즘
        # https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html

        #clear session
        keras.backend.clear_session()

        image = request.FILES['file-upload']
        myTime = time.strftime('%H%M%S')
        im = Image.open(image)
        im.save('C:\\Users\\thswl\\PycharmProjects\\books\\check_directory\\test\\atopy\\'+myTime+'.jpg')

        test_datagen = ImageDataGenerator(rescale=1./ 255)
        test_set = test_datagen.flow_from_directory('C:\\develop\\picture\\jongsul_generator\\test',
                                                    target_size=(224, 224),
                                                    batch_size=1,
                                                    class_mode='binary')

        test_data = test_set.next()[0]
        model = load_model('Alexnet_final_epochs_1000.h5')
        output = model.predict(test_data)

        # 1 :normal 0 : atopy
        result = np.where(output >= 0.5, 1, 0)[0]

        # image 삭제
        os.remove('C:\\Users\\thswl\\PycharmProjects\\books\\check_directory\\test\\atopy\\' + myTime + '.jpg')

        #db에 저장
        # 현재 user 얻기 (session) 사용 http://egloos.zum.com/blackyyy/v/5314617
        req = request.session['user_id']

        #model reset
        #user_log db 에 저장, foreign키로 User가 걸려있어 넣어줌
        new_user_log = UserLog(username = req, atopy_true = result)
        new_user_log.save()

        return render(request,'check/check_result.html',{'result':result, 'user_id':req})



class checkResultPageView(TemplateView):
  pass

