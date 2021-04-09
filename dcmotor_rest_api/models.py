from djongo import models
from django import forms
# from djangotoolbox.fields import ListField, EmbeddedModelField

class Fault_Predict(models.Model):
    # timestamp = models.DateTimeField()
    strstamp = models.CharField(max_length=100)
    faultPredictval = models.DecimalField(decimal_places=4, max_digits=9)

    class Meta:
        abstract = True
    
class FaultPredictForm(forms.ModelForm):
    class Meta:
        model = Fault_Predict
        fields = (
            'strstamp', 'faultPredictval'
        )

class All_Status(models.Model):
    createdStr = models.CharField(max_length=100)
    faultval = models.DecimalField(decimal_places=4, max_digits=9)
    faultPredict = models.ArrayField(
        model_container=Fault_Predict,
        model_form_class=FaultPredictForm
    )
    speedVal = models.DecimalField(decimal_places=4, max_digits=9)
    currentVal = models.DecimalField(decimal_places=4, max_digits=9)

    def __str__(self):
        return self.createdStr