from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    # 위젯 설정 2.
    # title = forms.CharField(
    #     max_length=10, 
    #     label='제목',
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': '제목을 입력바랍니다.'
    #         }
    #     )
    # )
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목을 입력바랍니다.'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용을 입력바랍니다.',
            }
        )
    )
        
    class Meta:
        model = Article
        fields = ('title', 'content', 'image')
        # fields = ('title', )
        # exclude = ('title', )
        # 위젯 설정 1.
        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'placeholder': '제목을 입력바랍니다.'
        #         }
        #     )
        # }

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        widget=forms.Textarea(
            attrs={
                'placeholder': '...댓글댓글댓글댓글...',
                'rows': 3,
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('content', )

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10, 
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': '제목을 입력바랍니다.'
#             }
#         )
#     )
#     content = forms.CharField(
#         # label 내용 수정
#         label='내용',
#         # Django form에서 HTML 속성 지정 -> widget
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': '내용을 입력바랍니다.',
#                 'row': 3,
#                 'col': 30
#             }
#         )
#     )