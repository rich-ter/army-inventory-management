from django import forms
from .models import Proion, Apothema


# φόρμα που επιτρέπει στον χρήστη να δημιουργεί ένα νέο αντικείμενο 
# προιόντος μέσω του user interaface.

class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['onoma'].widget.attrs.update({'class': 'textinput form-control'})       
        self.fields['perigrafi'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['seriakos_arithmos'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['typos_proiontos'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['xrisi'].widget.attrs.update({'class': 'textinput form-control'})

    class Meta:
        model = Proion
        fields = ['onoma', 'perigrafi', 'seriakos_arithmos', 'typos_proiontos', 'xrisi']



# φόρμα που επιτρέπει στον χρήστη να δημιουργεί ένα νέο αντικείμενο 
# αποθέματος μέσω του user interaface.
#δεν εχει τελειωσει ακομα αυτό αλλαξε τα όλα όπως απο πανω. προφαση κωδικα λόγω μπήκε ο αλλος μέσα δεν έχω ιδέα τι κάνει όντως 

class ApothemaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['posotita'].widget.attrs.update({'class': 'text-input form-control'})
        self.fields['proion'].widget.attrs.update({'class': 'text-input form-control'})
        self.fields['apothiki'].widget.attrs.update({'class': 'text-input form-control'})
        self.fields['simioseis'].widget.attrs.update({'class': 'text-input form-control'})

    class Meta:
        model = Apothema
        fields = ['posotita', 'proion', 'apothiki', 'simioseis']

# φόρμα που επιτρέπει στον χρήστη να δημιουργεί ένα νέο αντικείμενο 
# παραγγελίας μέσω του user interaface.
class OrderForm(forms.ModelForm):
    pass


    # onoma_paralipti = models.CharField(max_length=200, null=True, blank = True)
    # monada_paralipti = models.ForeignKey(Paraliptis, on_delete=models.DO_NOTHING)
    # perigrafi = models.CharField(max_length=200, null=True)
    
    # paragelia = models.ForeignKey(Paragelia, on_delete=models.CASCADE)
    # proion = models.ForeignKey(Proion, on_delete=models.CASCADE, null=True)
    # posotita = models.IntegerField(default=1)
    # imerominia = models.DateTimeField(auto_now=True)
    # plirofories = models.CharField(max_length=200, null=True)
    # apothiki = models.ForeignKey(Apothiki, on_delete=models.CASCADE)

# φόρμα που επιτρέπει στον χρήστη να δημιουργεί ένα νέο αντικείμενο 
# αποθέματος μέσω του user interaface.