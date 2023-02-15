# from django import forms
#custom validation in fields and forms in django ,there are many ways to do this but I am going to assume that you are going to do
# this validation once in particular form ,if you are doing in a multiple places like multiple forms ,then you may have to consider
# making your own validator or even your own field but since you are limited to one form there is a particular method that you can use
# to validate the thing
# we have here a form with one value
#we have a template that renders it and
# we have a views that handles the anagram form so, nothing here is really important just to get the form
# the template is very straight forward

from django import forms

from example.core.models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title"]

    def clean_title(self):
        title = self.cleaned_data["title"]
        if not title:
            return title

        if not title[0].isupper():
            self.add_error("title", "Should start with an uppercase letter")

        if title.endswith("."):
            self.add_error("title", "Should not end with a full stop")

        if "&" in title:
            self.add_error("title", "Use 'and' instead of '&'")

        return title

# ******************************************************

# def is_anagram(x, y):
#     return sorted(x) == sorted(y)
# class AnagramForm(forms.Form):
#     test_value = forms.CharField(
#         label='Test value',
#         max_length=100,
#         widget=forms.TextInput(attrs={'class': "input"}))
#
#     def clean_test_value(self):
#         data = self.cleaned_data.get('test_value')
#
#         if not is_anagram(data, 'listen'):
#             raise forms.ValidationError('This is not an anagram of listen.')
#         return data


    # *********************************************


    # test_anagram = forms.CharField(
    #     label='Test anagram',
    #     max_length=100,
    #     widget=forms.TextInput(attrs={'class': "input"}))

    # def clean(self):
    #     cleaned_data = super().clean()
    #     test_value = cleaned_data.get('test_value')
    #     test_anagram = cleaned_data.get('test_anagram')

        # if test_value and test_anagram:
        # if not is_anagram(data, 'listen'):
        #     raise forms.ValueError('')
        # return data



