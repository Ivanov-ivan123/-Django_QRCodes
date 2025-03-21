from django import forms
from .models import Subscription

class SubForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ["subscription", "desktopQuantity"]
        widgets = {
            "subscription": forms.TextInput(attrs = {
                "class": "form-input hidden-input",
                "placeholder": "Підписка"
                }
            ),
            "desktopQuantity": forms.NumberInput(attrs = {
                "class": "form-input",
                "placeholder": "5",
                }
            )
        }

    def save(self, user_id):
        sub = super().save(commit = False)
        sub.user_id = user_id
        sub.save()
