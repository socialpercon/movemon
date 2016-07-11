NAME="shutter"
check=`ps axf | grep ${NAME} | grep -v grep | awk '{print $1 }'`
if test -z "${check}"; then
	echo "${NAME} is stopped"
	state=0
else
	echo "${NAME} is running"
	state=1
fi
