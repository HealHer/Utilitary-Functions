#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 

def os_mkdir(name, folder) : 
  # Creation d'un dossier sur le <folder> parent
  path_folder = "%s/%s" % (folder, name)
  if name not in os.listdir(folder) : 
    os.mkdir(path_folder)
    
  # Retour pour les besoin de confirmation ou non 
  return os.path.isdir(path_folder)
     
