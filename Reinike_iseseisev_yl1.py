#Tauri Reinike

'''
import pygame #Impordib pygame

pygame.init() #pygame käivitatakse
#Siin ei tekinud ühtegi viga
screen=pygame.display.set_mode([640,480])#See rida loob pygame akna.
pygame.display.set_caption("My screen") #See rida uuendab akent, mis loodi eelmises reas.
'''

'''
import pygame #Impordib pygame
pygame.init() #Pygame käivitatakse

screen=pygame.display.set_mode([640,480],pygame.RESIZABLE)#Sellel real luuakse 640 * 480 suurusega aken, mida saab akent lohistades muuta suuremaks ja väiksemaks
pygame.display.set_caption("My Screen") #Paneb ekraanile pealkirja
'''
'''
import pygame #Impordib pygame
pygame.init() #pygame käivitatakse
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Myscreen") #Paneb ekraanile pealkirja
screen.fill([204,255,255]) #Muudab ekraani taustavärvi
pygame.display.flip() #Ekraani uuendatakse sellel real.
'''

import pygame #Impordib pygame
pygame.init()#Käivitab pygame

#ekraani seaded
screen=pygame.display.set_mode([640,480])#Loob uue ekraani
pygame.display.set_caption("My screen")#Annab ekraanile pealkirja
screen.fill([204,255,255]) #Täitab ekraani helesinise värviga

#Joonistamine

#pygame.draw.line(screen, [255,0,0], [100,100], [200,200],2) #Se rida joonistab sirge joone
#pygame.draw.rect(screen, [0,255,0], [50,80, 200,300], 2) #See rida joonistab ristküliku
#pygame.draw.circle(screen, [0,0,255], [150,200], 100, 1) #See rida joonistab sinise ringi
#pygame.draw.polygon(screen, [255, 0, 255], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2) #See rida joonistab hulknurga
#pygame.draw.ellipse(screen, [0,255,0], [50,80,200,300],2)#See rida joonistab ovaali
pygame.draw.arc(screen,[0,0,0], [100,100,250,200], 0, 3.14*1.5, 1) #See rida joonistab kaare

pygame.display.flip()#See rida uuendab ekraani.






#Alumine osa ei lase Pygame ekraanil ise kinni minna.
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()