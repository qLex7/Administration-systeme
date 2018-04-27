#!/usr/bin/python
# -*-coding: Latin-1 -*-
import subprocess as sp
import time


def sonde3():
        data=list()

        #------------------Nom machine------------------------
        p=sp.Popen(["hostname"],stdout=sp.PIPE, stdin=sp.PIPE)
        data.append(p.stdout.readline())
	

        #--------------------------------CPU utilise--------------------------------------------
        cmd= "top -b -n1 | grep 'Cpu' | cut -d' ' -f11 | sed 's/,/./g'"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        CpuDispo=float(p.stdout.readline())
        CpuUse=100-float(CpuDispo)
        data.append("%.2f" % CpuUse)


        #-------------------------------MemTotal------------------------------------ 
        cmd="grep MemTotal /proc/meminfo | cut -d: -f2 | sed 's/kB//'g"	
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        MemTot=p.stdout.readline()
        #-----------------------------MemFree------------------------------------------- 
        cmd="grep MemFree /proc/meminfo | cut -d: -f2 | sed 's/kB//'g"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        MemDispo=p.stdout.readline()

        #------------------RamUse----------------
        MemFree=float(MemDispo)/float(MemTot)*100
        MemUse=100-MemFree
        data.append("%.2f" % MemUse)


        #-------------------------Swap Total---------------------------- 
        cmd="grep SwapTotal /proc/meminfo | cut -d: -f2 | sed 's/kB//g' | sed 's/ //g'"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        SwapTot=p.stdout.readline()
        #---------------------------Swap Libre--------------------------
        cmd="grep SwapFree /proc/meminfo | cut -d: -f2 | sed 's/kB//g' | sed 's/ //g'"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        SwapDispo=p.stdout.readline()

        #-------------------SwapUse(%)--------------
        SwapFree=float(SwapDispo)/float(SwapTot)*100
        SwapUse=100-SwapFree
        data.append("%.2f" % SwapUse)


        #---------------Utilisation du Disque en %-------------------
        cmd= "df $PWD | awk '/[0-9]%/{print $(NF-1)}' | sed 's/%//g'"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        data.append(p.stdout.readline())

        #--------------Nombre de user connecté-------------
        cmd="who -q | cut -d: -f2 | tail -1 | sed 's/ //g'"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        data.append(p.stdout.readline())

        #-----------------Nombre processus---------------------
        cmd="ps -elf | wc -l"
        p = sp.Popen(cmd,stdout=sp.PIPE,stderr=None,shell=True)
        data.append(p.stdout.readline())

        #--------------------------Date-----------------------------------------
        p=sp.Popen(["date", "+%Y-%m-%d:%H:%M:%S"],stdout=sp.PIPE, stdin=sp.PIPE)
        data.append(p.stdout.readline())

        #--------------------------Heure------------------------
        p=sp.Popen(["date","+%H"],stdout=sp.PIPE, stdin=sp.PIPE)
        data.append(p.stdout.readline())


        mon_fichier = open("ressondee1.txt","w")
        for item in data:
                mon_fichier.write("%s\n" % item)

        mon_fichier.close