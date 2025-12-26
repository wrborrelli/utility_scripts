#!/u/local/apps/mathematica/13.1/Executables/wolframscript -script
(* ::Package:: *)

(* ./xyzToWater.wsl xyz_file.xyz file_name_comment box_length  *)

(* ::Input::Initialization:: *)
ff[x_]:=If[
#[[2]]<0,
ToString[NumberForm[#[[1]],{8,8}]]<>"D-"<>StringPadLeft[ToString[Abs[#[[2]]]],2,"0"]
,
ToString[NumberForm[#[[1]],{8,8}]]<>"D+"<>StringPadLeft[ToString[Abs[#[[2]]]],2,"0"]
]&@MantissaExponent[x]


(* ::Input::Initialization:: *)
spaceff[x_]:=If[x<0,""<>ToString[ff[x]]," "<>ToString[ff[x]]]


(* ::Input::Initialization:: *)
writeIns[ts_,path_,identifier_,boxL_]:=Module[{watHead={"==================================================","  [] WATER-SODIDE ADIABATIC MD SIMULATION","==================================================","","  <> DATE::  Tue Dec  6 15:47:03 2022","","  480860     499  0.24644646D+02  0.50000000D+00  0.24043000D+06  0.00000000D+00  4  0.00000000D+00  0.00000000D+00  0.00000000D+00  0.00000000D+00  0.00000000D+00  0.00000000D+00  0.00000000D+00  0.00000000D+00  0.00000000D+00  0.00000000D+00  0.00000000D+00  0.00000000D+00",""},dat,mms,oxs,oys,ozs,h1xs,h1ys,h1zs,h2xs,h2ys,h2zs,flat,pos,file,vels,unitl=boxL/2},
dat=ToExpression[StringSplit[StringReplace[ts,{"e"->"*10^","D"->"*10^"}]][[3;;]][[All,2;;]]];
(* recenter about origin on symmetric interval of boxL *)
(*dat=Transpose[ToExpression[Transpose[dat]]+Map[SetPrecision[unitl,2]-#&,Map[Max,ToExpression[Transpose[dat]]]]];*)
dat=Flatten[Map[miWat[#,boxL]&,Partition[dat,3]],1];
dat=Flatten[Map[miWat[#,boxL]&,Partition[dat,3]],1];
dat=Flatten[Map[miWat[#,boxL]&,Partition[dat,3]],1];
(* process *)
{oxs,oys,ozs}=Transpose[dat[[1;;-3;;3]]];
{h1xs,h1ys,h1zs}=Transpose[dat[[2;;-2;;3]]];
{h2xs,h2ys,h2zs}=Transpose[dat[[3;;-1;;3]]];
vels=Partition[Table[" 0.00000000D+00",Length[oxs]*3*3],3];
flat=(ToExpression[Flatten[{oxs,h1xs,h2xs,oys,h1ys,h2ys,ozs,h1zs,h2zs}]]/unitl);
pos=Partition[Map[spaceff,flat],3];
file=OpenWrite[path<>"in.water"<>identifier];
Map[WriteLine[file,#]&,watHead];
Map[WriteLine[file,StringReplace[StringDelete[ToString[#],{"}",","}],"{"->" "]]&,pos];
WriteLine[file,""];
Map[WriteLine[file,StringReplace[StringDelete[ToString[#],{"}",","}],"{"->" "]]&,vels];
Close[file];
]


(* ::Input::Initialization:: *)
mi[x_,bl_]:=Table[Which[x[[i]]<-bl*0.5,x[[i]]+bl,x[[i]]>=bl*0.5,x[[i]]-bl,True,x[[i]]],{i,1,3}]


(* ::Input::Initialization:: *)
miWat[wat_,bl_]:=Transpose[Table[
Which[
wat[[1]][[i]]<-bl*0.5,
Table[wat[[j]][[i]]+bl,{j,1,3}],
wat[[1]][[i]]>=bl*0.5,
Table[wat[[j]][[i]]-bl,{j,1,3}],
True,
Table[wat[[j]][[i]],{j,1,3}]
]
,{i,1,3}]]

xyz = ReadList[$ScriptCommandLine[[2]], "String"];
dir = Directory[]<>"/";

writeIns[xyz, dir, $ScriptCommandLine[[3]], ToExpression[$ScriptCommandLine[[4]]]];

