#!/bin/bash

#-----Nom de la machine----
hostname >> ressondee1.txt


#--------------------------------------Cpu utilisé-----------------------------------------------
grep 'cpu' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage "%"}' >> ressondee1
.txt

#------------------Nombre users connecte--------------------
who -q | cut -d: -f2 | tail -1 | sed 's/ //g' >> ressondee1.txt

#--------Nombre process-------
ps -elf | wc -l >> ressondee1.txt

#-----------------------------MémoireTotal------------------------------
grep MemTotal /proc/meminfo | cut -d: -f2 | sed 's/kB//'g >> ressondee1.txt

#-----------------------------MémoireLibre-----------------------------
grep MemFree /proc/meminfo | cut -d: -f2 | sed 's/kB//'g >> ressondee1.txt

#-----------------------------DiskTotal----------------------------------------------
df -h | grep '/dev/sda1' | cut -d"G" -f1 | cut -c10-100 | sed 's/ //g' >> ressondee1.txt

#------------------------DiskLibre---------------------
df -h | grep '/dev/sda1' | cut -d"G" -f3 >> ressondee1.txt

#-------------------------DiskUtilise-------------------------------------------------
df -h | grep '/dev/sda1' | cut -d"G" -f4 | sed 's/%//g' | cut -d"/" -f1 >> ressondee1.txt

#---------------------------SwapTotal------------------------------------
grep SwapTotal /proc/meminfo | cut -d: -f2 | sed 's/kB//g' >> ressondee1.txt

#---------------------------SwapLibre------------------------------------
grep SwapLibre /proc/meminfo | cut -d: -f2 | sed 's/kB//g' >> ressondee1.txt

#------------Date--------------
date +"%Y-%m-%d" >> ressondee1.txt

#------------Heure-------------
date +"%k:%M:%S" >> ressondee1.txt
