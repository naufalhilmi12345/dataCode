from django.shortcuts import render, redirect
import datetime
from .forms import dateForm
from .Model import Model

regression_model = Model()

# Create your views here.

###############################################################
# KITA SUKA SC KARENA IBU ARUNI YANG CANTIKKKKKKKKK BANGETTTT #
#               KASIH KITA NILAI A YA BU                      #
###############################################################

def homepage(request):
    dct = {}
    if request.method == 'POST':
        form = dateForm(request.POST)
        if (form.is_valid()):
            tanggal = form.cleaned_data['tanggal']
            tanggal_awal = datetime.date(2020, 3, 2)
            tanggal_max = datetime.date(2021, 3, 1)
            if (tanggal < tanggal_max):
                is_psbb = "check" in request.POST
                selisih_tanggal = tanggal - tanggal_awal
                prediction = None
                if is_psbb:
                    prediction = regression_model.predict(selisih_tanggal.days, "PSBB")
                else:
                    prediction = regression_model.predict(selisih_tanggal.days, "NO PSBB")

                #nampilin hasil.
                
            else:
                form = dateForm()
                dct = {
                    'form' : form,
                    'valid' : False
                }
                return render(request, 'homepage/homepage.html', dct)
        return redirect("/")
    else:
        form = dateForm()
        dct = {
            'form' : form,
            'valid' : True
        }   
        return render(request, 'homepage/homepage.html', dct)