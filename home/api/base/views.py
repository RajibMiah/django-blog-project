
from django.http import  response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from home.helper import *
from django.contrib.auth import authenticate , login
# from models import Profile


class loginView(APIView):

    def post(self , request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'

        try:
          data = request.data
          if data.get('username') is None:
              response['message'] = 'key username not found'
              raise Exception('key user not found')
          if data.get('password') is None:
              response['message'] = 'key password not found'
              raise Exception('key password not found')
          
          check_user = User.objects.filter(username = data.get('username')).first()

          if check_user is None:
              response['message'] = 'invalid username , user not found'    

          user_obj = authenticate(username = data.get('username') , password = data.get('password'))

          if user_obj:
              login(request , user_obj)
              response['status'] = 200
              response['message'] = 'wellcome'
          else:
              response['message'] = 'invalid passowrd'
              raise Exception('invalid password')



        except Exception as e:
            print(e)
        
        return Response(response)        


class RegisterView(APIView):
    response = {}
    response['status'] = 500
    response['message'] = 'Something went wrong'

    def post(self , request):
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] =  'Key username not found'
                raise Exception('key username is not found')

            if data.get('password') is None:
                response['message'] = 'Key password not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user:
                response['message'] = 'username already taken'
                raise Exception('username taken')

            user_obj = User.objects.create(email = data.get('username') , username = data.get('username'))

            user_obj.set_password(data.get('password'))

            user_obj.save()

            token = generate_random_string(20)
            """
            NOTE:: ISSUDE ON PROFILE CREATE
            """
            # Profile.objects.create(user = user_obj , token = token)

            #send_mail_to_user(token , data.get('username'))
            response['message'] = 'User created '
            response['status'] = 200
        
        except Exception as e :
                print(e)
                
        return Response(response)
            

                  