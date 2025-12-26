#loads a trajectory, then calcualtes and writes out a RDF
# Jennie Thomas -  October 2006
#does not write the integrated values correctly

mol addfile tb_10fs.xyz type xyz waitfor all

pbc set {24.6446459431854, 24.6446459431854, 24.6446459431854} -all

#set up the atom selections
set sel1 [atomselect top "name com"]
set sel2 [atomselect top "name O"]

set n_frames [molinfo top get numframes]

set ngr [ expr $n_frames - 1 ]

set gr [measure gofr $sel1 $sel2 delta .1 rmax 12 usepbc 1 selupdate 1 first 0 last $ngr step 1]
set outfile [open tb_eo_gr.dat w]
set r [lindex $gr 0]
set gr2 [lindex $gr 1]
set igr [lindex $gr 2]
set i 0
foreach j $r k $gr2 l $igr {
    puts $outfile "$j $k $l"
    }

#calculate g(r)
#set gr [measure gofr $sel1 $sel2 delta .1 rmax 6 usepbc 1 selupdate 1 first 1 last 1 step 1]

#set up the outfile and write out the data
#set outfile [open gofr.dat w]

#set r [lindex $gr 0]
#set gr2 [lindex $gr 1]
#set igr [lindex $gr 2]

#set i 0
#foreach j $r k $gr2 l $igr {
#   puts $outfile "$j $k $l"
#}

#close $outfile
exit vmd
exit
