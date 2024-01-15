from django.db import models
from django.contrib.auth.models import User, Group

class Paraliptis(models.Model):
    id = models.AutoField(primary_key=True)
    onoma = models.CharField(max_length=150)
    monada = models.CharField(max_length=150)

    def __str__(self):
	    return self.monada

class Proion(models.Model):

    TYPOS_PROIONTOS_EPILOGES = (
        ("ΔΡΟΜΟΛΟΓΗΤΗΣ", "ΔΡΟΜΟΛΟΓΗΤΗΣ"), 
        ("CONVERTER", "CONVERTER"),
        ("SWITCH", "SWITCH"),
        ("MODULE", "MODULE"),
        ("ΜΕΤΑΤΡΟΠΕΑΣ", "ΜΕΤΑΤΡΟΠΕΑΣ"),
        ("LAN EXTENDER", "LAN EXTENDER"),
        ("ΚΑΛΩΔΙΩΣΗ", "ΚΑΛΩΔΙΩΣΗ"),
        ("ΚΑΜΙΑ ΕΠΙΛΟΓΗ", "ΚΑΜΙΑ ΕΠΙΛΟΓΗ"),
    )

    XRISI_PROIONTOS_EPILOGES = (
        ("ΔΙΔΕΣ ΔΙΚΤΥΑΚΟΣ ΕΞΟΠΛΙΣΜΟΣ", "ΔΙΔΕΣ ΔΙΚΤΥΑΚΟΣ ΕΞΟΠΛΙΣΜΟΣ"), 
        ("ΣΔΑ ΠΥΡΣΕΙΑ", "ΣΔΑ ΠΥΡΣΕΙΑ"),
        ("ΕΨΑΔ-ΤΗΛΕΦΩΝΙΚΟ ΚΕΝΤΡΟ", "ΕΨΑΔ-ΤΗΛΕΦΩΝΙΚΟ ΚΕΝΤΡΟ"),
        ("ΚΡΥΠΤΟ", "ΚΡΥΠΤΟ"),
        ("UPS", "UPS"),
        ("ΛΟΙΠΑ ΥΛΙΚΑ", "ΛΟΙΠΑ ΥΛΙΚΑ"),
        ("ΚΑΜΙΑ ΕΠΙΛΟΓΗ", "ΚΑΜΙΑ ΕΠΙΛΟΓΗ"),       
    )
    
    id = models.AutoField(primary_key=True)
    onoma = models.CharField(max_length=100, null = False)
    seriakos_arithmos = models.CharField(max_length=100, null = False)
    typos_proiontos = models.CharField(max_length=30, choices=TYPOS_PROIONTOS_EPILOGES, default='ΚΑΜΙΑ ΕΠΙΛΟΓΗ')
    xrisi = models.CharField(max_length=50, choices=XRISI_PROIONTOS_EPILOGES, default='ΚΑΜΙΑ ΕΠΙΛΟΓΗ')
    perigrafi = models.CharField(max_length=200, null=True)

    def __str__(self):
	    return self.onoma

    def get_total_stock(self):
        return self.apothema_set.aggregate(total_stock=models.Sum('posotita'))['total_stock'] or 0

    def has_enough_stock(self, requested_quantity):
        pass
    
class Apothiki(models.Model):
    id = models.AutoField(primary_key=True)
    onoma = models.CharField(max_length=100, null=True)
    perigrafi = models.CharField(max_length=200, null=True)
    simioseis = models.CharField(max_length=200, null=True, blank = True)

    def __str__(self):
	    return self.onoma

class Apothema(models.Model):
    id = models.AutoField(primary_key=True)
    posotita = models.IntegerField(default=1)
    simioseis = models.CharField(max_length=200, null=True, blank=True)
    proion = models.ForeignKey(Proion, on_delete=models.CASCADE)
    apothiki = models.ForeignKey(Apothiki, on_delete=models.CASCADE)
    # imera_paralavis = models.DateTimeField(auto_now_add=True)
    
class Paragelia(models.Model):
    id = models.AutoField(primary_key=True)
    onoma_paralipti = models.CharField(max_length=200, null=True, blank = True)
    monada_paralipti = models.ForeignKey(Paraliptis, on_delete=models.DO_NOTHING)
    perigrafi = models.CharField(max_length=200, null=True)
    dimiourgos = models.ForeignKey(User,models.DO_NOTHING)

    def __str__(self):
        return f'{self.onoma_paralipti}'
    
class PliroforiesParagellias(models.Model):
    id = models.AutoField(primary_key=True)
    paragelia = models.ForeignKey(Paragelia, on_delete=models.CASCADE)
    proion = models.ForeignKey(Proion, on_delete=models.CASCADE, null=True)
    posotita = models.IntegerField(default=1)
    imerominia = models.DateTimeField(auto_now=True)
    plirofories = models.CharField(max_length=200, null=True)
    apothiki = models.ForeignKey(Apothiki, on_delete=models.CASCADE)

    def returnTotalValue(self):
        pass 
        # we want this to return the inventory for all warehouses. 
