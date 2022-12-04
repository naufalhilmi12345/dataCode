from django.shortcuts import render, redirect
from .forms import *
from django.db import connection
from django.contrib import messages

# Create your views here.
def login(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            cursor.execute('select password from medikago.pengguna where username like ' + "'" + username + "'")
            hasil = cursor.fetchall()
            if len(hasil) == 0:
                messages.info(request, 'Username atau Password salah')
                return redirect ('/login/')
            else:
                dataPassword = hasil[0][0]
                if password == dataPassword:
                    request.session['username'] = username
                    if is_admin(username):
                        request.session['role'] = 'administrator'
                    elif is_dokter(username):
                        request.session['role'] = 'dokter'
                    else:
                        request.session['role'] = 'pasien'
                    return redirect("/fiturhilmi/profile")
                else:
                    messages.info(request, 'Username atau Password salah')
                    return redirect('/login/')
        return redirect('/login/')
    else:
        form = login_form()
        response = {'form': form}
        return render(request,'login.html', response)

def is_admin(username):
    cursor = connection.cursor()
    cursor.execute('select username from medikago.administrator where username like ' + "'" + username + "'")
    hasil = cursor.fetchall()
    if len(hasil) ==0:
        return False
    else:
        return True

def is_dokter(username):
    cursor = connection.cursor()
    cursor.execute('select username from medikago.dokter where username like ' + "'" + username + "'")
    hasil = cursor.fetchall()
    if len(hasil) ==0:
        return False
    else:
        return True

def logout(request):
    request.session.flush()
    return redirect('/')

def homepage(request):
    return render(request, 'homepage.html')

def daftar_admin(request):
    cursor = connection.cursor()
    if request.method =='POST':
        form = DaftarAdministrator(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            nomor_identitas = form.cleaned_data['no_id']
            nama = form.cleaned_data['nama']
            ttl = form.cleaned_data['ttl']
            email = form.cleaned_data['email']
            alamat = form.cleaned_data['alamat']
            if check_nomor_id(nomor_identitas) and check_email(email):
                cursor.execute("insert into medikago.pengguna values ('{}','{}','{}','{}','{}','{}','{}')".format(email,username,password,nama,nomor_identitas,ttl,alamat))
                cursor.execute("select nomor_pegawai from medikago.administrator order by nomor_pegawai desc limit 1")
                nomor_pegawai_terakhir = int(cursor.fetchall()[0][0])
                if(nomor_pegawai_terakhir < 10):
                    cursor.execute("insert into medikago.administrator values ('0{}','{}','{}')".format((nomor_pegawai_terakhir+1),username,'02'))
                else:
                    cursor.execute("insert into medikago.administrator values ('{}','{}','{}')".format((nomor_pegawai_terakhir+1),username,'02'))
                request.session['username'] = username
                request.session['role'] = 'administrator'
                messages.info(request, 'Akun berhasil dibuat')
                return redirect("/fiturhilmi/profile")
            return redirect('/daftar_admin')
        return redirect('/daftar_admin')
    else:
        form = DaftarAdministrator()
        args = {'form': form}
        return render(request, 'daftar_admin.html', args)
            
def daftar_dokter(request):
    cursor = connection.cursor()
    if request.method =='POST':
        form = DaftarDokter(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            nomor_identitas = form.cleaned_data['no_id']
            nama = form.cleaned_data['nama']
            ttl = form.cleaned_data['ttl']
            email = form.cleaned_data['email']
            alamat = form.cleaned_data['alamat']
            sip = form.cleaned_data['sip']
            spesialisasi = form.cleaned_data['spesialisasi']
            if check_nomor_id(nomor_identitas) and check_email(email):
                cursor.execute("insert into medikago.pengguna values ('{}','{}','{}','{}','{}','{}','{}')".format(email,username,password,nama,nomor_identitas,ttl,alamat))
                cursor.execute("select id_dokter from medikago.dokter order by id_dokter desc limit 1")
                id_dokter_terakhir = int(cursor.fetchall()[0][0])
                if(id_dokter_terakhir < 9):
                    cursor.execute("insert into medikago.dokter values ('0{}','{}','{}','{}')".format((id_dokter_terakhir+1),username,sip,spesialisasi))
                else:
                    cursor.execute("insert into medikago.dokter values ('{}','{}','{}','{}')".format((id_dokter_terakhir+1),username,sip,spesialisasi))
                request.session['username'] = username
                request.session['role'] = 'dokter'
                messages.info(request, 'Akun berhasil dibuat')
                return redirect("/fiturhilmi/profile")
            return redirect('/daftar_dokter')
        return redirect('/daftar_dokter')
    else:
        form = DaftarDokter()
        args = {'form': form}
        return render(request, 'regis_dokter.html', args)

def daftar_pasien(request):
    cursor = connection.cursor()
    if request.method =='POST':
        form = DaftarPasien(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            nomor_identitas = form.cleaned_data['no_id']
            nama = form.cleaned_data['nama']
            ttl = form.cleaned_data['ttl']
            email = form.cleaned_data['email']
            alamat = form.cleaned_data['alamat']
            alergi = []
            alergi.append(form.cleaned_data['alergi'])
            angka = 1
            while True:
                try:
                    dataAlergi = 'alergi-' + str(angka)
                    data = request.POST[dataAlergi]
                    if len(data) != 0:
                        alergi.append(data)
                    angka += 1
                except:
                    break
            if check_nomor_id(nomor_identitas) and check_email(email):
                cursor.execute("insert into medikago.pengguna values ('{}','{}','{}','{}','{}','{}','{}')".format(email,username,password,nama,nomor_identitas,ttl,alamat))
                cursor.execute("select no_rekam_medis from medikago.pasien order by no_rekam_medis desc limit 1")
                no_rekam_medis_terakhir = cursor.fetchall()[0][0]
                last_number = no_rekam_medis_terakhir.split('-')
                last_number[2] = str(int(last_number[2])+1)
                cursor.execute("insert into medikago.pasien values ('{}-{}-{}','{}','{}')".format(last_number[0],last_number[1],last_number[2],username,'Armstrong Group'))
                for alergiPasien in alergi:
                    cursor.execute("insert into medikago.alergi_pasien values ('{}-{}-{}','{}')".format(last_number[0],last_number[1],last_number[2],alergiPasien))
                request.session['username'] = username
                request.session['role'] = 'pasien'
                messages.info(request, 'Akun berhasil dibuat')
                return redirect("/fiturhilmi/profile")
            return redirect('/daftar_pasien')
        return redirect('/daftar_pasien')
    else:
        form = DaftarPasien()
        args = {'form': form}
        return render(request, 'daftar_pasien.html', args)


def check_nomor_id(nomor_identitas):
    cursor = connection.cursor()
    cursor.execute('select nomor_id from medikago.pengguna where nomor_id like ' + "'" + nomor_identitas + "'")
    hasil = cursor.fetchall()
    if len(hasil) ==0:
        return True
    else:
        return False

def check_email(email):
    cursor = connection.cursor()
    cursor.execute('select email from medikago.pengguna where email like ' + "'" + email + "'")
    hasil = cursor.fetchall()
    if len(hasil) ==0:
        return True
    else:
        return False
