###############################   IMPORT   ###############################

#for os gestion
import os

#for qrcode
import qrcode

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

try:
    import pkg_resources.py2_warn
except:
    pass
###############################



###############################   CODE   ###############################

###########   DEF   ###########

def showwifiprofile():
    global listevide
    global listeprofile
    global choixprofilend
        # nothing = blank
    nothing=""

        # In cmd 'netsh wlan show profile' give all ssid register in pc
    lineshowprofiles='netsh wlan show profile>result.txt'

        # Launch the command in cmd
    os.system(lineshowprofiles)
    listevide=[]
    listeprofile=[]
    ssidcount=0
    profilevariable='profile'
    removetextprofiles='    Profil Tous les utilisateurs    ÿ: '
    print('')
    fichier1profiles = open("result.txt","r")
    for ligneprofiles in fichier1profiles:
        if removetextprofiles in ligneprofiles:
            try:
                ssidcount=ssidcount+1
                strssidcount=str(ssidcount)

                ligneprofiles=ligneprofiles[39:]
                ligneprofiles=ligneprofiles[:-1]
                #print('['+strssidcount+'] '+ligneprofiles)
                exec("profile"+strssidcount+"='"+ligneprofiles+"'")
                listeprofile.append(ligneprofiles)
            except:
                pass
    fichier1profiles.close()        
    print('')
    choixprofilverif=False
    os.remove('result.txt')
    #while choixprofilverif==False:
        #choixprofil=int(input('Choix du profil [1 - '+strssidcount+']   > '))
        #try:
            #choixprofil=choixprofil-1
            #choixprofilend=listeprofile[choixprofil]
            
            #print(choixprofilend)
            #print('ok')
            #choixprofilverif=True
        #except:
            #print('error')

def veriflistvide():
    global listevide
    global listeprofile
    global valid_btn
    if listeprofile==listevide:
        listeprofile=["Error, no wifi !","","Help :","- Check your wifi drivers","- Save some ssid","- Insert your Wifikey"]
        valid_btn ['state'] = DISABLED
        valid_btn ['text'] = ' No Wifi save :( '
    else:
        valid_btn ['state'] = NORMAL


def showwifipasstest():
    global choixprofilend
    choixprofilend=listshowco.get(ANCHOR)
    #print(choixprofilend)
    showwifipass()

def showwifipass():
    global choixprofilend
    lignecheckpassword='netsh wlan show profile name="'+choixprofilend+'" key=clear | findstr clé>result2.txt'
    #print(lignecheckpassword)
    os.system(lignecheckpassword)

    removetext2='    Contenu de la cl‚            : ' 

    fichier = open("result2.txt","r")
    for ligne in fichier:
        password=ligne
        password=password[35:]
        password=password[:-1]
        #print(password)


    lignecheckaut='netsh wlan show profile name="'+choixprofilend+'" key=clear | findstr Authentification>result3.txt'
    #print(lignecheckaut)
    os.system(lignecheckaut)

    autsearchwpa='WPA'
    autsearchwpa='WEP'

    fichieraut = open("result3.txt","r")
    for ligne in fichieraut:
        if 'WPA' in ligne:
            autverif='WPA'
        elif 'WEP' in ligne:
            autverif='WEP'
        else:
            print('error')

    #print('network visible or not ?')
    #Visibilidad=input(' > ')
    Visibilidad = "true"

            
    qrrr='WIFI:T:'+autverif+';S:'+choixprofilend+';P:'+password+';H:'+Visibilidad+';'
    ##print(str(qrrr))
    img = qrcode.make(qrrr)
    img.save('qrcode.png')

    newWindow = Toplevel(app)

    fichier.close()
    fichieraut.close()
    
    os.remove('result2.txt')
    os.remove('result3.txt')
    
    try:
        newWindow.iconbitmap('wifi.ico')
    except:
        pass
    newWindow.wm_attributes('-topmost', 1)

        #Centrer fenetre tkinter
    screen_x = newWindow.winfo_screenwidth()
    screen_y = newWindow.winfo_screenheight()
    windows_x = 535
    windows_y= 500

    posX = (screen_x // 6)- (windows_x //2)
    posY = (screen_y // 2)- (windows_y //2)
    geo= "{}x{}+{}+{}".format(windows_x, windows_y, posX, posY)

    newWindow.geometry(geo)

        #redimensionable = False
    newWindow.resizable(width=False, height=False)

    photo = PhotoImage(file='qrcode.png')

    wifipassframe = LabelFrame(newWindow, text='[Qrcode : '+choixprofilend+']',font=("Comic Sans MS","10","italic" ))
    wifipassframe.grid(row=0, column=0, pady=15, padx=30)
    label = Label(wifipassframe, image=photo)
    label.grid(row=0, column=0, pady=15, padx=30)
    os.remove('qrcode.png') 
    newWindow.mainloop()
    
    

###########   ###   ###########

app = Tk()
app.title('ShowCo.Py | V 1')
try:
    app.iconbitmap('wifi.ico')
except:
    pass

##global var
##var = IntVar()
## 
##def result():
##    print(var.get())

    #Centrer fenetre tkinter
screen_x = app.winfo_screenwidth()
screen_y = app.winfo_screenheight()
windows_x = 575
windows_y= 900

posX = (screen_x // 2)- (windows_x //2)
posY = (screen_y // 2)- (windows_y //2)
geo= "{}x{}+{}+{}".format(windows_x, windows_y, posX, posY)

app.geometry(geo)

    #redimensionable = False
app.resizable(width=False, height=False)

    #title
mainframe = LabelFrame(app, text='[By Gugus | reverdyguillaume73@gmail.com]',font=("Russo One","12"), borderwidth='5px',cursor='X_cursor')
mainframe.grid(row=0, column=0, pady=10, padx=20)
label_welcome = Label(mainframe, text="ShowCo.Py",font=("Roboto Slab Light","50","bold" ))
label_welcome.grid(row=0, column=0, pady=15, padx=80)

    #listbox
showcoframe = LabelFrame(app, text='[All wifi already save]',font=("Comic Sans MS","10","italic" ))
showcoframe.grid(row=1, column=0, pady=15, padx=30)
listshowco=Listbox(showcoframe, width=20, borderwidth='2px',cursor='circle', font=("Catamaran Medium","20" ) )
listshowco.grid(row=0, column=0, pady=15, padx=30)

    #scrollbar
scrollbar = Scrollbar(showcoframe)
scrollbar.grid(row=0, column=1, sticky="news")

listshowco.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listshowco.yview) 



    #Bouton
buttonframe = LabelFrame(app, text='[Create Qrcode]',font=("Comic Sans MS","10","italic" ))
buttonframe.grid(row=2, column=0, pady=15, padx=30)
valid_btn = Button(buttonframe, text=" GET ", command=showwifipasstest,font=("Comic Sans MS","15" ), borderwidth='5px',cursor='iron_cross',state=DISABLED)
valid_btn.grid(row=0, column=0, pady=15, padx=30)

showwifiprofile()
veriflistvide()
for item in listeprofile:
    listshowco.insert(END, item)


app.mainloop()
