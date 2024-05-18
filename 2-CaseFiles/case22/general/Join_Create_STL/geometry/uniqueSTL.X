# changest the stl to give the name as for the OF patch,
# then produces an unique file for the grid production

files="FilesToJoin/"

for N in `cat mylist`; do
	cat ${files}${N}.stl | sed -e '1d;$d' > ${N}_.tmp
	echo "solid ${N}" >> ${N}_1.stl
	cat ${N}_.tmp >> ${N}_1.stl
	echo "endsolid ${N}" >> ${N}_1.stl
        touch total.stl
        surfaceAdd ${N}_1.stl total.stl total.stl
	rm ${N}_.tmp
done

surfaceFeatureEdges total.stl total.fms

printf " Use the following command to move all undesired files to the trashcan \n"
printf "\n \n"

printf "gvfs-trash /home/pc/Desktop/joinSTLfiles/!(FilesToJoin|'clear.sh'|'JoinStlFiles.py'|'uniqueSTL.X'|'total.stl')"

printf "\n \n"
