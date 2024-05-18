cd ../c3Geo
./uniqueSTL.X
cp total.fms ../c3
cd ../c3
cartesianMesh
transformPoints -scale 1e-3
decomposePar -force
mpirun -np 3 simpleFoam -parallel > log.simpleFoam && tail -f log.simpleFoam
