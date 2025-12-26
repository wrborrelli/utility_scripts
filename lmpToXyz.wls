#!/u/local/apps/mathematica/13.1/Executables/wolframscript -script
(* ::Package:: *)

com = $ScriptCommandLine[[3]]

dat = ReadList[$ScriptCommandLine[[2]], "String"];
symbs = Flatten[Table[{"O", "H", "H"}, 216]];

df = Map[StringDelete[ToString[#], {",", "{", "}"}] &, Flatten[{#[[1 ;; 2]], Flatten /@ Thread[{symbs, #[[3 ;;]][[All, 2 ;;]]}]} &@Map[StringSplit, dat], 1]]

f = OpenWrite["form_"<>ToString[com]<>".xyz"];
Map[WriteLine[f,#]&,df];
Close[f];

