
%	input  @1 [ [2,5,42], [6,6] , [1,2,3,4,4,5] ]     @2  [ 49, 12, 19]

sumVecOP( [], 0).
sumVecOP( [ Head|Tail] , X ):- sumVecOP(Tail, Y), X is Y+Head .

checkLenVecsOP( [], [] ).
checkLenVecsOP( [HeadVec|TailVec] , [HeadLen|TailLen] ):- sumVecOP( HeadVec , HeadLen), checkLenVecsOP( TailVec, TailLen).