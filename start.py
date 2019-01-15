#!/usr/bin/env python
import os,sys,time,re , urllib 

curr_dir = sys.argv[0]
abs_path =  os.path.abspath(curr_dir)
parent, fn = os.path.split (  abs_path )  

repos = urllib.urlopen('https://raw.githubusercontent.com/soteria-book/publication/master/repositories.txt' )
lines = [ l.strip() for l in   repos.readlines() ]

for l in lines : 
	d = l.split('/')[-1]
	d = d .split(  '''.''')[0]
	new_url = 'git@github.com:soteria-book/%s.git' % (d  ) 
	cmd = 'git clone %s %s ' % (  new_url ,   os.path.join( parent, d ))
	os.system(cmd)


os.system('git clone git@github.com:soteria-book/soteria-book.git %s  '  % os.path.join (parent, 'book')  )



