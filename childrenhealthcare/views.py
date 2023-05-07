import random
import string
import re
from django.contrib.auth.models import  User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,AllowAny
from social_django.utils import psa
# from requests.exceptions import HTTPError
from .serializers import (UserSerializer,
                          SectionSerializer,
                          SubSectionSerializer,
                          CategorySerializer,
                          ArticleSerializer ,
                          VideoSerializer ,
                          SubtitlesSerializer,
                          ReviewSerializer,
                          RegisterUserSerializer)
from .models import Articles,Category,Review,TbSections,TbSubsections,Videos,Subtitles,UserData
from rest_framework.decorators import api_view,action,permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.core.mail import EmailMessage
import pdb
from .permissions import NoDownloadPermission
import json
from django.conf import settings
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer



@api_view(['POST'])
def loginuser(request):
    data = json.loads(request.body)
    username=data.get("username")
    password=data.get("password")
    if username is None or username=='':
        return Response({"error": "User not found"})
    user=User.objects.filter(username=username).first()

    user_data=UserData.objects.filter(user=user).first()
    try:
        # pdb.set_trace()
        user_data.email_verified
    except AttributeError:
        return Response({'error': 'you are not register before.'}, status=status.HTTP_404_NOT_FOUND)
    if user_data.email_verified==True:
        loguser = authenticate(username=username, password=password)
        if not loguser:
            return Response({"error":"username or password not existing"},status=status.HTTP_404_NOT_FOUND)
        login(request, loguser)
        userID=User.objects.filter(username=username).first().pk
        uchild=UserData.objects.filter(user=userID).first().child_age
        if not uchild==''and uchild is not None:
            try:
                Section_Name = TbSections.objects.filter(child_age=uchild).first().section_name
                return Response({'message': 'User Login successfully','section_choice': Section_Name},status=status.HTTP_202_ACCEPTED)
            except AttributeError:
                pass
        else: return Response({'message': 'User Login successfully'},status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'error': 'Please verify your email address before logging in.'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def register(request):
    # pdb.set_trace()
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    valid_password= re.match(r'^(?=.*[A-Z])[A-Za-z0-9@#$%^&+=]*$', password) if True else False
    if username is None or username=='' or password is None or password=='':
        return Response({"error": "you can't register with empty username or password"},
                        status=status.HTTP_400_BAD_REQUEST)
    elif email is None or email=='':
        return Response({'error': 'Please enter your email to can log in'},
                        status=status.HTTP_400_BAD_REQUEST)
    elif (len(username) < 5) or not str(username).isalnum():
        return Response({'error': 'Username must be at least 5 characters long,and contain alphabet , numbers and not contain spaces.'},
                        status=status.HTTP_400_BAD_REQUEST)
    elif not valid_password or len(password) < 8:
            return Response({'error': 'Password must be at least 8 characters long , and start with capital letter contain alphabet , numbers , special character and not contain spaces.'},
                            status=status.HTTP_400_BAD_REQUEST)
    else:

        serializer = RegisterUserSerializer(data={
            'username': username,
            'password': password,
            'email': email
        })
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
            
        # Generate verification code and send verification email
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        user_data = UserData.objects.filter(user=user.pk).first()
        user_data.code_verification = code
        user_data.save()
        subject = 'Verify Your Email Address'
        message = f'Please enter the following code to verify your email address: {code}'
        email_message = EmailMessage(subject, message, to=[user.email])
        email_message.send()
        if data.get('child_age') is not None and not data.get('child_age')==''and isinstance(data.get('child_age'), str):
            user_data.child_age = data['child_age']
            user_data.save()
            return Response({"message": 'User created successfully,we send code to your email Please Verify your email'},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"message": 'User created successfully,we send code to your email Please Verify your email'},
                            status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def register(request):
#     # pdb.set_trace()
#     username = request.POST.get('username')
#     print('username',username)
#     password=request.POST.get('password')
#     email =request.POST.get('email')
#     if username ==None or password ==None:
#         return Response({"Error1":"you can't register with empty username or password"},
#                         status=status.HTTP_400_BAD_REQUEST)
#     elif  email ==None:
#         return Response({'Error': 'Please enter your email to can log in'},
#                         status=status.HTTP_400_BAD_REQUEST)
#     elif (len(username) < 5) or not str(username).isalnum():
#         return Response({'Error': 'Username must be at least 5 characters long,and contain alphabet , numbers and not contain spaces.'},
#                         status=status.HTTP_400_BAD_REQUEST)
#     elif not re.match(r"^(?=.*[A-Z])[A-Za-z0-9@#$%^&+=]*$", password) or len(password) < 8:
#             return Response({'Error': 'Password must be at least 8 characters long , and start with capital letter contain alphabet , numbers , special character and not contain spaces.'},
#                             status=status.HTTP_400_BAD_REQUEST)
#     else:
#         serializer = RegisterUserSerializer(data = {
#         'username': request.data['username'],
#         'password': request.data['password'],
#         'email': request.data['email']})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         # Generate verification code and send verification email
#         code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
#         user_data=UserData.objects.filter(user=user.pk).first()
#         user_data.code_verification=code
#         user_data.save()
#         subject = 'Verify Your Email Address'
#         message = f'Please enter the following code to verify your email address: {code}'
#         email_message = EmailMessage(subject, message, to=[user.email])
#         email_message.send()
#         if not request.data.get('child_age') == None:
#             user_data.child_age=request.data['child_age']
#             user_data.save()
#             return Response({"message": 'User created successfully,we send code to your email Please Verify your email'},status=status.HTTP_201_CREATED)
#         else:
#             return Response({"message": 'User created successfully,we send code to your email Please Verify your email'},status=status.HTTP_201_CREATED)


@api_view(['POST'])
def verify_email(request):
    data = json.loads(request.body)
    code = data.get("code")
    # pdb.set_trace()
    if code==None or code=='':
        return Response({'error':'please enter code that send to your email'},status=status.HTTP_400_BAD_REQUEST)
    else:
        user_data = UserData.objects.filter(code_verification=code).first()
        if not user_data:
            return Response({'error': 'Invalid verification code.'}, status=status.HTTP_400_BAD_REQUEST)

        user_data.email_verified = True
        user_data.code_verification = ''
        user_data.save()

        return Response({'message': 'Email address verified.'})
# @api_view(['POST'])
# def register(request):
#     username = request.data.get('username')
#     print(str(username).isalnum())
#     if (len(username) < 5) or not str(username).isalnum():
#         return Response({'error': 'Username must be at least 5 characters long,and alphabet and numbers and not contain spaces.'}, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         serializer = RegisterUserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         if request.data['child_age']:
#             section = TbSections.objects.filter(child_age=request.data['child_age']).first().pk
#             return Response({"Message": 'User create Successfully','Section choice':section})
#         return Response({"Message": 'User create Successfully'})

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def logout_user(request):
    logout(request)
    return Response({'message': 'User logged out successfully'})


@api_view(['POST'])
def reset_password(request):
    data = json.loads(request.body)
    email =data.get('email')
    if email is None or email=='':
        return Response({'error': 'Please enter your email to send email to can reset your password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.filter(email=email).first()
    if not user:
        return Response({'error': 'No user found with the provided email.'}, status=status.HTTP_404_NOT_FOUND)

    # Generate reset password code and send reset password email
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    user_data=UserData.objects.filter(user=user.pk).first()
    user_data.code_verification= code
    user_data.save()
    subject = 'Reset Your Password'
    message = f'Please enter the following code to reset your password: {code}'
    email_message = EmailMessage(subject, message, to=[user.email])
    email_message.send()

    return Response({'message': 'Reset password code sent to your email address.'} ,status=status.HTTP_200_OK)

@api_view(['POST'])
def reset_password_confirm(request):
    data = json.loads(request.body)
    code = data.get('code')
    password = request.data.get('password')
    valid_password= re.match(r'^(?=.*[A-Z])[A-Za-z0-9@#$%^&+=]*$', password) if True else False
    if code=='' or code is None:
        return Response({'error':'please enter code that send to your email'},status=status.HTTP_400_BAD_REQUEST)
    elif (password=='' and not valid_password or password is None or len(password) < 8):
        return Response({'error':'password must be at least 8 characters long , contain at least  one capital letter contain alphabet , numbers , special character and not contain spaces.'},
                        status=status.HTTP_400_BAD_REQUEST)

    else:
        # pdb.set_trace()
        userverfiy = UserData.objects.filter(code_verification=code).first()
        if not userverfiy:
            return Response({'error': 'Invalid reset password code.'}, status=status.HTTP_400_BAD_REQUEST)
        user=User.objects.filter(username=userverfiy).first()

        user.set_password(password)
        userverfiy.code_verification = ''
        userverfiy.save()
        user.save()

        return Response({'message': 'Password reset successfully.'})

#@psa():It connects our view with python-social-auth and adds details to the request object.
@api_view(['POST'])
@permission_classes([AllowAny])
@psa()
def register_by_google(request, backend):
    data = json.loads(request.body)
    token = data.get('access_token')
    user = request.backend.do_auth(token)
    if user:
        login(request, user) # log in the user
        return Response(
            {
                'message': 'User authenticated and registered successfully.'
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {
                'error': {
                    'token': 'Invalid token'
                    }
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

class SectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset= TbSections.objects.all()
    serializer_class= SectionSerializer
    permission_classes=[IsAuthenticatedOrReadOnly,]

class SubSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset= TbSubsections.objects.all()
    serializer_class=SubSectionSerializer
    permission_classes=[IsAuthenticatedOrReadOnly,]
    @action(detail=False, methods=['get'])
    def sectionById(self, request):
        section_id = request.query_params.get('section')
        if not section_id:
            return Response({'error': 'section parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        section = self.queryset.filter(section__id=section_id)
        name=TbSections.objects.filter(id=section_id).first()
        serializer = self.get_serializer(section, many=True)
        data = {
            'name': name.section_name,
            'subsection': serializer.data
        }

        return Response(data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAuthenticatedOrReadOnly,]
    @action(detail=False, methods=['get'])
    def SubsectionById(self, request):
        subsection_id = request.query_params.get('subsection')
        if not subsection_id:
            return Response({'error': 'subsection parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        subsection = self.queryset.filter(subsection__id=subsection_id)
        name=TbSubsections.objects.filter(id=subsection_id).first()
        serializer = self.get_serializer(subsection, many=True)
        data = {
            'category_name': name.subsection_name,
            'subsection': serializer.data
        }

        return Response(data)


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=[IsAuthenticatedOrReadOnly,]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'article_details']
    @action(detail=False, methods=['get'])
    def CategoryById(self, request):
        category_id = request.query_params.get('category')
        if not category_id:
            return Response({'error': 'category parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        category_name = Category.objects.filter(id=category_id).first()
        articles = self.queryset.filter(category__id=category_id)
        
        serializer = self.get_serializer(articles, many=True)
        data = {
            'category_name': category_name.category_name,
            'articles': serializer.data
        }

        return Response(data)
    @action(detail=False, methods=['get'])
    def by_subsection(self, request):
        subsection_name = request.query_params.get('subsection_name')
        subsection=TbSubsections.objects.filter(subsection_name=subsection_name).first()
        if subsection:
            queryset = Articles.objects.filter(category__subsection=subsection.pk)
        else:
            queryset = Articles.objects.none()
        serializer = self.get_serializer(queryset, many=True)
        data={"subsection_name":subsection_name,"Articles":serializer.data}
        return Response(data)


class VideoViewSet(viewsets.ModelViewSet):
    queryset=Videos.objects.filter(verified_video=True)
    serializer_class=VideoSerializer
    permission_classes=[IsAuthenticatedOrReadOnly,NoDownloadPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['video_name']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={'video_name':request.data['video_name'],
                                               'category':request.data['category'],
                                               'video_path':request.data['video_path']
                                               })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        targetvideo=Videos.objects.filter(video_name=request.data['video_name']).first()
        targetvideo.created_by=request.user
        targetvideo.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=False, methods=['get'])
    def CategoryById(self, request):
        category_id = request.query_params.get('category')
        if not category_id:
            return Response({'error': 'category parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        category_name = Category.objects.filter(id=category_id).first()
        videos = self.queryset.filter(category__id=category_id)
        serializer = self.get_serializer(videos, many=True)
        data = {
            'category_name': category_name.category_name,
            'videos': serializer.data
        }
        return Response(data)

# class VideoViewSetToCUD(viewsets.ModelViewSet):
#     queryset=Videos.objects.filter(verified_video=True)
#     serializer_class=VideoSerializer
#     permission_classes=[IsAuthenticated,]
#     # def retrieve(self, request, *args, **kwargs):
#     #     return Response({'Error':"you can't Get from this api"})
#     # def list(self, request, *args, **kwargs):
#     #     return Response({'Error':"you can't Get from this api"})



class SubtitlesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Subtitles.objects.all()
    serializer_class=SubtitlesSerializer
    @action(detail=False, methods=['get'])
    def VideoById(self, request):
        video_id = request.query_params.get('video_ID')
        if not video_id:
            return Response({'error': 'video_ID parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        subtitles = self.queryset.filter(video_ID_id=video_id)
        name=Videos.objects.filter(id=video_id).first()
        serializer = self.get_serializer(subtitles, many=True)
        data = {
            'video_name': name.video_name,
            'subtitles': serializer.data
        }

        return Response(data)

class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated,]
    @action(detail=False, methods=['get'])
    def ArtivlesReviewById(self, request):
        article_id = request.query_params.get('article_ID')
        if not article_id:
            return Response({'error': 'article_ID parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        article_name = Articles.objects.filter(id=article_id).first()
        reviwes = self.queryset.filter(article_ID_id=article_id)
        serializer = self.get_serializer(reviwes, many=True)
        data = {
            'article_name': article_name.title,
            'reviews': serializer.data
        }
        return Response(data)


class ReviewApi(APIView):
    permission_classes=[IsAuthenticated,]
    def post(self, request):
        rev = ReviewSerializer(data={
            "feedback":request.data['feedback'],
            "user_ID":request.user.id,
            "article_ID":request.data['article_ID']
        })
        if rev.is_valid():
            rev.save()
            return Response(rev.data, status=status.HTTP_200_OK)
        else:
            return Response(rev.errors, status=status.HTTP_200_OK)
        
        
        


