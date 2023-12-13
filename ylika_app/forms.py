from django import forms
from .models import Stock


# φόρμα που επιτρέπει στον χρήστη να δημιουργεί ένα νέο αντικείμενο 
# αποθέματος μέσω του user interaface.  

class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})

    class Meta:
        model = Stock
        fields = ['name', 'quantity']




# φόρμα που επιτρέπει στον χρήστη να δημιουργεί ένα νέο αντικείμενο 
# προιόντος μέσω του user interaface.

    # onoma
    # seriakos_arithmos 
    # perigrafi 



# φόρμα που επιτρέπει στον χρήστη να δημιουργεί ένα νέο αντικείμενο 
# παραγγελίας μέσω του user interaface.

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