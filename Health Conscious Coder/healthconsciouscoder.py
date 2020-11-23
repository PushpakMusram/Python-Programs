#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pygame

def Music(Dj):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(Dj)
    pygame.mixer.music.play()
    
    
    
def IsThisOfficeTime(current_time):
    if current_time>'09:00:00' and current_time<'17:00:00':
        return True
    else:
        return False

#Initialisations
DrinkWaterAfterEvery = 1200  #in sec [20 Min]   
DoEyesExersiseAfterEvery = 1800 #in sec [30min] 
DoPhysicalExerciseAfterEvery = 2700 #in sec [45 min]

current_time = time.strftime('%H:%M:%S')
WaterAT = time.time()
EyesAT = time.time()
ExerciserAT = time.time()
    
    
NumberOfWaterTrials = 18        
WaterDrink = 'Water.ogg'
EyesExercise = 'eyes.ogg'
BodyExercise = 'Exercise.ogg'

SleepTime=20

while (IsThisOfficeTime(current_time)):
    if NumberOfWaterTrials > 0:
        if (time.time() - WaterAT) > DrinkWaterAfterEvery :
            print("Bhaii please Paani pilo bhaii...Please Bhaii")
            
            while True:
                Music(WaterDrink)
                
                if input("Enter Done if you had water: ").lower() =="done":
                        WaterAT = time.time()
                        break 
        
        
        if (time.time() - EyesAT) > EyeExerciseAfterEvery:
            print("Bhaii please Eyes ki Exercise krlo bhaii...Please Bhaii")
            
            while True:
                Music(EyesExercise)
                
                if input("Enter Done if you had exercised eyes: ").lower() =="done":
                        EyesAT = time.time()
                        
                        break                  
            
        
        
        if (time.time() - ExerciserAT) > DoPhysicalExerciseAfterEvery :
            print("Bhaii please Exersise krlo bhaii...Please Bhaii")
            
            while True:
                Music(BodyExercise)
                
                if input("Enter Done if you had Exercised: ").lower() =="done":
                        ExerciserAT = time.time()
                        
                        break 
                        
                        
    time.sleep(SleepTime)
    current_time = time.strftime('%H:%M:%S')
                        

