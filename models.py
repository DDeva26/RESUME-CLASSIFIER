'''
Created on 01-Apr-2019

@author: Ashokkumar.Rayapati
'''
from django.db import models

class uploadfolder(models.Model):
    """ my application """
    File_to_upload = models.FileField(upload_to='')