from django.contrib import admin


from childrenhealthcare.models import (Review,
                                       Subtitles,
                                       TbSections,
                                       Category,
                                       Articles,
                                       TbSubsections,
                                       Videos,
                                       CustomAdmin,
                                       UserData)

# Register your models here.
admin.site.site_header='Cildern Health Care'
admin.site.site_title='Cildern Health Care'
class Inlindata1(admin.StackedInline):
    model=TbSections
    extra=1

    
class InlindataTbSubsections(admin.StackedInline):
    
    model=TbSubsections
    extra=1
    
class InlindataCategorey(admin.StackedInline):
    model=Category
    extra=1
    
class InlindataArticles(admin.StackedInline):
    model=Articles
    extra=1

class InlindataVideos(admin.StackedInline):
    model=Videos
    extra=1
class InlindataSubtitles(admin.StackedInline):
    model=Subtitles
    extra=1

class sectionAdmin(admin.ModelAdmin):
    list_filter=("section_name",)
    search_fields=('section_name',)
    inlines=[InlindataTbSubsections]
    

class SubsectionAdmin(admin.ModelAdmin):
    list_filter=("subsection_name",)
    search_fields=('subsection_name',)
    inlines=[InlindataCategorey]


class CategoryAdmin(admin.ModelAdmin):
    list_filter=("category_name",)
    search_fields=('category_name',)
    inlines=[InlindataArticles,InlindataVideos]


class ArticlesAdmin(admin.ModelAdmin):
    list_filter=("title",)
    search_fields=('title',)


class VideosAdmin(admin.ModelAdmin):
    list_filter=("video_name",)
    search_fields=('article_name',)
    inlines=[InlindataSubtitles]
    

class SubtitleAdmin(admin.ModelAdmin):
    list_filter=("subtitle_name",)
    search_fields=('subtitle_name',)

admin.site.register(TbSections,sectionAdmin)
admin.site.register(TbSubsections,SubsectionAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Videos,VideosAdmin)
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Subtitles,SubtitleAdmin)
admin.site.register(Review)
admin.site.register(CustomAdmin)
admin.site.register(UserData)