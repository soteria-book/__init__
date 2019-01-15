#!/usr/bin/env bash 

start=$( cd `dirname $0` && pwd	 )
echo "test"
echo $start
echo "again"


http https://raw.githubusercontent.com/soteria-book/publication/master/repositories.txt | while read l ; do

	d=$( echo $l | cut -f5 -d\/ | cut -f1 -d\.  ) 
	echo "Processing $d"  
	dir_to_create=${start}/$d
  	
	if [[ -e  $dir_to_create ]] ; then 
		echo "WARN: ${dir_to_create} aleady exists." 
	else  	
		echo "initializing ${dir_to_create}"  
		git_repo=git@github.com:soteria-book/${d}.git
		git clone ${git_repo} ${dir_to_create}
	fi
done 

cd ${start}

#git clone git@github.com:soteria-book/soteria-book.git ${start}/book 
#subl ${start} 

