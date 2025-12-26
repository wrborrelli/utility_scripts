#!/u/local/apps/mathematica/13.1/Executables/wolframscript -script
(* ::Package:: *)

miWat[wat_, bl_ : 15.66] := Transpose[Table[
Which[
wat[[1]][[i]] < -bl*0.5,
Table[wat[[j]][[i]] + bl, {j, 1, 3}],
wat[[1]][[i]] >= bl*0.5,
Table[wat[[j]][[i]] - bl, {j, 1, 3}],
True,
Table[wat[[j]][[i]], {j, 1, 3}]
]
, {i, 1, 3}]]

dat = Map[StringSplit, ReadList[$ScriptCommandLine[[2]], "String"]];
blength = ToExpression[$ScriptCommandLine[[3]]];
dir = Directory[]<>"/";
head = dat[[1;;2]];
tdat = dat[[3 ;;]];
atomLabs = tdat[[All, 1]];
com = ToExpression[tdat[[-1]][[2 ;;]]];
fdat = Map[# - com&,ToExpression[tdat[[All, 2;;]]]];
el = fdat[[-1]];
fdatWats = Partition[fdat[[1;;-2]], 3];
fdatWats = Map[miWat[#, blength]&, fdatWats];
fdatWats = Flatten[fdatWats, 1];
fdatWats = Join[fdatWats, el];
finalDat = Map[StringDelete[ToString[#], {",", "{", "}"}] &,Join[head, Map[Flatten, Thread[{atomLabs, fdat}]]]];
f = OpenWrite[dir<>"out_center.xyz"];
Map[WriteLine[f, #]&, finalDat];
Close[f];

