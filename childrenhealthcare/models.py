from django.db import models
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import  User
from django.db.models.signals import post_save




class CustomAdmin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(verbose_name=_('phone'),max_length=20,blank=True, null=True)
    address = models.CharField(verbose_name=_('Address'),max_length=255,blank=True, null=True)

    def __str__(self):
        return self.user.username



class TbSections(models.Model):
    admin_ID = models.ForeignKey(CustomAdmin ,on_delete=models.CASCADE, null=True, blank=True)
    section_name = models.CharField(max_length=255)
    section_description = models.CharField(max_length=255, null=True, blank=True)
    section_image = models.ImageField(max_length=255,upload_to='image_sections/' ,blank=True, null=True)
    child_age = models.CharField(max_length=30, blank=True, null=True)

    class Meta:


        verbose_name=_('Section')
        verbose_name_plural=_('Sections')


    def __str__(self):
        return str(self.section_name)


class TbSubsections(models.Model):
    section = models.ForeignKey(TbSections,on_delete=models.CASCADE,blank=True, null=True)
    subsection_name = models.CharField(verbose_name=_('SubSection Name'),max_length=255)
    subsection_image = models.ImageField(verbose_name=_('SubSection Image'),max_length=255,upload_to='SubSection_Image/', blank=True, null=True)
    subsection_icon = models.ImageField(verbose_name=_('SubSection Icon'),max_length=255,upload_to='SubSection_Image/', blank=True, null=True)

    class Meta:


        verbose_name=_('Subsection')
        verbose_name_plural=_('Subsections')


    def __str__(self):
        return str(self.subsection_name)




class Category(models.Model):
    subsection = models.ForeignKey(TbSubsections,on_delete=models.CASCADE,blank=True, null=True)
    category_name = models.CharField(verbose_name=_('Category Name'),max_length=255)

    class Meta:


        verbose_name=_('category')
        verbose_name_plural=_('categories')


    def __str__(self):
        return str(self.category_name)

class Videos(models.Model):
    video_name = models.CharField(verbose_name=_('Video Name'),max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)
    video_path = models.FileField(verbose_name=_('Video'),max_length=255,upload_to='Videos/')
    class Meta:


        verbose_name=_('video')
        verbose_name_plural=_('videos')


    def __str__(self):
        return str(self.video_name)

class Subtitles(models.Model):
    video_ID = models.ForeignKey(Videos,on_delete=models.CASCADE,blank=True, null=True)
    subtitle_name=models.CharField(max_length=255,blank=True, null=True)
    subtitle = models.FileField(verbose_name=_('Subtitle'),max_length=255,upload_to='Subtitle/', blank=True, null=True)

    class Meta:
        verbose_name=_('Subtitle')
        verbose_name_plural=_('Subtitles')


    def __str__(self):
        return str(self.subtitle_name)


class Articles(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(verbose_name=_('Title'),max_length=255)
    article_details = models.TextField(verbose_name=_('Subject'))
    image_path = models.ImageField(verbose_name=_('Image'),upload_to='Articles_Images',max_length=255, blank=True, null=True)

    class Meta:


        verbose_name=_('Articles')
        verbose_name_plural=_('Article')


    def __str__(self):
        return str(self.title)


class UserData(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    SECTION_CHOICE=(('Pregnancy','Pregnancy'),
                ('0-3 months','0-3 months'),
                ('3-12 months','3-12 months'),
                ('1-3 years','1-3 years'),
                ('Autism','Autism'),
                ('Disability','Disability'))
    child_age = models.CharField(max_length=40,verbose_name=("user section"),choices=SECTION_CHOICE,null=True,blank=True)
    email_verified = models.BooleanField(default=False)
    code_verification = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name=_('User')
        verbose_name_plural=_('Users')

    def __str__(self):
        return'%s' %(self.user.username)


@receiver(post_save, sender=User)
def create_AnotherUserData(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        UserData.objects.create(user=instance)


class Review(models.Model):
    feedback = models.TextField(verbose_name=_('Comment'))
    user_ID = models.ForeignKey(UserData,verbose_name=_('Name'),on_delete=models.CASCADE,blank=True, null=True)
    article_ID = models.ForeignKey(Articles,verbose_name=_('Article'),on_delete=models.CASCADE,blank=True, null=True)

    class Meta:


        unique_together = (('user_ID', 'article_ID'),)
        verbose_name=_('Review')
        verbose_name_plural=_('Reviews')


    def __str__(self):
        return str(self.feedback)