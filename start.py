#!/usr/bin/env python
import os,sys,time,re , urllib 


def dt ():
	from datetime import datetime
	from dateutil.tz import tzutc
	dt_2020 = datetime(2020, 9, 13, 12, 26, 40, tzinfo=tzutc())
	dt_1970 = datetime(1970, 1, 1, 0, 0, 0, tzinfo=tzutc())
	return int((dt_2020 - dt_1970).total_seconds())

parent  = sys.argv[0]



repos = urllib.urlopen('https://raw.githubusercontent.com/soteria-book/publication/master/repositories.txt?q=%s' % dt()  )
lines = [ l.strip() for l in   repos.readlines() ]

for l in lines : 
	d = l.split('/')[-1]
	d = d .split(  '''.''')[0]
	new_url = 'git@github.com:soteria-book/%s.git' % (d  ) 
	cmd = 'git clone %s %s ' % (  new_url ,   os.path.join( parent, d ))
	os.system(cmd)


os.system('git clone git@github.com:soteria-book/soteria-book.git %s  '  % os.path.join (parent, 'book')  )



