form .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'first_name',
            'last_name',
            'email',
            'title',
            'description',
            'price'
        ]
class RawProductForm(forms.Form):
    first_name = forms.CharField(maxlength=250)
    last_name = forms.Charfield(maxlength=250)
    email = forms.EmailField(maxlength=250)
    title = forms.Charfield(label = '', widget = forms.TextInput(attrs={"placeholder": "Your Title"}))
    description = forms.Charfield(
                        required = False,
                        widget=forms.Textarea(
                                    attrs={
                                          "placeholder": "Your Description",
                                          "class": "new-class-name two",
                                          "id": "my-id-for-textarea",
                                          "rows"=20,
                                          "cols"=120
                                    }
                             )
                        )

    price = forms.DecimalField(initial=199.99)

def clean_firstname(self, *args, **kwargs):
    first_name=self.cleaned_data.get("first_name")
    if not first_name:
        raise forms.ValidationError("This is not a Required Field")
    required = True
    return first_name

def clean_lastname(self, *args, **kwargs):
    last_name=self.cleaned_data.get("last_name")
    if not last_name:
        raise forms.ValidationError("This is not Required Field")
    required = True
    return last_name

def clean_email(self, *args, **kwargs):
    email = self.cleaned_data.get("first_name")
    if not email.endswith("edu"):
        raise forms.ValidationError("This is not valid email")
    required = True
    return email

def clean_title(self, *args, **kwargs):
    title=self.cleaned_data.get("title")
    if not "CFE" in title:
        raise forms.ValidationError("This is not a valid title")
    if not "books" in title:
        raise forms.ValidationError("This is not a valid title")
    if not "news" in title:
        raise forms.ValidationError("This is not a valid title")
    return title
