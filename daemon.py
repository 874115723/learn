#!/usr/bin/python

#encoding:utf-8

import os

FileList=[]
Suffix = ".txt"
target = "liyi"

def ScanFile(Dir):
    if os.path.isdir(Dir):
      items=os.listdir(Dir)
      for names in items:
        if os.path.isfile(Dir+'/'+names) and names.endswith(Suffix):
          if names.split('/')[-1].find(target) != -1:
              FileList.append(Dir+'/'+names)
        else:
          if os.path.isdir(Dir+'/'+names):
            #print Dir+'/'+names
            ScanFile(Dir+'/'+names)

DIRNAME="/home"

ScanFile(DIRNAME)

if len(FileList)!=0:

  print(FileList)

else:

  print("txt file that filename contains liyi is not exist!")