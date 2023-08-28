import json
from kivy import Config
from kivy.app import App
from functools import partial
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.utils import platform

#Config.set('graphics', 'resizable', 0)
#Config.set('graphics', 'width', 1080)
#Config.set('graphics', 'height', 2400)

class MyPopup(Popup):
    pass

class MyPopup_2(Popup):
    pass

class MyPopup_3(Popup):
    pass

class GameOverPopup(Popup):
    pass

class Portada(Screen):
    
    def press(self):

        name = self.ids.name_input.text
        if name != 'P':
            self.ids.passw.text = 'Contraseña incorrecta!\nPrueba otra vez'
            self.ids.name_input.text = ''
        else:
            self.ids.passw.text = 'Correcto!'
            self.ids.nex.disabled = False

        self.manager.get_screen('ronda1intro').ids.name_label.text = (
        f'¡Hola Yaiza!\nEn esta primera ronda tendrás que contestar ' 
        f'diez preguntas. Si aciertas una pregunta, acumularás 1.000€ '
        f'más en tu bote. El bote que obtengas será una de las posibilidades '
        f'por las que podrás jugar cuando conozcas al cazador/a, que '
        f'te hará dos ofertas: una más conservadora, con la que te será '
        f'más fácil sobrevivir a la caza; y una más arriesgada, con un '
        f'premio más suculento, pero con la que no tendrás margen de error. ' 
        f'¿Estás listo/a para la caza?'
        )
        # self.ids.name_input.text = ''

class Ronda1Intro(Screen):
    pass

class Ronda1Q0(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.start_new_music()

    def press(self, widget, ans, *args):

        true = 2

        with open('money.json', 'r') as f:
            money = json.load(f)

        q0oA = self.ids.q0o0
        q0oB = self.ids.q0o1
        q0oC = self.ids.q0o2
       
        animate_red = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_green = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_same = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)
        animate_gw = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        animate_red += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_green += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        animate_gw += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        
        animate_red += Animation(
                background_color=(1,0,0,1), 
                duration=0.001)
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=0.001)

        if ans == 0:
            animate_red.start(q0oA)
            animate_same.start(q0oB)
            animate_gw.start(q0oC)

        elif ans == 1:
            animate_same.start(q0oA)
            animate_red.start(q0oB)
            animate_gw.start(q0oC)

        elif ans == 2:
            animate_same.start(q0oA)
            animate_same.start(q0oB)
            animate_green.start(q0oC)
        
        Clock.schedule_once(lambda dt: self.reset_label(ans, true, money), 3)    
        self.ids.q0o0.disabled = True
        self.ids.q0o1.disabled = True
        self.ids.q0o2.disabled = True
        self.ids.nex.disabled = False

    def reset_label(self, ans, true, money):

        app = App.get_running_app()
        if ans == true:
            money += 1000
            self.ids.moneyQ0.text = f'{money}€'
            app.stop_music()   
            app.correct_music()

            #app.correct_music()

        else:
            self.ids.moneyQ0.text = f'{money}€'
            app.stop_music()   
            app.wrong_music()
        
        self.manager.get_screen('ronda1q1').ids.moneyQ0.text = f'{money}€'
   

class Ronda1Q1(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.start_new_music()

    def press(self, widget, ans, *args):
        
        money = int(self.manager.get_screen('ronda1q0').ids.moneyQ0.text[:-1])
        true = 2

        q0oA = self.ids.q0o0
        q0oB = self.ids.q0o1
        q0oC = self.ids.q0o2
       
        animate_red = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_green = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_same = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)
        animate_gw = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        animate_red += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_green += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        animate_gw += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        
        animate_red += Animation(
                background_color=(1,0,0,1), 
                duration=0.001)
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=0.001)

        if ans == 0:
            animate_red.start(q0oA)
            animate_same.start(q0oB)
            animate_gw.start(q0oC)

        elif ans == 1:
            animate_same.start(q0oA)
            animate_red.start(q0oB)
            animate_gw.start(q0oC)

        elif ans == 2:
            animate_same.start(q0oA)
            animate_same.start(q0oB)
            animate_green.start(q0oC)
        
        Clock.schedule_once(lambda dt: self.reset_label(ans, true, money), 3)    
        self.ids.q0o0.disabled = True
        self.ids.q0o1.disabled = True
        self.ids.q0o2.disabled = True
        self.ids.nex.disabled = False

        
    def reset_label(self, ans, true, money):
        app = App.get_running_app()
        if ans == true:
            money += 1000
            self.ids.moneyQ0.text = f'{money}€'
            app.stop_music()   
            app.correct_music()

            #app.correct_music()

        else:
            self.ids.moneyQ0.text = f'{money}€'
            app.stop_music()   
            app.wrong_music()
        
        self.manager.get_screen('ronda1q2').ids.moneyQ0.text = f'{money}€'

class Ronda1Q2(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.start_new_music()

    def press(self, widget, ans, *args):
        
        money = int(self.manager.get_screen('ronda1q1').ids.moneyQ0.text[:-1])
        true = 0

        q0oA = self.ids.q0o0
        q0oB = self.ids.q0o1
        q0oC = self.ids.q0o2
       
        animate_red = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_green = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_same = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)
        animate_gw = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        animate_red += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_green += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        animate_gw += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        
        animate_red += Animation(
                background_color=(1,0,0,1), 
                duration=0.001)
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=0.001)

        if ans == 0:
            animate_green.start(q0oA)
            animate_same.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 1:
            animate_gw.start(q0oA)
            animate_red.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 2:
            animate_gw.start(q0oA)
            animate_same.start(q0oB)
            animate_red.start(q0oC)

        Clock.schedule_once(lambda dt: self.reset_label(ans, true, money), 3)    
        self.ids.q0o0.disabled = True
        self.ids.q0o1.disabled = True
        self.ids.q0o2.disabled = True
        self.ids.nex.disabled = False
        
    def reset_label(self, ans, true, money):
        app = App.get_running_app()
        if ans == true:
            money += 1000
            self.ids.moneyQ0.text = f'{money}€'
            app.stop_music()   
            app.correct_music()

            #app.correct_music()

        else:
            self.ids.moneyQ0.text = f'{money}€'
            app.stop_music()   
            app.wrong_music()
        
        self.manager.get_screen('ronda1q3').ids.moneyQ0.text = f'{money}€'

class Ronda1Q3(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.start_new_music()

    def press(self, widget, ans, *args):
        
        money = int(self.manager.get_screen('ronda1q2').ids.moneyQ0.text[:-1])
        true = 1

        q0oA = self.ids.q0o0
        q0oB = self.ids.q0o1
        q0oC = self.ids.q0o2

        animate_red = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_green = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_same = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)
        animate_gw = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        animate_red += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_green += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        animate_gw += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        
        animate_red += Animation(
                background_color=(1,0,0,1), 
                duration=0.001)
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
       
        if ans == 0:
            animate_red.start(q0oA)
            animate_gw.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 1:
            animate_same.start(q0oA)
            animate_green.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 2:
            animate_same.start(q0oA)
            animate_gw.start(q0oB)
            animate_red.start(q0oC)
        
        Clock.schedule_once(lambda dt: self.reset_label(ans, true, money), 3)    
        self.ids.q0o0.disabled = True
        self.ids.q0o1.disabled = True
        self.ids.q0o2.disabled = True
        self.ids.nex.disabled = False

        
    def reset_label(self, ans, true, money):
        app = App.get_running_app()
        if ans == true:
            money += 1000
            self.ids.moneyQ0.text = f'{money}€'
            app.stop_music()   
            app.correct_music()

            #app.correct_music()

        else:
            self.ids.moneyQ0.text = f'{money}€'
            app.stop_music()   
            app.wrong_music()
        
        self.manager.get_screen('ronda1q4').ids.moneyQ0.text = f'{money}€'

class Ronda1Q4(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.start_new_music()

    def press(self, widget, ans, *args):
        
        money = int(self.manager.get_screen('ronda1q3').ids.moneyQ0.text[:-1])
        true = 0

        q0oA = self.ids.q0o0
        q0oB = self.ids.q0o1
        q0oC = self.ids.q0o2

        animate_red = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_green = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_same = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)
        animate_gw = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        animate_red += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_green += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        animate_gw += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        
        animate_red += Animation(
                background_color=(1,0,0,1), 
                duration=0.001)
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=0.001)

        if ans == 0:
            animate_green.start(q0oA)
            animate_same.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 1:
            animate_gw.start(q0oA)
            animate_red.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 2:
            animate_gw.start(q0oA)
            animate_same.start(q0oB)
            animate_red.start(q0oC)

        Clock.schedule_once(lambda dt: self.reset_label(ans, true, money), 3)    
        self.ids.q0o0.disabled = True
        self.ids.q0o1.disabled = True
        self.ids.q0o2.disabled = True
        self.ids.nex.disabled = False

    def reset_label(self, ans, true, money):
        app = App.get_running_app()
        if ans == true:
            money += 1000
            self.ids.moneyQ0.text = f'{money}€'
            app.stop_music()   
            app.correct_music()

            #app.correct_music()

        else:
            self.ids.moneyQ0.text = f'{money}€'
            app.stop_music()   
            app.wrong_music()
        
        self.manager.get_screen('ronda2ofertas').ids.p3.text = (
                f'{money}€'
                )

        self.manager.get_screen('ronda2intro').ids.name_label.text = (
        f'¡Enhorabuena Yaiza, has acumulado una cantidad de {money}€!\n' 
        f'Eso sí, ahora comienza lo verdaderamente complicado. En la '
        f'siguiente ronda conocerás al cazador o cazadora a quien te '
        f'enfrentarás. Te hará dos ofertas, y tú misma decidirás la '
        f'cantidad por la que jugarás. ¿Será la Gobernanta? ¿Será el '
        f'Justiciero? O tal vez la Espía o la Profesora? Lo sabrás en '
        f'la siguiente pantalla. Tal vez te lleves una sorpresa...' 
        )
        # self.ids.name_input.text = ''

class Ronda2Intro(Screen):
    pass

class Ronda2Cazadora(Screen):
    
    def press(self):
        app = App.get_running_app()
        app.stop_music()   
        app.start_cazadora_music()
        
        self.ids.descubrir.disabled = True
        Clock.schedule_once(lambda dt: self.intro_cazadora(), 11.1)    

    def intro_cazadora(self):
        self.ids.yaiza.opacity = 1
        self.ids.qiagener.opacity = 1
        self.ids.nex.disabled = False

class Ronda2Ofertas(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.start_new_music()

    def press(self, opt):

        animate_blue = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_stay = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        if opt == 'b1':
            animate_blue.start(self.ids.p2)
            animate_stay.start(self.ids.p3)
            animate_stay.start(self.ids.p4)

            self.manager.get_screen('ronda2q0').ids.p2.text = self.ids.p2.text
            self.manager.get_screen('ronda2q0').ids.p3.text = ''
            self.manager.get_screen('ronda2q0').ids.p4.text = ''

        elif opt == 'b2':
            animate_stay.start(self.ids.p2)
            animate_blue.start(self.ids.p3)
            animate_stay.start(self.ids.p4)

            self.manager.get_screen('ronda2q0').ids.p2.text = ''
            self.manager.get_screen('ronda2q0').ids.p3.text = self.ids.p3.text
            self.manager.get_screen('ronda2q0').ids.p4.text = ''

        elif opt == 'b3':
            animate_stay.start(self.ids.p2)
            animate_stay.start(self.ids.p3)
            animate_blue.start(self.ids.p4)

            self.manager.get_screen('ronda2q0').ids.p2.text = ''
            self.manager.get_screen('ronda2q0').ids.p3.text = ''
            self.manager.get_screen('ronda2q0').ids.p4.text = self.ids.p4.text

        self.ids.nex.disabled = False

    def oferta_baja(self):
        self.ids.oferta_alta.disabled = False
        oferta = int(float(self.ids.p3.text[:-1])*0.5)
        self.ids.p4.text = f'{oferta}€'
        app = App.get_running_app()
        app.open_popup_3()

    def oferta_alta(self):
        oferta = 50000
        self.ids.p2.text = f'{oferta}€'
        app = App.get_running_app()
        app.open_popup_2()

        
        self.ids.p2.disabled = False
        self.ids.p3.disabled = False
        self.ids.p4.disabled = False
        self.ids.oferta_baja.disabled = True 
        self.ids.oferta_alta.disabled = True

class Ronda2Q0(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.final_music()

    def press(self, ans):
        list_ps = [self.ids.p0.text, self.ids.p1.text,
                self.ids.p2.text, self.ids.p3.text,
                self.ids.p4.text, self.ids.p5.text,
                self.ids.p6.text, self.ids.p7.text,
                self.ids.p8.text]
        
        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1
        else:
            user_money = list_ps[user_p]
            
        true = 1
        q0oA = self.ids.q0o0
        q0oB = self.ids.q0o1
        q0oC = self.ids.q0o2

        animate_red = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_green = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_same = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)
        animate_gw = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        animate_red += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_green += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        animate_gw += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        
        animate_red += Animation(
                background_color=(1,0,0,1), 
                duration=0.001)
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
       
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=2.5)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=2.5)

        animate_green += Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)

        animate_caza = Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=8.5)
        animate_caza += Animation(
                background_color=(0.8,0.2,0.1,1), 
                duration=0.001)

        if ans == 0:
            animate_red.start(q0oA)
            animate_gw.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 1:
            animate_same.start(q0oA)
            animate_green.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 2:
            animate_same.start(q0oA)
            animate_gw.start(q0oB)
            animate_red.start(q0oC)

        p1 = self.ids.p1 
        animate_caza.start(p1)
        
        Clock.schedule_once(lambda dt: self.update(ans, true, user_p, list_ps), 3)    
        self.ids.q0o0.disabled = True
        self.ids.q0o1.disabled = True
        self.ids.q0o2.disabled = True
        self.ids.nex.disabled = False

    def update(self, ans, true, user_p, list_ps):
        
        app = App.get_running_app()
        app.stop_music()   
        app.correct_music()

        if ans == true:

            i = 0
            while list_ps[i] == '' or list_ps[i] == 'caza':
                i += 1
            else:
                list_ps[i+1] = list_ps[i]
                list_ps[i] = ''

        self.ids.p1.text = list_ps[1]
        self.ids.p2.text = list_ps[2]
        self.ids.p3.text = list_ps[3]
        self.ids.p4.text = list_ps[4]
        self.ids.p5.text = list_ps[5]
        self.ids.p6.text = list_ps[6]
        self.ids.p7.text = list_ps[7]

        if ans != true:
            app = App.get_running_app()
            app.open_popup()

        self.manager.get_screen('ronda2q1').ids.p1.text= list_ps[1]
        self.manager.get_screen('ronda2q1').ids.p2.text= list_ps[2]
        self.manager.get_screen('ronda2q1').ids.p3.text= list_ps[3]
        self.manager.get_screen('ronda2q1').ids.p4.text= list_ps[4]
        self.manager.get_screen('ronda2q1').ids.p5.text= list_ps[5]
        self.manager.get_screen('ronda2q1').ids.p6.text= list_ps[6]
        self.manager.get_screen('ronda2q1').ids.p7.text= list_ps[7]

class Ronda2Q1(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.final_music()

    def press(self, ans):
        list_ps = [self.ids.p0.text, self.ids.p1.text,
                self.ids.p2.text, self.ids.p3.text,
                self.ids.p4.text, self.ids.p5.text,
                self.ids.p6.text, self.ids.p7.text,
                self.ids.p8.text]
        
        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1
        else:
            user_money = list_ps[user_p]
            
        true = 0
        q0oA = self.ids.q0o0
        q0oB = self.ids.q0o1
        q0oC = self.ids.q0o2

        animate_red = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_green = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_same = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)
        animate_gw = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        animate_red += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_green += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        animate_gw += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        
        animate_red += Animation(
                background_color=(1,0,0,1), 
                duration=0.001)
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
       
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=2.5)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=2.5)

        animate_green += Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)

        animate_caza = Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=8.5)
        animate_caza += Animation(
                background_color=(0.8,0.2,0.1,0.9), 
                duration=0.001)

        if ans == 0:
            animate_green.start(q0oA)
            animate_same.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 1:
            animate_gw.start(q0oA)
            animate_red.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 2:
            animate_gw.start(q0oA)
            animate_same.start(q0oB)
            animate_red.start(q0oC)

        p2 = self.ids.p2 
        animate_caza.start(p2)
        
        Clock.schedule_once(lambda dt: self.update(ans, true, user_p, list_ps), 3)    
        self.ids.q0o0.disabled = True
        self.ids.q0o1.disabled = True
        self.ids.q0o2.disabled = True
        self.ids.nex.disabled = False

    def update(self, ans, true, user_p, list_ps):
        
        app = App.get_running_app()
        app.stop_music()   
        app.correct_music()

        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1

        if ans == true:
            user_p += 1
            i = 0
            while list_ps[i] == '' or list_ps[i] == 'caza':
                i += 1
            else:
                list_ps[i+1] = list_ps[i]
                list_ps[i] = ''
        
        self.ids.p1.text = list_ps[1]
        self.ids.p2.text = list_ps[2]
        self.ids.p3.text = list_ps[3]
        self.ids.p4.text = list_ps[4]
        self.ids.p5.text = list_ps[5]
        self.ids.p6.text = list_ps[6]
        self.ids.p7.text = list_ps[7]

        if ans != true:
            app = App.get_running_app()
            app.open_popup()
        
        caza_p = 2
        if user_p == caza_p:
            app = App.get_running_app()
            app.game_over_popup()
            app.stop()

        self.manager.get_screen('ronda2q2').ids.p1.text= list_ps[1]
        self.manager.get_screen('ronda2q2').ids.p2.text= list_ps[2]
        self.manager.get_screen('ronda2q2').ids.p3.text= list_ps[3]
        self.manager.get_screen('ronda2q2').ids.p4.text= list_ps[4]
        self.manager.get_screen('ronda2q2').ids.p5.text= list_ps[5]
        self.manager.get_screen('ronda2q2').ids.p6.text= list_ps[6]
        self.manager.get_screen('ronda2q2').ids.p7.text= list_ps[7]

class Ronda2Q2(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.final_music()

    def press(self, ans):
        list_ps = [self.ids.p0.text, self.ids.p1.text,
                self.ids.p2.text, self.ids.p3.text,
                self.ids.p4.text, self.ids.p5.text,
                self.ids.p6.text, self.ids.p7.text,
                self.ids.p8.text]
        
        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1
        else:
            user_money = list_ps[user_p]
            
        true = 2
        q0oA = self.ids.q0o0
        q0oB = self.ids.q0o1
        q0oC = self.ids.q0o2

        animate_red = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_green = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_same = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)
        animate_gw = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        animate_red += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_green += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        animate_gw += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        
        animate_red += Animation(
                background_color=(1,0,0,1), 
                duration=0.001)
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
       
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=2.5)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=2.5)

        animate_green += Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)

        animate_caza = Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=8.5)
        animate_caza += Animation(
                background_color=(0.8,0.2,0.1,0.9), 
                duration=0.001)

        if ans == 0:
            animate_red.start(q0oA)
            animate_same.start(q0oB)
            animate_gw.start(q0oC)

        elif ans == 1:
            animate_same.start(q0oA)
            animate_red.start(q0oB)
            animate_gw.start(q0oC)

        elif ans == 2:
            animate_same.start(q0oA)
            animate_same.start(q0oB)
            animate_green.start(q0oC)

        p3 = self.ids.p3 
        animate_caza.start(p3)
        
        Clock.schedule_once(lambda dt: self.update(ans, true, user_p, list_ps), 3)    
        self.ids.q0o0.disabled = True
        self.ids.q0o1.disabled = True
        self.ids.q0o2.disabled = True
        self.ids.nex.disabled = False

    def update(self, ans, true, user_p, list_ps):
        
        app = App.get_running_app()
        app.stop_music()   
        app.correct_music()

        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1

        if ans == true:
            user_p += 1
            i = 0
            while list_ps[i] == '' or list_ps[i] == 'caza':
                i += 1
            else:
                list_ps[i+1] = list_ps[i]
                list_ps[i] = ''
        
        if ans != true:
            app = App.get_running_app()
            app.open_popup()

        self.ids.p1.text = list_ps[1]
        self.ids.p2.text = list_ps[2]
        self.ids.p3.text = list_ps[3]
        self.ids.p4.text = list_ps[4]
        self.ids.p5.text = list_ps[5]
        self.ids.p6.text = list_ps[6]
        self.ids.p7.text = list_ps[7]
        
        caza_p = 3
        if user_p == caza_p:
            app = App.get_running_app()
            app.game_over_popup()
            app.stop()

        self.manager.get_screen('ronda2q3').ids.p1.text= list_ps[1]
        self.manager.get_screen('ronda2q3').ids.p2.text= list_ps[2]
        self.manager.get_screen('ronda2q3').ids.p3.text= list_ps[3]
        self.manager.get_screen('ronda2q3').ids.p4.text= list_ps[4]
        self.manager.get_screen('ronda2q3').ids.p5.text= list_ps[5]
        self.manager.get_screen('ronda2q3').ids.p6.text= list_ps[6]
        self.manager.get_screen('ronda2q3').ids.p7.text= list_ps[7]

class Ronda2Q3(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.final_music()

    def press(self, ans):
        list_ps = [self.ids.p0.text, self.ids.p1.text,
                self.ids.p2.text, self.ids.p3.text,
                self.ids.p4.text, self.ids.p5.text,
                self.ids.p6.text, self.ids.p7.text,
                self.ids.p8.text]
        
        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1
        else:
            user_money = list_ps[user_p]
            
        true = 1
        q0oA = self.ids.q0o0
        q0oB = self.ids.q0o1
        q0oC = self.ids.q0o2

        animate_red = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_green = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_same = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)
        animate_gw = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        animate_red += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_green += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        animate_gw += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        
        animate_red += Animation(
                background_color=(1,0,0,1), 
                duration=0.001)
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
       
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=2.5)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=2.5)

        animate_green += Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)

        animate_caza = Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=8.5)
        animate_caza += Animation(
                background_color=(0.8,0.2,0.1,0.9), 
                duration=0.001)

        if ans == 0:
            animate_red.start(q0oA)
            animate_gw.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 1:
            animate_same.start(q0oA)
            animate_green.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 2:
            animate_same.start(q0oA)
            animate_gw.start(q0oB)
            animate_red.start(q0oC)

        p4 = self.ids.p4 
        animate_caza.start(p4)
        
        Clock.schedule_once(lambda dt: self.update(ans, true, user_p, list_ps), 3)    
        self.ids.q0o0.disabled = True
        self.ids.q0o1.disabled = True
        self.ids.q0o2.disabled = True
        self.ids.nex.disabled = False

    def update(self, ans, true, user_p, list_ps):
        
        app = App.get_running_app()
        app.stop_music()   
        app.correct_music()

        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1

        if ans == true:
            user_p += 1
            if user_p == 8:
                self.ids.p8.disabled = False
                self.ids.p8.text = 'FIN'
                self.ids.nex.disabled = True

            i = 0
            while list_ps[i] == '' or list_ps[i] == 'caza':
                i += 1
            else:
                list_ps[i+1] = list_ps[i]
                list_ps[i] = ''
        
        if ans != true:
            app = App.get_running_app()
            app.open_popup()

        self.ids.p1.text = list_ps[1]
        self.ids.p2.text = list_ps[2]
        self.ids.p3.text = list_ps[3]
        self.ids.p4.text = list_ps[4]
        self.ids.p5.text = list_ps[5]
        self.ids.p6.text = list_ps[6]
        self.ids.p7.text = list_ps[7]
        
        caza_p = 4
        if user_p == caza_p:
            app = App.get_running_app()
            app.game_over_popup()
            app.stop()

        self.manager.get_screen('ronda2q4').ids.p1.text= list_ps[1]
        self.manager.get_screen('ronda2q4').ids.p2.text= list_ps[2]
        self.manager.get_screen('ronda2q4').ids.p3.text= list_ps[3]
        self.manager.get_screen('ronda2q4').ids.p4.text= list_ps[4]
        self.manager.get_screen('ronda2q4').ids.p5.text= list_ps[5]
        self.manager.get_screen('ronda2q4').ids.p6.text= list_ps[6]
        self.manager.get_screen('ronda2q4').ids.p7.text= list_ps[7]

class Ronda2Q4(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.final_music()

    def press(self, ans):
        list_ps = [self.ids.p0.text, self.ids.p1.text,
                self.ids.p2.text, self.ids.p3.text,
                self.ids.p4.text, self.ids.p5.text,
                self.ids.p6.text, self.ids.p7.text,
                self.ids.p8.text]
        
        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1
        else:
            user_money = list_ps[user_p]
            
        true = 2
        q0oA = self.ids.q0o0
        q0oB = self.ids.q0o1
        q0oC = self.ids.q0o2

        animate_red = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_green = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_same = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)
        animate_gw = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        animate_red += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_green += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        animate_gw += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        
        animate_red += Animation(
                background_color=(1,0,0,1), 
                duration=0.001)
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
       
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=2.5)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=2.5)

        animate_green += Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)

        animate_caza = Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=8.5)
        animate_caza += Animation(
                background_color=(0.8,0.2,0.1,0.9), 
                duration=0.001)

        if ans == 0:
            animate_red.start(q0oA)
            animate_same.start(q0oB)
            animate_gw.start(q0oC)

        elif ans == 1:
            animate_same.start(q0oA)
            animate_red.start(q0oB)
            animate_gw.start(q0oC)

        elif ans == 2:
            animate_same.start(q0oA)
            animate_same.start(q0oB)
            animate_green.start(q0oC)

        p5 = self.ids.p5 
        animate_caza.start(p5)
        
        Clock.schedule_once(lambda dt: self.update(ans, true, user_p, list_ps), 3)    
        self.ids.q0o0.disabled = True
        self.ids.q0o1.disabled = True
        self.ids.q0o2.disabled = True
        self.ids.nex.disabled = False

    def update(self, ans, true, user_p, list_ps):
        
        app = App.get_running_app()
        app.stop_music()   
        app.correct_music()

        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1

        if ans == true:
            user_p += 1
            if user_p == 8:
                self.ids.p8.disabled = False
                self.ids.p8.text= 'FIN'
                self.ids.nex.disabled = True
            i = 0
            while list_ps[i] == '' or list_ps[i] == 'caza':
                i += 1
            else:
                list_ps[i+1] = list_ps[i]
                list_ps[i] = ''
        
        if ans != true:
            app = App.get_running_app()
            app.open_popup()

        self.ids.p1.text = list_ps[1]
        self.ids.p2.text = list_ps[2]
        self.ids.p3.text = list_ps[3]
        self.ids.p4.text = list_ps[4]
        self.ids.p5.text = list_ps[5]
        self.ids.p6.text = list_ps[6]
        self.ids.p7.text = list_ps[7]
        
        caza_p = 5
        if user_p == caza_p:
            app = App.get_running_app()
            app.game_over_popup()
            app.stop()

        self.manager.get_screen('ronda2q5').ids.p1.text= list_ps[1]
        self.manager.get_screen('ronda2q5').ids.p2.text= list_ps[2]
        self.manager.get_screen('ronda2q5').ids.p3.text= list_ps[3]
        self.manager.get_screen('ronda2q5').ids.p4.text= list_ps[4]
        self.manager.get_screen('ronda2q5').ids.p5.text= list_ps[5]
        self.manager.get_screen('ronda2q5').ids.p6.text= list_ps[6]
        self.manager.get_screen('ronda2q5').ids.p7.text= list_ps[7]

class Ronda2Q5(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.final_music()

    def press(self, ans):
        list_ps = [self.ids.p0.text, self.ids.p1.text,
                self.ids.p2.text, self.ids.p3.text,
                self.ids.p4.text, self.ids.p5.text,
                self.ids.p6.text, self.ids.p7.text,
                self.ids.p8.text]
        
        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1
        else:
            user_money = list_ps[user_p]
            
        true = 1
        q0oA = self.ids.q0o0
        q0oB = self.ids.q0o1
        q0oC = self.ids.q0o2

        animate_red = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_green = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_same = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)
        animate_gw = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        animate_red += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_green += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        animate_gw += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        
        animate_red += Animation(
                background_color=(1,0,0,1), 
                duration=0.001)
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
       
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=2.5)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=2.5)

        animate_green += Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)

        animate_caza = Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=8.5)
        animate_caza += Animation(
                background_color=(0.8,0.2,0.1,0.9), 
                duration=0.001)

        if ans == 0:
            animate_red.start(q0oA)
            animate_gw.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 1:
            animate_same.start(q0oA)
            animate_green.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 2:
            animate_same.start(q0oA)
            animate_gw.start(q0oB)
            animate_red.start(q0oC)

        p6 = self.ids.p6 
        animate_caza.start(p6)
        
        Clock.schedule_once(lambda dt: self.update(ans, true, user_p, list_ps), 3)    
        self.ids.q0o0.disabled = True
        self.ids.q0o1.disabled = True
        self.ids.q0o2.disabled = True
        self.ids.nex.disabled = False

    def update(self, ans, true, user_p, list_ps):
        
        app = App.get_running_app()
        app.stop_music()   
        app.correct_music()

        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1

        if ans == true:
            user_p += 1
            if user_p == 8:
                self.ids.p8.disabled = False
                self.ids.nex.disabled = True
                self.ids.p8.text = 'FIN'
            i = 0
            while list_ps[i] == '' or list_ps[i] == 'caza':
                i += 1
            else:
                list_ps[i+1] = list_ps[i]
                list_ps[i] = ''
        
        if ans != true:
            app = App.get_running_app()
            app.open_popup()

        self.ids.p1.text = list_ps[1]
        self.ids.p2.text = list_ps[2]
        self.ids.p3.text = list_ps[3]
        self.ids.p4.text = list_ps[4]
        self.ids.p5.text = list_ps[5]
        self.ids.p6.text = list_ps[6]
        self.ids.p7.text = list_ps[7]
        
        caza_p = 6
        if user_p == caza_p:
            app = App.get_running_app()
            app.game_over_popup()
            app.stop()

        self.manager.get_screen('ronda2q6').ids.p1.text= list_ps[1]
        self.manager.get_screen('ronda2q6').ids.p2.text= list_ps[2]
        self.manager.get_screen('ronda2q6').ids.p3.text= list_ps[3]
        self.manager.get_screen('ronda2q6').ids.p4.text= list_ps[4]
        self.manager.get_screen('ronda2q6').ids.p5.text= list_ps[5]
        self.manager.get_screen('ronda2q6').ids.p6.text= list_ps[6]
        self.manager.get_screen('ronda2q6').ids.p7.text= list_ps[7]

class Ronda2Q6(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.final_music()

    def press(self, ans):
        list_ps = [self.ids.p0.text, self.ids.p1.text,
                self.ids.p2.text, self.ids.p3.text,
                self.ids.p4.text, self.ids.p5.text,
                self.ids.p6.text, self.ids.p7.text,
                self.ids.p8.text]
        
        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1
        else:
            user_money = list_ps[user_p]
            
        true = 1
        q0oA = self.ids.q0o0
        q0oB = self.ids.q0o1
        q0oC = self.ids.q0o2

        animate_red = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_green = Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=0.001)
        animate_same = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)
        animate_gw = Animation(
                background_color=(123/255, 8/255, 1/255, 1),
                duration=0.001)

        animate_red += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_green += Animation(
                background_color=(156/255, 178/255, 214/255, 1),
                duration=3)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        animate_gw += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=3)
        
        animate_red += Animation(
                background_color=(1,0,0,1), 
                duration=0.001)
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
        animate_same += Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=0.001)
       
        animate_green += Animation(
                background_color=(0,1,0,1), 
                duration=2.5)
        animate_gw+= Animation(
                background_color=(0,1,0,1), 
                duration=2.5)

        animate_green += Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)
        animate_gw+= Animation(
                background_color=(0.8,0.1,0.2,0.9), 
                duration=0.001)

        animate_caza = Animation(
                background_color=(123/255, 8/255, 1/255, 1), 
                duration=8.5)
        animate_caza += Animation(
                background_color=(0.8,0.2,0.1,0.9), 
                duration=0.001)

        if ans == 0:
            animate_red.start(q0oA)
            animate_gw.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 1:
            animate_same.start(q0oA)
            animate_green.start(q0oB)
            animate_same.start(q0oC)

        elif ans == 2:
            animate_same.start(q0oA)
            animate_gw.start(q0oB)
            animate_red.start(q0oC)

        p7 = self.ids.p7 
        animate_caza.start(p7)
        
        Clock.schedule_once(lambda dt: self.update(ans, true, user_p, list_ps), 3)    
        self.ids.q0o0.disabled = True
        self.ids.q0o1.disabled = True
        self.ids.q0o2.disabled = True
        self.ids.nex.disabled = False

    def update(self, ans, true, user_p, list_ps):
        
        app = App.get_running_app()
        app.stop_music()   
        app.correct_music()

        user_p = 0
        while list_ps[user_p] == '' or list_ps[user_p] == 'caza':
            user_p += 1

        if ans == true:
            user_p += 1
            if user_p == 8:
                self.ids.p8.disabled = False
                self.ids.p8.text = 'FIN'
            i = 0
            while list_ps[i] == '' or list_ps[i] == 'caza':
                i += 1
            else:
                list_ps[i+1] = list_ps[i]
                list_ps[i] = ''
        
        if ans != true:
            app = App.get_running_app()
            app.open_popup()

        self.ids.p1.text = list_ps[1]
        self.ids.p2.text = list_ps[2]
        self.ids.p3.text = list_ps[3]
        self.ids.p4.text = list_ps[4]
        self.ids.p5.text = list_ps[5]
        self.ids.p6.text = list_ps[6]
        self.ids.p7.text = list_ps[7]
        
        caza_p = 7
        if user_p == caza_p:
            app = App.get_running_app()
            app.game_over_popup()
            app.stop()

class Victoria(Screen):

    def on_enter(self):
        app = App.get_running_app()
        app.stop_music()   
        app.start_initial_music()

    def close_app(self):
        app = App.get_running_app()
        app.stop()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('new_window.kv')

class Cazador(App):
    initial_music = None
    new_music = None
    cazadora_music = None
    correct_music = None
    wrong_music = None
    final_music = None

    def build(self):

        self.portada = Portada(name='portada')
        self.ronda1q0 = Ronda1Q0(name='ronda1q0')
        self.ronda2cazadora= Ronda2Cazadora(name='ronda2cazadora')

        money = 0
        with open('money.json', 'w') as f:
            json.dump(money, f)

        if platform == 'android' or platform == 'ios':
            Window.maximize()
        else:
            Window.maximize()

        return kv

    def on_start(self):
        self.start_initial_music()  # Start initial music when the app starts

    def start_initial_music(self):
        self.initial_music = SoundLoader.load('music.mp3')
        if self.initial_music:
            self.initial_music.loop = True
            self.initial_music.play()

    def stop_music(self):
        if self.initial_music:
            self.initial_music.stop()
        if self.new_music:
            self.new_music.stop()
        if self.cazadora_music:
            self.new_music.stop()

    def start_new_music(self):
        self.new_music = SoundLoader.load('ronda1.mp3')
        if self.new_music:
            self.new_music.loop = True
            self.new_music.play()

    def final_music(self):
        self.new_music = SoundLoader.load('final.mp3')
        if self.new_music:
            self.new_music.loop = True
            self.new_music.play()

    def start_cazadora_music(self):
        self.new_music = SoundLoader.load('cazadora.mp3')
        if self.new_music:
            self.new_music.loop = False
            self.new_music.play()

    def correct_music(self):
        self.new_music = SoundLoader.load('correct.mp3')
        if self.new_music:
            self.new_music.play()

    def wrong_music(self):
        self.new_music = SoundLoader.load('correct.mp3')
        if self.new_music:
            self.new_music.play()

    def open_popup(self):
        popup = MyPopup()  
        popup.open()

    def open_popup_2(self):
        popup = MyPopup_2()  
        popup.open()

    def open_popup_3(self):
        popup = MyPopup_3()  
        popup.open()

    def game_over_popup(self):
        popup = GameOverPopup()  
        popup.open()

if __name__ == '__main__':
    Cazador().run()
