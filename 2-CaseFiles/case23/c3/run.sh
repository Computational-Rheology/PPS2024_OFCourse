cd ../c3Geo
./uniqueSTL.X
cp total.fms ../c3
cd ../c3
cartesianMesh
transformPoints -scale 1e-3
simpleFoam
