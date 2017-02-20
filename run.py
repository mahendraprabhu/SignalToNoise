# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:59:48 2017

@author: mramacha
"""

import os
import glob
import shutil

InputDir = r'C:\Users\mramacha\Documents\Python\My Scripts\SignalToNoise\input'
OutputDir = r'C:\Users\mramacha\Documents\Python\My Scripts\SignalToNoise\output'
TemplateDir = r'C:\Users\mramacha\Documents\Python\My Scripts\SignalToNoise\templates'

#shutil.copy( os.path.join(TemplateDir,'template.html'),OutputDir)
os.chdir(InputDir)
FileNames = glob.glob('*.txt')
print (FileNames)

for fname in FileNames:
    OutputFileName = fname[:-4] + '.html'
    shutil.copy(os.path.join(TemplateDir,'template.html'),
                os.path.join(OutputDir,OutputFileName))
    with open(fname, 'r') as f1:
        txt = f1.readlines()
        with open(os.path.join(OutputDir,OutputFileName),'a') as f:
           f.write('<ul>\n')
           for i in txt:
               print (i)
               f.write('\t<li>\n')
               f.write('\t\t<a href="#">\n')
               f.write('\t\t<p>'+i[:-1]+'</p>\n')
               f.write('\t\t</a>')
               f.write('\t</li>\n')
           f.write('</ul>\n')    
           f.write('</body>')