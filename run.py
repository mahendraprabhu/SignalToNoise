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
               if 'Image' in i:
                   break
               print (i)
               f.write('\t<li>\n')
               f.write('\t\t<a href="#">\n')
               f.write('\t\t<p>'+i[:-1]+'</p>\n')
               f.write('\t\t</a>')
               f.write('\t</li>\n')
           f.write('</ul>\n')  
           f.write('<h1> Images </h1>\n')
           f.write('<p>The following images were taken from <a href="http://sweetpublishing.com">http://sweetpublishing.com </a></p>\n')

           for i in txt:
               if 'Image' in i:

                   a = i.split(',')
                   print (a)
                   ImageString = '\t<img alt="'+a[1]+'" src='+a[2][:-1]+' height="500"> '
                   print (ImageString)
                   f.write('<div class="gallery">\n')
#                   f.write('<a target="_blank" href="fjords.jpg">\n')
                   f.write('\t<a target="_blank" href='+a[2][:-1]+'>\n')
                   f.write('\t\t'+ImageString+'\n')
                   f.write('\t</a>\n')
                   f.write('<div class="desc">')
                   f.write(a[1])
                   f.write('</div>\n')                   
                   f.write('</div>\n\n')
#                   f.write(ImageString)
#           f.write('<a href="http://sweetpublishing.com"> http://sweetpublishing.com </a>')
           f.write('</body>')
