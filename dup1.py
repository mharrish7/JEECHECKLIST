import time
from kivymd_extensions.akivymd.uix.charts import AKPieChart
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager,FadeTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.snackbar import Snackbar
from kivy.animation import Animation
from kivymd.uix.spinner import MDSpinner
import threading
import csv

Window.size = (320,600)

colourb = '56/255,40/255,81/255,1'
colourf = '69/255,55/255,86/255,1'

class Welcome(MDScreen):
    pass

class Home(MDScreen):
    pass

class Chapterp(MDScreen):
    pass

class Chapterc(MDScreen):
    pass

class Chapterm(MDScreen):
    pass

chapmain = """
ScrollView:
    do_x_scroll : False
    MDGridLayout:
        spacing : dp(15)
        padding : [0,100,0,0]
        pos_hint : {'center_x' : 0.5 , 'center_y' : 0.5}
        id : chapgrid
        size_hint_y :  None
        height : self.minimum_height
        cols : 1
        
"""

chapcardp = """
MDCard:
    radius : dp(15)
    size_hint_y : None
    height : dp(40)
    md_bg_color : 69/255,55/255,86/255,1
    text : ''
    active : 0
    theory : 0
    rev : 0
    MDLabel:
        text : '  ' + root.text
    MDCheckbox:
        active : root.active
        id :check
        selected_color : 1,1,1,1
        size_hint :  None,None
        size : dp(48),dp(48)
        on_active : app.checkthreadfp()
    MDCheckbox:
        active : root.theory
        id :theory
        selected_color : 1,1,1,1
        size_hint :  None,None
        size : dp(48),dp(48)
        on_active : app.checkthreadfp()
    MDCheckbox:
        active : root.rev
        id :rev
        selected_color : 1,1,1,1
        size_hint :  None,None
        size : dp(48),dp(48)
        on_active : app.checkthreadfp()
    
"""
chapcardc = """
MDCard:
    radius : dp(15)
    size_hint_y : None
    height : dp(40)
    md_bg_color : 69/255,55/255,86/255,1
    text : ''
    active : 0
    theory : 0
    rev : 0
    MDLabel:
        text : '  ' + root.text
    MDCheckbox:
        id :check
        active : root.active
        selected_color : 1,1,1,1
        size_hint :  None,None
        size : dp(48),dp(48)
        on_active : app.checkthreadfc()
    MDCheckbox:
        active : root.theory
        id :theory
        selected_color : 1,1,1,1
        size_hint :  None,None
        size : dp(48),dp(48)
        on_active : app.checkthreadfc()
    MDCheckbox:
        active : root.rev
        id :rev
        selected_color : 1,1,1,1
        size_hint :  None,None
        size : dp(48),dp(48)
        on_active : app.checkthreadfc()
"""

chapcardm = """
MDCard:
    radius : dp(15)
    size_hint_y : None
    height : dp(40)
    md_bg_color : 69/255,55/255,86/255,1
    text : ''
    active : 0
    theory : 0
    rev : 0
    MDLabel:
        text : '  ' + root.text
    MDCheckbox:
        id :check
        active : root.active
        selected_color : 1,1,1,1
        size_hint :  None,None
        size : dp(48),dp(48)
        on_active : app.checkthreadfm()
    MDCheckbox:
        active : root.theory
        id :theory
        selected_color : 1,1,1,1
        size_hint :  None,None
        size : dp(48),dp(48)
        on_active : app.checkthreadfm()
    MDCheckbox:
        active : root.rev
        id :rev
        selected_color : 1,1,1,1
        size_hint :  None,None
        size : dp(48),dp(48)
        on_active : app.checkthreadfm()
    
       
"""

chapc = """
MDCard:
    radius : dp(17)
    md_bg_color : 69/255,55/255,86/255,1
    size_hint : (0.9,None)
    height : dp(39)
"""

subcard = """
MDCard:
    radius : dp(17)
    md_bg_color : 69/255,55/255,86/255,1
    size_hint : (0.9,None)
    height : dp(39)
    text : ''
    MDBoxLayout:
        Image:
            source : 'target.png'
        MDLabel:
            text : root.text
            font_style : 'Subtitle1'
        MDFillRoundFlatButton:
            id : subbut
            md_bg_color : 100 / 255, 70 / 255, 130 / 255, 1
            text : 'GO'
    
"""

cardt = """
MDCard:
    md_bg_color : 69/255,55/255,86/255,1
    size_hint : (0.6,None)
    height : dp(60)

"""

butt = """
MDFillRoundFlatButton:
    text : 'hello'
"""

scorep = 0
scorec = 0
scorem = 0
mfix = 0
pfix = 0
cfix = 0

physics = ['Measurements','Kinemetics','Laws of motion','Work & energy','Rotational','Gravitation','Solids and liquids'
           ,'Thermodynamics','Kinetic Theory','Oscillations','Waves','Electrostatics','Current elec','Magnetism'
           ,'Induction','AC','EM Waves','Optics','Dual Nature','Atoms and Nuclei','Electronic Devices','Communication']
chemistry = ['Basics','States of matter','Atomic structure','Chemical bonding','Thermodynamics','Solutions','Equilibrium'
             ,'Redox','Chemical kinetics','surface chem','Periodic table','Metallurgy','Hydrogen','s-block','p-block'
             ,'d-block','f-block','Coordinate comp','Environmental chem','Basics of organic','Hydrocarbons','Org-Halogens','Org-Oxygen'
            ,'Org-Nitrogen','Polymers','Biomolecules','Everyday life','Labworks']
maths = ['Sets','Functions','Relations','Complex numbers','Quadratic EQs','Matrix','Determinants','Permutations','Combinations','Math Induction',
         'Binomial theorem','Sequence and series','Limit & Continuity','Differentiability','Integrals','Diff EQs'
         ,'Co-ordinate geo','3-D','Vector','Stats & probability','Trignometry','Reasoning']

readerdat = []

try:
    file = open('data2.csv' , mode = 'r')
    reader = csv.reader(file,delimiter = ',')
    for row in reader:
        if row != []:
            readerdat.append(row)
    file.close()

except:
    file = open('data2.csv', mode = 'w')
    writer = csv.writer(file , delimiter = ',')
    for i in physics:
        writer.writerow(['p',i,0,0,0])
    for j in chemistry:
        writer.writerow(['c',j,0,0,0])
    for k in maths:
        writer.writerow(['m',k,0,0,0])
    file.close()
    file2 = open('data2.csv', mode = 'r')
    reader = csv.reader(file2,delimiter = ',')
    for row in reader:
        if row != []:
            readerdat.append(row)
    file2.close()





class JEECHECKLIST(MDApp):
    def backc(self):
        global pdata,cdata,mdata,readerdat,scorep,scorem,scorec,leng
        readerdat = []
        score = 0
        scoret = 0
        scorepyq = 0
        scorerev = 0
        self.sm.current = 'home'
        file = open('data2.csv',mode = 'w')
        writer = csv.writer(file,delimiter = ',')
        for i in pdata:
            writer.writerow(i)
        for j in cdata:
            writer.writerow(j)
        for k in mdata:
            writer.writerow(k)
        file.close()
        file2 = open('data2.csv',mode = 'r')
        reader = csv.reader(file2,delimiter = ',')
        for row in reader:
            if row!= []:
                readerdat.append(row)

        file2.close()
        for row in readerdat:
            if row != []:
                score = score + int(row[2]) + int(row[3]) + int(row[4])
                scoret = scoret + int(row[2])
                scorepyq = scorepyq + int(row[3])
                scorerev = scorerev + int(row[4])

        theory = (scoret/leng)*100
        pyq = (scorepyq/leng)*100
        revision = (scorerev/leng)*100


        items1 = [{'Done' : theory , 'Not Done' : abs(100-theory)}]
        items2 = [{'Done' : pyq , 'Not Done' : abs(100-pyq)}]
        items3 = [{'Done' : revision , 'Not Done' : abs(100-revision)}]

        self.piechart1.items = items1
        self.piechart2.items = items2
        self.piechart3.items = items3

        self.lab.text = str(score) + '/' + str(leng*3) + ' acheived'




    def checkthreadfc(self):
        global cardwc,scorec,cdata,readerdat
        cdata = []
        for row in readerdat:
            if row != [] and len(cardwc) == 0:
                if row[0] == 'c':
                    cdata.append(row)
        tempd = []
        scorec = 0
        for row in readerdat:
            if row != []:
                if row[0] == 'c':
                    tempd.append(row[1])

        for i in range(0,len(cardwc)):
            scorec = scorec + cardwc[i].ids['check'].active + cardwc[i].ids['theory'].active + cardwc[i].ids['rev'].active
            cdata.append(['c', tempd[i], int(cardwc[i].ids['check'].active), int(cardwc[i].ids['theory'].active),int(cardwc[i].ids['rev'].active)])
            scorec = int(scorec)
        try:
            self.tool2.title = str(scorec) + '/' + str(len(chemistry)*3)
        except:
            pass

    def checkthreadfp(self):
        global cardwp,scorep,pdata,readerdat
        pdata = []
        for row in readerdat:
            if row != [] and len(cardwp) == 0:
                if row[0] == 'p':
                    pdata.append(row)
        tempd = []
        scorep = 0
        for row in readerdat:
            if row != []:
                if row[0] == 'p':
                    tempd.append(row[1])

        for i in range(0,len(cardwp)):
            scorep = scorep + cardwp[i].ids['check'].active + cardwp[i].ids['theory'].active + cardwp[i].ids['rev'].active
            pdata.append(['p',tempd[i],int(cardwp[i].ids['check'].active),int(cardwp[i].ids['theory'].active),int(cardwp[i].ids['rev'].active)])
            scorep = int(scorep)
        try:
            self.tool1.title = str(scorep) + '/' + str(len(physics)*3)
        except:
            pass

    def checkthreadfm(self):
        global cardwm,scorem,mdata,readerdat
        mdata = []
        for row in readerdat:
            if row != [] and len(cardwm) == 0:
                if row[0] == 'm':
                    mdata.append(row)
        tempd = []
        scorem = 0
        for row in readerdat:
            if row != []:
                if row[0] == 'm':
                    tempd.append(row[1])

        for i in range(0,len(cardwm)):
            scorem = scorem + cardwm[i].ids['check'].active + cardwm[i].ids['theory'].active + cardwm[i].ids['rev'].active
            mdata.append(['m', tempd[i], int(cardwm[i].ids['check'].active), int(cardwm[i].ids['theory'].active),int(cardwm[i].ids['rev'].active)])
            scorem = int(scorem)
        try:
            self.tool3.title = str(scorem) + '/' + str(len(maths)*3)

        except:
            pass

    def fixchaptersp(self):
        Snackbar(text = 'Press back to save changes',duration = 1).open()
        global cardwp,readerdat,pdata

        tempd = []
        for row in readerdat:
            if row[0] == 'p':
                tempd.append(row)

        for i in range(0,len(tempd)):
            cardwp[i].text = tempd[i][1]
            cardwp[i].active = int(tempd[i][2])
            cardwp[i].theory = int(tempd[i][3])
            cardwp[i].rev = int(tempd[i][4])


        self.sm.transition = FadeTransition(duration = 0.3)
        self.sm.current = 'chapterp'
        self.checkthreadfp()


    def fixchaptersc(self):
        Snackbar(text = 'Press back to save changes',duration = 1).open()

        global cardwc,readerdat,cdata
        tempd = []
        for row in readerdat:
            if row[0] == 'c':
                tempd.append(row)

        for i in range(0, len(tempd)):
            cardwc[i].text = tempd[i][1]
            cardwc[i].active = int(tempd[i][2])
            cardwc[i].theory = int(tempd[i][3])
            cardwc[i].rev = int(tempd[i][4])

        self.sm.transition = FadeTransition(duration = 0.3)
        self.sm.current = 'chapterc'
        self.checkthreadfc()

    def fixchaptersm(self):
        Snackbar(text = 'Press back to save changes',duration = 1).open()

        global cardwm,readerdat,mdata
        tempd = []
        for row in readerdat:
            if row[0] == 'm':
                tempd.append(row)

        for i in range(0, len(tempd)):
            cardwm[i].text = tempd[i][1]
            cardwm[i].active = int(tempd[i][2])
            cardwm[i].theory = int(tempd[i][3])
            cardwm[i].rev = int(tempd[i][4])

        self.sm.transition = FadeTransition(duration = 0.3)
        self.sm.current = 'chapterm'
        self.checkthreadfm()


    def homes(self):
        self.sm.current = 'home'

    def homeswitch(self):
        time.sleep(0.5)
        self.home = Home(name='home')
        self.home.md_bg_color = (56 / 255, 40 / 255, 81 / 255, 1)
        self.sm.add_widget(self.home)

        self.chapterp = Chapterp(name='chapterp')
        self.chapterp.md_bg_color = (56 / 255, 40 / 255, 81 / 255, 1)
        self.sm.add_widget(self.chapterp)

        self.chapterc = Chapterc(name='chapterc')
        self.chapterc.md_bg_color = (56 / 255, 40 / 255, 81 / 255, 1)
        self.sm.add_widget(self.chapterc)

        self.chapterm = Chapterm(name='chapterm')
        self.chapterm.md_bg_color = (56 / 255, 40 / 255, 81 / 255, 1)
        self.sm.add_widget(self.chapterm)

        global scorep,scorem,scorec,cardwp,cardwm,cardwc,readerdat,leng
        cardwm=[]
        cardwc=[]
        cardwp=[]
        score = 0
        leng = 0
        scoret = 0
        scorepyq = 0
        scorerev =0
        for row in readerdat:
            if row != []:
                leng = leng + 1
                scoret = scoret + int(row[2])
                scorepyq = scorepyq + int(row[3])
                scorerev = scorerev + int(row[4])
                score = score + int(row[2]) + int(row[3]) + int(row[4])
        tool1 = MDToolbar(title='HOME', pos_hint={'top': 1})
        tool1.md_bg_color = 100 / 255, 70 / 255, 130 / 255, 1
        self.home.add_widget(tool1)
        cardp = Builder.load_string(cardt)
        cardp.pos_hint = {'center_x' : 0.5 , 'center_y' : 0.1}
        cardp.radius = 15
        self.lab = MDLabel(text = str(score) + '/' + str(leng*3) + '  acheived', font_style = 'H6',halign = 'center')
        cardp.add_widget(self.lab)
        self.home.add_widget(cardp)
        cardsub = Builder.load_string(subcard)
        cardsub.pos_hint = {'center_x' : 0.5 , 'center_y' : 0.45}
        cardsub.text = 'PHYSICS'
        cardsub.ids['subbut'].on_release = self.fixchaptersp
        self.home.add_widget(cardsub)
        cardsub2 = Builder.load_string(subcard)
        cardsub2.pos_hint = {'center_x': 0.5, 'center_y': 0.35}
        cardsub2.ids['subbut'].on_release = self.fixchaptersc
        cardsub2.text = 'CHEMISTRY'
        self.home.add_widget(cardsub2)
        cardsub3 = Builder.load_string(subcard)
        cardsub3.pos_hint = {'center_x': 0.5, 'center_y': 0.25}
        cardsub3.ids['subbut'].on_release = self.fixchaptersm
        cardsub3.text = 'MATHS'
        self.home.add_widget(cardsub3)
        self.checkthreadfp()
        self.checkthreadfm()
        self.checkthreadfc()
        theory = (scoret / leng) * 100
        pyq = (scorepyq / leng) * 100
        revision = (scorerev / leng) * 100

        items1 = [{'Done': theory, 'Not Done': abs(100 - theory)}]
        items2 = [{'Done': pyq, 'Not Done': abs(100 - pyq)}]
        items3 = [{'Done': revision, 'Not Done': abs(100 - revision)}]

        self.piechart1 = AKPieChart(items = items1,pos_hint = {'center_x' : 0.17 , 'center_y' : 0.75},size_hint = (0.3,0.15))
        self.home.add_widget(self.piechart1)
        self.piechart2 = AKPieChart(items=items2, pos_hint={'center_x': 0.5, 'center_y': 0.75}, size_hint=(0.3, 0.15))
        self.home.add_widget(self.piechart2)
        self.piechart3 = AKPieChart(items=items3, pos_hint={'center_x': 0.83, 'center_y': 0.75}, size_hint=(0.3,0.15))
        self.home.add_widget(self.piechart3)


        labt = MDLabel(text ='Theory',pos_hint={'center_x': 0.17, 'center_y': 0.6},halign = 'center')
        self.home.add_widget(labt)
        labp = MDLabel(text='PYQ', pos_hint={'center_x': 0.5, 'center_y': 0.6}, halign='center')
        self.home.add_widget(labp)
        labr = MDLabel(text='Revision', pos_hint={'center_x': 0.83, 'center_y': 0.6}, halign='center')
        self.home.add_widget(labr)

        #physcis
        cardwp = []
        self.boxc1 = MDBoxLayout(orientation='vertical')
        self.tool1 = MDToolbar(title='0/20', pos_hint={'top': 1})
        self.tool1.left_action_items = [['arrow-left', lambda x: self.backc()]]
        self.tool1.md_bg_color = 100 / 255, 70 / 255, 130 / 255, 1
        self.boxc1.add_widget(self.tool1)
        self.chapterp.add_widget(self.boxc1)
        main1 = Builder.load_string(chapmain)
        card1 = Builder.load_string(chapc)
        labchap = MDLabel(text='Chapters                                        Theory PYQ Revision', halign='center',
                          font_style='Subtitle2')
        card1.add_widget(labchap)
        main1.ids['chapgrid'].add_widget(card1)
        for row in readerdat:
            if row != []:
                if row[0] == 'p':
                    card = Builder.load_string(chapcardp)
                    main1.ids['chapgrid'].add_widget(card)
                    cardwp.append(card)

        self.boxc1.add_widget(main1)


        #chemistry
        cardwc = []
        self.boxc = MDBoxLayout(orientation='vertical')
        self.tool2 = MDToolbar(title='0/20', pos_hint={'top': 1})
        self.tool2.left_action_items = [['arrow-left', lambda x: self.backc()]]
        self.tool2.md_bg_color = 100 / 255, 70 / 255, 130 / 255, 1
        self.boxc.add_widget(self.tool2)
        self.chapterc.add_widget(self.boxc)
        main = Builder.load_string(chapmain)
        card = Builder.load_string(chapc)
        labchap = MDLabel(text='Chapters                                        Theory PYQ Revision', halign='center',
                          font_style='Subtitle2')
        card.add_widget(labchap)
        main.ids['chapgrid'].add_widget(card)
        for row in readerdat:
            if row != []:
                if row[0] == 'c':
                    card = Builder.load_string(chapcardc)
                    main.ids['chapgrid'].add_widget(card)
                    cardwc.append(card)

        self.boxc.add_widget(main)

        #maths
        cardwm = []
        self.boxc3 = MDBoxLayout(orientation='vertical')
        self.tool3 = MDToolbar(title='0/20', pos_hint={'top': 1})
        self.tool3.left_action_items = [['arrow-left', lambda x: self.backc()]]
        self.tool3.md_bg_color = 100 / 255, 70 / 255, 130 / 255, 1
        self.boxc3.add_widget(self.tool3)
        self.chapterm.add_widget(self.boxc3)
        main3 = Builder.load_string(chapmain)
        card3 = Builder.load_string(chapc)
        labchap = MDLabel(text='Chapters                                        Theory PYQ Revision', halign='center',
                          font_style='Subtitle2')
        card3.add_widget(labchap)
        main3.ids['chapgrid'].add_widget(card3)

        for row in readerdat:
            if row != []:
                if row[0] == 'm':
                    card = Builder.load_string(chapcardm)
                    main3.ids['chapgrid'].add_widget(card)
                    cardwm.append(card)

        self.boxc3.add_widget(main3)




        self.homes()

    def build(self):
        global cardt
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        self.sm = ScreenManager()
        welcome = Welcome(name = 'welcome')
        welcome.md_bg_color = (56/255,40/255,81/255,1)
        self.sm.add_widget(welcome)




        #welcome screen

        lab1 = MDLabel(text = 'WELCOME',theme_text_color = 'Custom',halign = 'center',font_style = 'H3')
        lab1.text_color = (56/255,40/255,81/255,1)
        animate = Animation(text_color = (1,1,1,1))
        animate.start(lab1)
        spin1 = MDSpinner(pos_hint = {'center_x' : 0.5 , 'center_y' : 0.3 }, size_hint = (0.2,0.2))


        welcome.add_widget(lab1)
        welcome.add_widget(spin1)


        #home
        self.iconc1 = Image(source='target.png')
        self.iconc2 = Image(source='book.png')


        loadthread = threading.Thread(target=self.homeswitch)
        loadthread.start()


        return self.sm






JEECHECKLIST().run()
