#!/usr/bin/env python3

#import modules
import shutil
import os

#starting directory
os.chdir('/home/student/mycode/')

#move file to folder
shutil.move('raynor.obj', 'ceph_storage/')

#prompt user for new name of file
xname = input('What is the new name for kerrigan.obj? ')

#remane mfile
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


