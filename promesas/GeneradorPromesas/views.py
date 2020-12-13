from django.shortcuts import render
from docx import Document
from docxtpl import DocxTemplate
from django.http import HttpResponse
from GeneradorPromesas.forms import formularioPromesas
import io 



def Convert(string): 
    list1=[] 
    list1[:]=string 
    return list1 


def numeros_letras(valorCadena):
     
    letras = ""
    letras2 = ""
    letras3= ""
    print("largo de la cadena", len(valorCadena))
    
    
    
    
    
    
    if len(valorCadena)==1:
        letras=""
        letras3=""
        if valorCadena[0]=='1':
            letras2="un"
        elif valorCadena[0]=='2':
            letras2="dos"
        elif valorCadena[0]=='3':
            letras2="tres"    
        elif valorCadena[0]=='4':
            letras2="cuatro"
        elif valorCadena[0]=='5':
            letras2="cinco"
        elif valorCadena[0]=='6':
            letras2="séis"
        elif valorCadena[0]=='7':
            letras2="siete"
        elif valorCadena[0]=='8':
            letras2="ocho"
        elif valorCadena[0]=='9':
            letras2="nueve"
            
#---------------------------------------------------------------------------------dos digitos-----------------------------------------  
    
    elif len(valorCadena)==2:
        letras =""
        letras3 =""

        
                
            #--------------------------------------------------------------------------------------10-----------------------------------------------------------------                
        if valorCadena[0]=='1' and valorCadena[1]=='0':
                letras2 ="diez"
                
        elif valorCadena[0]=='1' and valorCadena[1]=='1':
                letras2 ="once"
                
        elif valorCadena[0]=='1' and valorCadena[1]=='2':
                letras2 = "doce"
                
        elif valorCadena[0]=='1' and valorCadena[1]=='3':
                letras2 ="trece"
                
        elif valorCadena[0]=='1' and valorCadena[1]=='4':
                letras2 = "catorce"
                
        elif valorCadena[0]=='1' and valorCadena[1]=='5':
                letras2 ="quince"
                
        elif valorCadena[0]=='1' and valorCadena[1]=='6':
                letras2 = "dieciséis"
                
        elif valorCadena[0]=='1' and valorCadena[1]=='7':
                letras2 ="diecisiete"
                
        elif valorCadena[0]=='1' and valorCadena[1]=='8':
                letras2 = "dieciocho"
                  
        elif valorCadena[0]=='1' and valorCadena[1]=='9':
                letras2 = "diecinueve"
                                
        
        
#--------------------------------------------------------------------------20----------------------------------------------------
        
        elif valorCadena[0]=='2' and valorCadena[1]=='0':
                    letras2 ="veinte"
                    letras3 =""
        elif valorCadena[0]=='2' and valorCadena[1]=='1':
                    letras2 = "veintiún"
                    letras3 =""
        elif valorCadena[0]=='2' and valorCadena[1]=='2':
                    letras2 = "veintidós"
                    letras3 =""
        elif valorCadena[0]=='2' and valorCadena[1]=='3':
                    letras2 ="veintitrés"
                    letras3 =""
        elif valorCadena[0]=='2' and valorCadena[1]=='4':
                    letras2 = "veinticuatro"
                    letras3 =""
        elif valorCadena[0]=='2' and valorCadena[1]=='5':
                    letras2 = "veinticinco"
                    letras3 =""
        elif valorCadena[0]=='2' and valorCadena[1]=='6':
                    letras2 = "veintiséis"
                    letras3 =""
        elif valorCadena[0]=='2' and valorCadena[1]=='7':
                    letras2 = "veintisiete"
                    letras3 =""
        elif valorCadena[0]=='2' and valorCadena[1]=='8':
                    letras2 = "veintiocho"
                    letras3 =""
        elif valorCadena[0]=='2' and valorCadena[1]=='9':
                    letras2 = "veintinueve"
                    letras3 =""
#-------------------------------------------------------------------------------otro metodo 30------------------------------------------------------
        elif valorCadena[0]=='3':
            letras2="treinta"
            if valorCadena[1]=='1':
                letras3="y un"
            elif valorCadena[1]=='2':
                letras3="y dos"
            elif valorCadena[1]=='3':
                letras3="y tres"
            elif valorCadena[1]=='4':
                letras3="y cuatro"
            elif valorCadena[1]=='5':
                letras3="y cinco"
            elif valorCadena[1]=='6':
                letras3="y seis"
            elif valorCadena[1]=='7':
                letras3="y siete"
            elif valorCadena[1]=='8':
                letras3="y ocho"
            elif valorCadena[1]=='9':
                letras3="y nueve"  
#----------------------------------------------------------------------------------------40----------------------------------------------------------            
        elif valorCadena[0]=='4':
            letras2 = "cuarenta"
            if valorCadena[1]=='1':
                letras3="y un"
            elif valorCadena[1]=='2':
                letras3="y dos"
            elif valorCadena[1]=='3':
                letras3="y tres"
            elif valorCadena[1]=='4':
                letras3="y cuatro"
            elif valorCadena[1]=='5':
                letras3="y cinco"
            elif valorCadena[1]=='6':
                letras3="y seis"
            elif valorCadena[1]=='7':
                letras3="y siete"
            elif valorCadena[1]=='8':
                letras3="y ocho"
            elif valorCadena[1]=='9':
                letras3="y nueve"  
        
#------------------------------------------------------------------------------------------50-------------------------------------------------------------
        elif valorCadena[0]=='5':
            letras2 = "cincuenta"
            if valorCadena[1]=='1':
                letras3="y un"
            elif valorCadena[1]=='2':
                letras3="y dos"
            elif valorCadena[1]=='3':
                letras3="y tres"
            elif valorCadena[1]=='4':
                letras3="y cuatro"
            elif valorCadena[1]=='5':
                letras3="y cinco"
            elif valorCadena[1]=='6':
                letras3="y seis"
            elif valorCadena[1]=='7':
                letras3="y siete"
            elif valorCadena[1]=='8':
                letras3="y ocho"
            elif valorCadena[1]=='9':
                letras3="y nueve"      
        
#-------------------------------------------------------------------------------------------60-------------------------------------------------------------
        elif valorCadena[0]=='6':
            letras2 = "sesenta"
            if valorCadena[1]=='1':
                letras3="y un"
            elif valorCadena[1]=='2':
                letras3="y dos"
            elif valorCadena[1]=='3':
                letras3="y tres"
            elif valorCadena[1]=='4':
                letras3="y cuatro"
            elif valorCadena[1]=='5':
                letras3="y cinco"
            elif valorCadena[1]=='6':
                letras3="y seis"
            elif valorCadena[1]=='7':
                letras3="y siete"
            elif valorCadena[1]=='8':
                letras3="y ocho"
            elif valorCadena[1]=='9':
                letras3="y nueve"  
        
#-------------------------------------------------------------------------------------------70-------------------------------------------------------------
        elif valorCadena[0]=='7':
            letras2 = "setenta"
            if valorCadena[1]=='1':
                letras3="y un"
            elif valorCadena[1]=='2':
                letras3="y dos"
            elif valorCadena[1]=='3':
                letras3="y tres"
            elif valorCadena[1]=='4':
                letras3="y cuatro"
            elif valorCadena[1]=='5':
                letras3="y cinco"
            elif valorCadena[1]=='6':
                letras3="y seis"
            elif valorCadena[1]=='7':
                letras3="y siete"
            elif valorCadena[1]=='8':
                letras3="y ocho"
            elif valorCadena[1]=='9':
                letras3="y nueve"      
#-------------------------------------------------------------------------------------------80-------------------------------------------------------------
        elif valorCadena[0]=='8':
            letras2 = "ochenta"
            if valorCadena[1]=='1':
                letras3="y un"
            elif valorCadena[1]=='2':
                letras3="y dos"
            elif valorCadena[1]=='3':
                letras3="y tres"
            elif valorCadena[1]=='4':
                letras3="y cuatro"
            elif valorCadena[1]=='5':
                letras3="y cinco"
            elif valorCadena[1]=='6':
                letras3="y seis"
            elif valorCadena[1]=='7':
                letras3="y siete"
            elif valorCadena[1]=='8':
                letras3="y ocho"
            elif valorCadena[1]=='9':
                letras3="y nueve"               
#-------------------------------------------------------------------------------------------90-------------------------------------------------------------
        elif valorCadena[0]=='9':
            letras2 = "noventa"
            if valorCadena[1]=='1':
                letras3="y un"
            elif valorCadena[1]=='2':
                letras3="y dos"
            elif valorCadena[1]=='3':
                letras3="y tres"
            elif valorCadena[1]=='4':
                letras3="y cuatro"
            elif valorCadena[1]=='5':
                letras3="y cinco"
            elif valorCadena[1]=='6':
                letras3="y seis"
            elif valorCadena[1]=='7':
                letras3="y siete"
            elif valorCadena[1]=='8':
                letras3="y ocho"
            elif valorCadena[1]=='9':
                letras3="y nueve"    
#-----------------------------------------------------------------------------------------cientos-------------------------------------------
    
    elif len(valorCadena) == 3:
               
#----------------------------------------------------------------------------------------------000------------------------------------------------------------
        if valorCadena[0] =='0':
            letras = ""
            if valorCadena[1]=='0':
                letras2 = ""
                if valorCadena[2]=='1':
                    letras3="un"
                elif valorCadena[2]=='2':
                    letras3="dos"
                elif valorCadena[2]=='3':
                    letras3="tres"
                elif valorCadena[2]=='4':
                    letras3="cuatro"
                elif valorCadena[2]=='5':
                    letras3="cinco"
                elif valorCadena[2]=='6':
                    letras3="séis"
                elif valorCadena[2]=='7':
                    letras3="siete"
                elif valorCadena[2]=='8':
                    letras3="ocho"
                elif valorCadena[2]=='9':
                    letras3="nueve"
                
            #--------------------------------------------------------------------------------------010-----------------------------------------------------------------                
            if valorCadena[1]=='1' and valorCadena[2]=='0':
                    letras2 ="diez"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='1':
                    letras2 ="once"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='2':
                    letras2 = "doce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='3':
                    letras2 ="trece"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='4':
                    letras2 = "catorce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='5':
                    letras2 ="quince"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='6':
                    letras2 = "dieciséis"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='7':
                    letras2 ="diecisiete"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='8':
                    letras2 = "dieciocho"
                    letras3 =""   
            elif valorCadena[1]=='1' and valorCadena[2]=='9':
                    letras2 = "diecinueve"
                    letras3 =""                
            
            
#--------------------------------------------------------------------------020----------------------------------------------------
            
            elif valorCadena[1]=='2' and valorCadena[2]=='0':
                        letras2 ="veinte"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='1':
                        letras2 = "veintiún"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='2':
                        letras2 = "veintidós"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='3':
                        letras2 ="veintitrés"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='4':
                        letras2 = "veinticuatro"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='5':
                        letras2 = "veinticinco"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='6':
                        letras2 = "veintiséis"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='7':
                        letras2 = "veintisiete"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='8':
                        letras2 = "veintiocho"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='9':
                        letras2 = "veintinueve"
                        letras3 =""
#-------------------------------------------------------------------------------otro metodo 030------------------------------------------------------
            elif valorCadena[1]=='3':
                letras2="treinta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
#----------------------------------------------------------------------------------------040----------------------------------------------------------            
            elif valorCadena[1]=='4':
                letras2 = "cuarenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#------------------------------------------------------------------------------------------050-------------------------------------------------------------
            elif valorCadena[1]=='5':
                letras2 = "cincuenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
            
#-------------------------------------------------------------------------------------------060-------------------------------------------------------------
            elif valorCadena[1]=='6':
                letras2 = "sesenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------070-------------------------------------------------------------
            elif valorCadena[1]=='7':
                letras2 = "setenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
#-------------------------------------------------------------------------------------------080-------------------------------------------------------------
            elif valorCadena[1]=='8':
                letras2 = "ochenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"               
#-------------------------------------------------------------------------------------------090-------------------------------------------------------------
            elif valorCadena[1]=='9':
                letras2 = "noventa"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"
#------------------------------------------------------------------------100-----------------------------------------

        elif valorCadena[0] =='1':
            letras = "ciento"
            if valorCadena[1]=='0':
                letras2 = ""
                if valorCadena[2]=='1':
                    letras3="un"
                elif valorCadena[2]=='2':
                    letras3="dos"
                elif valorCadena[2]=='3':
                    letras3="tres"
                elif valorCadena[2]=='4':
                    letras3="cuatro"
                elif valorCadena[2]=='5':
                    letras3="cinco"
                elif valorCadena[2]=='6':
                    letras3="séis"
                elif valorCadena[2]=='7':
                    letras3="siete"
                elif valorCadena[2]=='8':
                    letras3="ocho"
                elif valorCadena[2]=='9':
                    letras3="nueve"
                
            #--------------------------------------------------------------------------------------110-----------------------------------------------------------------                
            if valorCadena[1]=='1' and valorCadena[2]=='0':
                    letras2 ="diez"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='1':
                    letras2 ="once"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='2':
                    letras2 = "doce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='3':
                    letras2 ="trece"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='4':
                    letras2 = "catorce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='5':
                    letras2 ="quince"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='6':
                    letras2 = "dieciséis"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='7':
                    letras2 ="diecisiete"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='8':
                    letras2 = "dieciocho"
                    letras3 =""   
            elif valorCadena[1]=='1' and valorCadena[2]=='9':
                    letras2 = "diecinueve"
                    letras3 =""                
            
            
#--------------------------------------------------------------------------120----------------------------------------------------
            
            elif valorCadena[1]=='2' and valorCadena[2]=='0':
                        letras2 ="veinte"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='1':
                        letras2 = "veintiún"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='2':
                        letras2 = "veintidós"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='3':
                        letras2 ="veintitrés"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='4':
                        letras2 = "veinticuatro"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='5':
                        letras2 = "veinticinco"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='6':
                        letras2 = "veintiséis"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='7':
                        letras2 = "veintisiete"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='8':
                        letras2 = "veintiocho"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='9':
                        letras2 = "veintinueve"
                        letras3 =""
#-------------------------------------------------------------------------------otro metodo 130------------------------------------------------------
            elif valorCadena[1]=='3':
                letras2="treinta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
#----------------------------------------------------------------------------------------140----------------------------------------------------------            
            elif valorCadena[1]=='4':
                letras2 = "cuarenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#------------------------------------------------------------------------------------------150-------------------------------------------------------------
            elif valorCadena[1]=='5':
                letras2 = "cincuenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
            
#-------------------------------------------------------------------------------------------160-------------------------------------------------------------
            elif valorCadena[1]=='6':
                letras2 = "sesenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------170-------------------------------------------------------------
            elif valorCadena[1]=='7':
                letras2 = "setenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
#-------------------------------------------------------------------------------------------180-------------------------------------------------------------
            elif valorCadena[1]=='8':
                letras2 = "ochenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"               
#-------------------------------------------------------------------------------------------190-------------------------------------------------------------
            elif valorCadena[1]=='9':
                letras2 = "noventa"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
        
        
                
            elif valorCadena[1]=='0' and valorCadena[2]=='0':
                letras = "cien"
            
            
#------------------------------------------------------------------------------------------200-------------------------------------------------
        elif valorCadena[0] =='2':
            letras = "doscientos"
            
            if valorCadena[1]=='0':
                letras2 = ""
                if valorCadena[2]=='1':
                    letras3="un"
                elif valorCadena[2]=='2':
                    letras3="dos"
                elif valorCadena[2]=='3':
                    letras3="tres"
                elif valorCadena[2]=='4':
                    letras3="cuatro"
                elif valorCadena[2]=='5':
                    letras3="cinco"
                elif valorCadena[2]=='6':
                    letras3="séis"
                elif valorCadena[2]=='7':
                    letras3="siete"
                elif valorCadena[2]=='8':
                    letras3="ocho"
                elif valorCadena[2]=='9':
                    letras3="nueve"
                
            #--------------------------------------------------------------------------------------210-----------------------------------------------------------------                
            if valorCadena[1]=='1' and valorCadena[2]=='0':
                    letras2 ="diez"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='1':
                    letras2 ="once"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='2':
                    letras2 = "doce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='3':
                    letras2 ="trece"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='4':
                    letras2 = "catorce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='5':
                    letras2 ="quince"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='6':
                    letras2 = "dieciséis"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='7':
                    letras2 ="diecisiete"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='8':
                    letras2 = "dieciocho"
                    letras3 =""   
            elif valorCadena[1]=='1' and valorCadena[2]=='9':
                    letras2 = "diecinueve"
                    letras3 =""                
            
            
#--------------------------------------------------------------------------220----------------------------------------------------
            
            elif valorCadena[1]=='2' and valorCadena[2]=='0':
                        letras2 ="veinte"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='1':
                        letras2 = "veintiún"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='2':
                        letras2 = "veintidós"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='3':
                        letras2 ="veintitrés"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='4':
                        letras2 = "veinticuatro"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='5':
                        letras2 = "veinticinco"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='6':
                        letras2 = "veintiséis"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='7':
                        letras2 = "veintisiete"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='8':
                        letras2 = "veintiocho"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='9':
                        letras2 = "veintinueve"
                        letras3 =""
#-------------------------------------------------------------------------------otro metodo 230------------------------------------------------------
            elif valorCadena[1]=='3':
                letras2="treinta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
#----------------------------------------------------------------------------------------240----------------------------------------------------------            
            elif valorCadena[1]=='4':
                letras2 = "cuarenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------250-------------------------------------------------------------
            elif valorCadena[1]=='5':
                letras2 = "cincuenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
            
#-------------------------------------------------------------------------------------------260-------------------------------------------------------------
            elif valorCadena[1]=='6':
                letras2 = "sesenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------270-------------------------------------------------------------
            elif valorCadena[1]=='7':
                letras2 = "setenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
#------------------------------------------------------------------------------------------280-------------------------------------------------------------
            elif valorCadena[1]=='8':
                letras2 = "ochenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"               
#------------------------------------------------------------------------------------------290-------------------------------------------------------------
            elif valorCadena[1]=='9':
                letras2 = "noventa"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
        
        
                
#---------------------------------------------------------------------------------------300----------------------------------------------------------------------------      
        
        elif valorCadena[0] =='3':
            letras = "trescientos"

            if valorCadena[1]=='0':
                letras2 = ""
                if valorCadena[2]=='1':
                    letras3="un"
                elif valorCadena[2]=='2':
                    letras3="dos"
                elif valorCadena[2]=='3':
                    letras3="tres"
                elif valorCadena[2]=='4':
                    letras3="cuatro"
                elif valorCadena[2]=='5':
                    letras3="cinco"
                elif valorCadena[2]=='6':
                    letras3="séis"
                elif valorCadena[2]=='7':
                    letras3="siete"
                elif valorCadena[2]=='8':
                    letras3="ocho"
                elif valorCadena[2]=='9':
                    letras3="nueve"
                
            #------------------------------------------------------------------------------------310-----------------------------------------------------------------                
            if valorCadena[1]=='1' and valorCadena[2]=='0':
                    letras2 ="diez"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='1':
                    letras2 ="once"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='2':
                    letras2 = "doce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='3':
                    letras2 ="trece"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='4':
                    letras2 = "catorce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='5':
                    letras2 ="quince"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='6':
                    letras2 = "dieciséis"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='7':
                    letras2 ="diecisiete"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='8':
                    letras2 = "dieciocho"
                    letras3 =""   
            elif valorCadena[1]=='1' and valorCadena[2]=='9':
                    letras2 = "diecinueve"
                    letras3 =""                
            
            
#--------------------------------------------------------------------------320----------------------------------------------------
            
            elif valorCadena[1]=='2' and valorCadena[2]=='0':
                        letras2 ="veinte"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='1':
                        letras2 = "veintiún"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='2':
                        letras2 = "veintidós"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='3':
                        letras2 ="veintitrés"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='4':
                        letras2 = "veinticuatro"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='5':
                        letras2 = "veinticinco"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='6':
                        letras2 = "veintiséis"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='7':
                        letras2 = "veintisiete"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='8':
                        letras2 = "veintiocho"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='9':
                        letras2 = "veintinueve"
                        letras3 =""
#-------------------------------------------------------------------------------otro metodo 330------------------------------------------------------
            elif valorCadena[1]=='3':
                letras2="treinta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
#---------------------------------------------------------------------------------------340----------------------------------------------------------            
            elif valorCadena[1]=='4':
                letras2 = "cuarenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------350-------------------------------------------------------------
            elif valorCadena[1]=='5':
                letras2 = "cincuenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
            
#------------------------------------------------------------------------------------------360-------------------------------------------------------------
            elif valorCadena[1]=='6':
                letras2 = "sesenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------370-------------------------------------------------------------
            elif valorCadena[1]=='7':
                letras2 = "setenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
#-------------------------------------------------------------------------------------------380-------------------------------------------------------------
            elif valorCadena[1]=='8':
                letras2 = "ochenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"               
#-------------------------------------------------------------------------------------------390-------------------------------------------------------------
            elif valorCadena[1]=='9':
                letras2 = "noventa"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
        
        
        
#----------------------------------------------------------400--------------------------------------------------------------------------------


        elif valorCadena[0] =='4':
            letras = "cuatrocientos"

            if valorCadena[1]=='0':
                letras2 = ""
                if valorCadena[2]=='1':
                    letras3="un"
                elif valorCadena[2]=='2':
                    letras3="dos"
                elif valorCadena[2]=='3':
                    letras3="tres"
                elif valorCadena[2]=='4':
                    letras3="cuatro"
                elif valorCadena[2]=='5':
                    letras3="cinco"
                elif valorCadena[2]=='6':
                    letras3="séis"
                elif valorCadena[2]=='7':
                    letras3="siete"
                elif valorCadena[2]=='8':
                    letras3="ocho"
                elif valorCadena[2]=='9':
                    letras3="nueve"
                
            #--------------------------------------------------------------------------------------410-----------------------------------------------------------------                
            if valorCadena[1]=='1' and valorCadena[2]=='0':
                    letras2 ="diez"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='1':
                    letras2 ="once"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='2':
                    letras2 = "doce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='3':
                    letras2 ="trece"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='4':
                    letras2 = "catorce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='5':
                    letras2 ="quince"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='6':
                    letras2 = "dieciséis"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='7':
                    letras2 ="diecisiete"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='8':
                    letras2 = "dieciocho"
                    letras3 =""   
            elif valorCadena[1]=='1' and valorCadena[2]=='9':
                    letras2 = "diecinueve"
                    letras3 =""                
            
            
#--------------------------------------------------------------------------420----------------------------------------------------
            
            elif valorCadena[1]=='2' and valorCadena[2]=='0':
                        letras2 ="veinte"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='1':
                        letras2 = "veintiún"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='2':
                        letras2 = "veintidós"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='3':
                        letras2 ="veintitrés"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='4':
                        letras2 = "veinticuatro"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='5':
                        letras2 = "veinticinco"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='6':
                        letras2 = "veintiséis"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='7':
                        letras2 = "veintisiete"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='8':
                        letras2 = "veintiocho"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='9':
                        letras2 = "veintinueve"
                        letras3 =""
#-------------------------------------------------------------------------------otro metodo 430------------------------------------------------------
            elif valorCadena[1]=='3':
                letras2="treinta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
#----------------------------------------------------------------------------------------440----------------------------------------------------------            
            elif valorCadena[1]=='4':
                letras2 = "cuarenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------450-------------------------------------------------------------
            elif valorCadena[1]=='5':
                letras2 = "cincuenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
            
#-------------------------------------------------------------------------------------------460-------------------------------------------------------------
            elif valorCadena[1]=='6':
                letras2 = "sesenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------470-------------------------------------------------------------
            elif valorCadena[1]=='7':
                letras2 = "setenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
#-------------------------------------------------------------------------------------------480-------------------------------------------------------------
            elif valorCadena[1]=='8':
                letras2 = "ochenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"               
#-------------------------------------------------------------------------------------------490-------------------------------------------------------------
            elif valorCadena[1]=='9':
                letras2 = "noventa"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
        
        
                
 #-----------------------------------------------------------------------------------------500-------------------------------------------------------------            
        
        elif valorCadena[0] =='5':
            letras = "quinientos"

            if valorCadena[1]=='0':
                letras2 = ""
                if valorCadena[2]=='1':
                    letras3="un"
                elif valorCadena[2]=='2':
                    letras3="dos"
                elif valorCadena[2]=='3':
                    letras3="tres"
                elif valorCadena[2]=='4':
                    letras3="cuatro"
                elif valorCadena[2]=='5':
                    letras3="cinco"
                elif valorCadena[2]=='6':
                    letras3="séis"
                elif valorCadena[2]=='7':
                    letras3="siete"
                elif valorCadena[2]=='8':
                    letras3="ocho"
                elif valorCadena[2]=='9':
                    letras3="nueve"
                
            #--------------------------------------------------------------------------------------510-----------------------------------------------------------------                
            if valorCadena[1]=='1' and valorCadena[2]=='0':
                    letras2 ="diez"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='1':
                    letras2 ="once"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='2':
                    letras2 = "doce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='3':
                    letras2 ="trece"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='4':
                    letras2 = "catorce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='5':
                    letras2 ="quince"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='6':
                    letras2 = "dieciséis"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='7':
                    letras2 ="diecisiete"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='8':
                    letras2 = "dieciocho"
                    letras3 =""   
            elif valorCadena[1]=='1' and valorCadena[2]=='9':
                    letras2 = "diecinueve"
                    letras3 =""                
            
            
#--------------------------------------------------------------------------520----------------------------------------------------
            
            elif valorCadena[1]=='2' and valorCadena[2]=='0':
                        letras2 ="veinte"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='1':
                        letras2 = "veintiún"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='2':
                        letras2 = "veintidós"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='3':
                        letras2 ="veintitrés"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='4':
                        letras2 = "veinticuatro"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='5':
                        letras2 = "veinticinco"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='6':
                        letras2 = "veintiséis"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='7':
                        letras2 = "veintisiete"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='8':
                        letras2 = "veintiocho"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='9':
                        letras2 = "veintinueve"
                        letras3 =""
#-------------------------------------------------------------------------------otro metodo 530------------------------------------------------------
            elif valorCadena[1]=='3':
                letras2="treinta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
#----------------------------------------------------------------------------------------540----------------------------------------------------------            
            elif valorCadena[1]=='4':
                letras2 = "cuarenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------550-------------------------------------------------------------
            elif valorCadena[1]=='5':
                letras2 = "cincuenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
            
#-------------------------------------------------------------------------------------------560-------------------------------------------------------------
            elif valorCadena[1]=='6':
                letras2 = "sesenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------570-------------------------------------------------------------
            elif valorCadena[1]=='7':
                letras2 = "setenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
#-------------------------------------------------------------------------------------------580-------------------------------------------------------------
            elif valorCadena[1]=='8':
                letras2 = "ochenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"               
#-------------------------------------------------------------------------------------------590-------------------------------------------------------------
            elif valorCadena[1]=='9':
                letras2 = "noventa"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
        
        
                
#----------------------------------------------------------------------------------------------600 -----------------------------      
        elif valorCadena[0] =='6':
            letras = "séiscientos"

            if valorCadena[1]=='0':
                letras2 = ""
                if valorCadena[2]=='1':
                    letras3="un"
                elif valorCadena[2]=='2':
                    letras3="dos"
                elif valorCadena[2]=='3':
                    letras3="tres"
                elif valorCadena[2]=='4':
                    letras3="cuatro"
                elif valorCadena[2]=='5':
                    letras3="cinco"
                elif valorCadena[2]=='6':
                    letras3="séis"
                elif valorCadena[2]=='7':
                    letras3="siete"
                elif valorCadena[2]=='8':
                    letras3="ocho"
                elif valorCadena[2]=='9':
                    letras3="nueve"
                
            #-------------------------------------------------------------------------------------610-----------------------------------------------------------------                
            if valorCadena[1]=='1' and valorCadena[2]=='0':
                    letras2 ="diez"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='1':
                    letras2 ="once"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='2':
                    letras2 = "doce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='3':
                    letras2 ="trece"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='4':
                    letras2 = "catorce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='5':
                    letras2 ="quince"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='6':
                    letras2 = "dieciséis"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='7':
                    letras2 ="diecisiete"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='8':
                    letras2 = "dieciocho"
                    letras3 =""   
            elif valorCadena[1]=='1' and valorCadena[2]=='9':
                    letras2 = "diecinueve"
                    letras3 =""                
            
            
#--------------------------------------------------------------------------620----------------------------------------------------
            
            elif valorCadena[1]=='2' and valorCadena[2]=='0':
                        letras2 ="veinte"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='1':
                        letras2 = "veintiún"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='2':
                        letras2 = "veintidós"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='3':
                        letras2 ="veintitrés"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='4':
                        letras2 = "veinticuatro"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='5':
                        letras2 = "veinticinco"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='6':
                        letras2 = "veintiséis"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='7':
                        letras2 = "veintisiete"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='8':
                        letras2 = "veintiocho"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='9':
                        letras2 = "veintinueve"
                        letras3 =""
#-------------------------------------------------------------------------------otro metodo 630------------------------------------------------------
            elif valorCadena[1]=='3':
                letras2="treinta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
#---------------------------------------------------------------------------------------640----------------------------------------------------------            
            elif valorCadena[1]=='4':
                letras2 = "cuarenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------650-------------------------------------------------------------
            elif valorCadena[1]=='5':
                letras2 = "cincuenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
            
#-------------------------------------------------------------------------------------------660-------------------------------------------------------------
            elif valorCadena[1]=='6':
                letras2 = "sesenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------670-------------------------------------------------------------
            elif valorCadena[1]=='7':
                letras2 = "setenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
#------------------------------------------------------------------------------------------680-------------------------------------------------------------
            elif valorCadena[1]=='8':
                letras2 = "ochenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"               
#-------------------------------------------------------------------------------------------690-------------------------------------------------------------
            elif valorCadena[1]=='9':
                letras2 = "noventa"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
        
        
#------------------------------------------------------------------------------------------------------700----------------------------------------------------------
        elif valorCadena[0] =='7':
            letras = "setecientos"

            if valorCadena[1]=='0':
                letras2 = ""
                if valorCadena[2]=='1':
                    letras3="un"
                elif valorCadena[2]=='2':
                    letras3="dos"
                elif valorCadena[2]=='3':
                    letras3="tres"
                elif valorCadena[2]=='4':
                    letras3="cuatro"
                elif valorCadena[2]=='5':
                    letras3="cinco"
                elif valorCadena[2]=='6':
                    letras3="séis"
                elif valorCadena[2]=='7':
                    letras3="siete"
                elif valorCadena[2]=='8':
                    letras3="ocho"
                elif valorCadena[2]=='9':
                    letras3="nueve"
                
            #--------------------------------------------------------------------------------------710-----------------------------------------------------------------                
            if valorCadena[1]=='1' and valorCadena[2]=='0':
                    letras2 ="diez"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='1':
                    letras2 ="once"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='2':
                    letras2 = "doce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='3':
                    letras2 ="trece"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='4':
                    letras2 = "catorce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='5':
                    letras2 ="quince"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='6':
                    letras2 = "dieciséis"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='7':
                    letras2 ="diecisiete"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='8':
                    letras2 = "dieciocho"
                    letras3 =""   
            elif valorCadena[1]=='1' and valorCadena[2]=='9':
                    letras2 = "diecinueve"
                    letras3 =""                
            
            
#--------------------------------------------------------------------------720----------------------------------------------------
            
            elif valorCadena[1]=='2' and valorCadena[2]=='0':
                        letras2 ="veinte"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='1':
                        letras2 = "veintiún"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='2':
                        letras2 = "veintidós"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='3':
                        letras2 ="veintitrés"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='4':
                        letras2 = "veinticuatro"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='5':
                        letras2 = "veinticinco"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='6':
                        letras2 = "veintiséis"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='7':
                        letras2 = "veintisiete"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='8':
                        letras2 = "veintiocho"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='9':
                        letras2 = "veintinueve"
                        letras3 =""
#-------------------------------------------------------------------------------otro metodo 730------------------------------------------------------
            elif valorCadena[1]=='3':
                letras2="treinta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
#----------------------------------------------------------------------------------------740----------------------------------------------------------            
            elif valorCadena[1]=='4':
                letras2 = "cuarenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------750-------------------------------------------------------------
            elif valorCadena[1]=='5':
                letras2 = "cincuenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
            
#------------------------------------------------------------------------------------------760-------------------------------------------------------------
            elif valorCadena[1]=='6':
                letras2 = "sesenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#------------------------------------------------------------------------------------------770-------------------------------------------------------------
            elif valorCadena[1]=='7':
                letras2 = "setenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
#------------------------------------------------------------------------------------------780-------------------------------------------------------------
            elif valorCadena[1]=='8':
                letras2 = "ochenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"               
#------------------------------------------------------------------------------------------790-------------------------------------------------------------
            elif valorCadena[1]=='9':
                letras2 = "noventa"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
        
        
        
       
#--------------------------------------------------------------800---------------------------------------  
        elif valorCadena[0] =='8':
            letras = "ochocientos"

            if valorCadena[1]=='0':
                letras2 = ""
                if valorCadena[2]=='1':
                    letras3="un"
                elif valorCadena[2]=='2':
                    letras3="dos"
                elif valorCadena[2]=='3':
                    letras3="tres"
                elif valorCadena[2]=='4':
                    letras3="cuatro"
                elif valorCadena[2]=='5':
                    letras3="cinco"
                elif valorCadena[2]=='6':
                    letras3="séis"
                elif valorCadena[2]=='7':
                    letras3="siete"
                elif valorCadena[2]=='8':
                    letras3="ocho"
                elif valorCadena[2]=='9':
                    letras3="nueve"
                
            #--------------------------------------------------------------------------------------810-----------------------------------------------------------------                
            if valorCadena[1]=='1' and valorCadena[2]=='0':
                    letras2 ="diez"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='1':
                    letras2 ="once"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='2':
                    letras2 = "doce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='3':
                    letras2 ="trece"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='4':
                    letras2 = "catorce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='5':
                    letras2 ="quince"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='6':
                    letras2 = "dieciséis"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='7':
                    letras2 ="diecisiete"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='8':
                    letras2 = "dieciocho"
                    letras3 =""   
            elif valorCadena[1]=='1' and valorCadena[2]=='9':
                    letras2 = "diecinueve"
                    letras3 =""                
            
            
#--------------------------------------------------------------------------820----------------------------------------------------
            
            elif valorCadena[1]=='2' and valorCadena[2]=='0':
                        letras2 ="veinte"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='1':
                        letras2 = "veintiún"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='2':
                        letras2 = "veintidós"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='3':
                        letras2 ="veintitrés"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='4':
                        letras2 = "veinticuatro"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='5':
                        letras2 = "veinticinco"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='6':
                        letras2 = "veintiséis"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='7':
                        letras2 = "veintisiete"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='8':
                        letras2 = "veintiocho"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='9':
                        letras2 = "veintinueve"
                        letras3 =""
#-------------------------------------------------------------------------------otro metodo 830------------------------------------------------------
            elif valorCadena[1]=='3':
                letras2="treinta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
#----------------------------------------------------------------------------------------840----------------------------------------------------------            
            elif valorCadena[1]=='4':
                letras2 = "cuarenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-----------------------------------------------------------------------------------------850-------------------------------------------------------------
            elif valorCadena[1]=='5':
                letras2 = "cincuenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
            
#------------------------------------------------------------------------------------------860-------------------------------------------------------------
            elif valorCadena[1]=='6':
                letras2 = "sesenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------870-------------------------------------------------------------
            elif valorCadena[1]=='7':
                letras2 = "setenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
#------------------------------------------------------------------------------------------880-------------------------------------------------------------
            elif valorCadena[1]=='8':
                letras2 = "ochenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"               
#-------------------------------------------------------------------------------------------890-------------------------------------------------------------
            elif valorCadena[1]=='9':
                letras2 = "noventa"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
        
        
        
        
#----------------------------------------------------------------------------------900----------------------------------------------------
        elif valorCadena[0] =='9':
            letras = "novecientos"

            if valorCadena[1]=='0':
                letras2 = ""
                if valorCadena[2]=='1':
                    letras3="un"
                elif valorCadena[2]=='2':
                    letras3="dos"
                elif valorCadena[2]=='3':
                    letras3="tres"
                elif valorCadena[2]=='4':
                    letras3="cuatro"
                elif valorCadena[2]=='5':
                    letras3="cinco"
                elif valorCadena[2]=='6':
                    letras3="séis"
                elif valorCadena[2]=='7':
                    letras3="siete"
                elif valorCadena[2]=='8':
                    letras3="ocho"
                elif valorCadena[2]=='9':
                    letras3="nueve"
                
            #--------------------------------------------------------------------------------------910-----------------------------------------------------------------                
            if valorCadena[1]=='1' and valorCadena[2]=='0':
                    letras2 ="diez"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='1':
                    letras2 ="once"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='2':
                    letras2 = "doce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='3':
                    letras2 ="trece"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='4':
                    letras2 = "catorce"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='5':
                    letras2 ="quince"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='6':
                    letras2 = "dieciséis"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='7':
                    letras2 ="diecisiete"
                    letras3 =""
            elif valorCadena[1]=='1' and valorCadena[2]=='8':
                    letras2 = "dieciocho"
                    letras3 =""   
            elif valorCadena[1]=='1' and valorCadena[2]=='9':
                    letras2 = "diecinueve"
                    letras3 =""                
            
            
#--------------------------------------------------------------------------920----------------------------------------------------
            
            elif valorCadena[1]=='2' and valorCadena[2]=='0':
                        letras2 ="veinte"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='1':
                        letras2 = "veintiún"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='2':
                        letras2 = "veintidós"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='3':
                        letras2 ="veintitrés"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='4':
                        letras2 = "veinticuatro"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='5':
                        letras2 = "veinticinco"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='6':
                        letras2 = "veintiséis"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='7':
                        letras2 = "veintisiete"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='8':
                        letras2 = "veintiocho"
                        letras3 =""
            elif valorCadena[1]=='2' and valorCadena[2]=='9':
                        letras2 = "veintinueve"
                        letras3 =""
#-------------------------------------------------------------------------------otro metodo 930------------------------------------------------------
            elif valorCadena[1]=='3':
                letras2="treinta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
#----------------------------------------------------------------------------------------940----------------------------------------------------------            
            elif valorCadena[1]=='4':
                letras2 = "cuarenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------950-------------------------------------------------------------
            elif valorCadena[1]=='5':
                letras2 = "cincuenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
            
#-------------------------------------------------------------------------------------------960-------------------------------------------------------------
            elif valorCadena[1]=='6':
                letras2 = "sesenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
            
#-------------------------------------------------------------------------------------------970-------------------------------------------------------------
            elif valorCadena[1]=='7':
                letras2 = "setenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"      
#-------------------------------------------------------------------------------------------980-------------------------------------------------------------
            elif valorCadena[1]=='8':
                letras2 = "ochenta"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"               
#-------------------------------------------------------------------------------------------990-------------------------------------------------------------
            elif valorCadena[1]=='9':
                letras2 = "noventa"
                if valorCadena[2]=='1':
                    letras3="y un"
                elif valorCadena[2]=='2':
                    letras3="y dos"
                elif valorCadena[2]=='3':
                    letras3="y tres"
                elif valorCadena[2]=='4':
                    letras3="y cuatro"
                elif valorCadena[2]=='5':
                    letras3="y cinco"
                elif valorCadena[2]=='6':
                    letras3="y seis"
                elif valorCadena[2]=='7':
                    letras3="y siete"
                elif valorCadena[2]=='8':
                    letras3="y ocho"
                elif valorCadena[2]=='9':
                    letras3="y nueve"  
        
        
        
        else:
            letras = ""
        

    valorTotal=letras.upper() + " "+ letras2.upper()+" " + letras3.upper()
    return valorTotal



# def download_docx(context = {}):
#     tpl = DocxTemplate(".\GeneradorPromesas\plan\promesaPrueba.docx")
    
#     tpl.render(context)
    
    

#     # save in the memory
#     doc_io = io.BytesIO()
#     tpl.save(doc_io)
#     doc_io.seek(0)
#     response = HttpResponse(doc_io.read())
#     response["Content-Disposition"] = "attachment; filename=generated_doc.docx"
#     response["Content-Type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

    # return response





def Convert(string): 
    list1=[] 
    list1[:]=string 
    return list1 
# Driver code 
def split (listaNueva):
    # print(listaNueva)
    # print(len(listaNueva))
    cantidad =""
    cantidad2 =""
    cantidad3 = ""
    if len(listaNueva) <= 3:
        primeraLista = listaNueva[0:4]
        cantidad = "cientos"
        cantidad2 =""
        cantidad3 = cantidad + cantidad2
        # print (cantidad3)
        # print(numeros_letras(primeraLista))
        return (numeros_letras(primeraLista))
        
    elif 3 < len(listaNueva) <=6:
        cantidad = "mil"
        cantidad2 =""
        cantidad3 = cantidad.upper() + cantidad2.upper()
        # print (cantidad3)
        if len(listaNueva) ==4:
            primeraLista= listaNueva[0]
            segundaLista = listaNueva[1:4]
            # print(primeraLista)
            # print(segundaLista)
            return(numeros_letras(primeraLista) + " " + cantidad3 + " "+ numeros_letras(segundaLista))
            #----------------------------------------por aquí es la vuelta---------------------------------------
            # print(cantidad3)
            # print(numeros_letras(segundaLista))
            
            
        elif len(listaNueva) ==5:
            primeraLista= listaNueva[0:2]
            segundaLista = listaNueva[2:5]
            print(primeraLista)
            print(segundaLista)
            return(numeros_letras(primeraLista) + " " + cantidad3 + " "+ numeros_letras(segundaLista))
            #--------------------------------------------ya tenemos numero---------------------------------
            
        else: 
            primeraLista= listaNueva[0:3]
            segundaLista = listaNueva[3:6]
            print(primeraLista)
            print(segundaLista)
            return(numeros_letras(primeraLista) + " " + cantidad3 + " "+ numeros_letras(segundaLista))
            
    elif 6< len(listaNueva) <=9:
        cantidad = "millones"
        cantidad2="mil"
        cantidad3 = cantidad.upper() + cantidad2.upper()
        # print (cantidad3)
        if len(listaNueva) ==7:
            primeraLista= listaNueva[0]
            if listaNueva[0] =='1':
                cantidad = "millón"

            segundaLista = listaNueva[1:4]
            terceraLista = listaNueva[4:8]
            print(primeraLista)
            print(segundaLista)
            print(terceraLista)
            return(numeros_letras(primeraLista) + " " + cantidad.upper() + " "+ numeros_letras(segundaLista)+" "+cantidad2.upper()+" "+numeros_letras(terceraLista))
            #-------------------------------------------------- yuju----------------------------------------------------------------------
        elif len(listaNueva) ==8:
            primeraLista= listaNueva[0:2]
            segundaLista = listaNueva[2:5]
            terceraLista = listaNueva[5:9]
            print(primeraLista)
            print(segundaLista)
            print(terceraLista)
            return(numeros_letras(primeraLista) + " " + cantidad.upper() + " "+ numeros_letras(segundaLista)+" "+cantidad2.upper()+" "+numeros_letras(terceraLista))
            
        else: 
            primeraLista= listaNueva[0:3]
            segundaLista = listaNueva[3:6]
            terceraLista = listaNueva[6:10]
            print(primeraLista)
            print(segundaLista)
            print(terceraLista)
            return(numeros_letras(primeraLista) + " " + cantidad.upper() + " "+ numeros_letras(segundaLista)+" "+cantidad2.upper()+" "+numeros_letras(terceraLista))
            
    else :
        cantidad = "millones"
        cantidad2="mil"
        cantidad3 = cantidad2 + cantidad + cantidad2
        print (cantidad3)
        if len(listaNueva) ==10:
            primeraLista= listaNueva[0]
            segundaLista = listaNueva[1:4]
            terceraLista = listaNueva[4:7]
            cuartaLista = listaNueva[7:10]
            print(primeraLista)
            print(segundaLista)
            print(terceraLista)
            print(cuartaLista)
            if listaNueva[0]=='1':
                return(cantidad2.upper() + " "+ numeros_letras(segundaLista)+" "+cantidad.upper()+" "+numeros_letras(terceraLista)+" "+cantidad2.upper()+" "+numeros_letras(cuartaLista))
            else:
                return(numeros_letras(primeraLista) + " " + cantidad2.upper() + " "+ numeros_letras(segundaLista)+" "+cantidad.upper()+" "+numeros_letras(terceraLista)+" "+cantidad2.upper()+" "+numeros_letras(cuartaLista))
            return primeraLista, segundaLista, terceraLista, cuartaLista
        elif len(listaNueva) ==11:
            primeraLista= listaNueva[0:2]
            segundaLista = listaNueva[2:5]
            terceraLista = listaNueva[5:8]
            cuartaLista = listaNueva[8:11]
            print(primeraLista)
            print(segundaLista)
            print(terceraLista)
            print(cuartaLista)
            return(numeros_letras(primeraLista) + " " + cantidad2.upper() + " "+ numeros_letras(segundaLista)+" "+cantidad.upper()+" "+numeros_letras(terceraLista)+" "+cantidad2.upper()+" "+numeros_letras(cuartaLista))
        else: 
            primeraLista= listaNueva[0:3]
            segundaLista = listaNueva[3:6]
            terceraLista = listaNueva[6:9]
            cuartaLista = listaNueva[9:12]
            print(primeraLista)
            print(segundaLista)
            print(terceraLista)
            print(cuartaLista)
            return(numeros_letras(primeraLista) + " " + cantidad2.upper() + " "+ numeros_letras(segundaLista)+" "+cantidad.upper()+" "+numeros_letras(terceraLista)+" "+cantidad2.upper()+" "+numeros_letras(cuartaLista))










def formPromesas(request):

    if request.method=="POST":
        miformulario = formularioPromesas(request.POST)

        if miformulario.is_valid():
            infForm = miformulario.cleaned_data
            totalAvaluo = infForm['valor_Terreno'] + infForm ['valor_Dano'] + infForm ['valor_Lucro']
            #pasarlo por el contexto del template
            infForm['totalAvaluo'] = totalAvaluo
            valorLetrasTotal = split(str(infForm['totalAvaluo']))
            infForm['valorLetrasTotal'] = valorLetrasTotal
            valorLetrasTerreno = split(str(infForm['valor_Terreno']))
            infForm['valorLetrasTerreno'] = valorLetrasTerreno
            valorLetrasDano = split(str(infForm['valor_Dano']))
            infForm['valorLetrasDano'] = valorLetrasDano
            valorLetrasLucro = split(str(infForm['valor_Lucro']))
            infForm['valorLetrasLucro'] = valorLetrasLucro
            tpl = DocxTemplate(".\GeneradorPromesas\plan\ofertaContingencia.docx")
    
            tpl.render(infForm)



            # save in the memory
            doc_io = io.BytesIO()
            tpl.save(doc_io)
            doc_io.seek(0)
            response = HttpResponse(doc_io.read())
            response["Content-Disposition"] = "attachment; filename=generated_doc.docx"
            response["Content-Type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

            return response
            
    
    else: 
        miformulario = formularioPromesas()

    return render(request,"GeneradorPromesas/formularioPromesas.html", {"form": miformulario})


def gracias(request):
    return render(request, "GeneradorPromesas/gracias.html")

# def download_docx(request):
#     tpl = DocxTemplate(".\GeneradorPromesas\plan\promesaPrueba.docx")
#     context = {"RT":"49520"}
#     tpl.render(context)
#     # f = open('./promesaPrueba.docx', 'rb')

#     #document = Document('.\plantilla\promesaPrueba.docx')
#     #document.add_heading('Document Title', 0)

#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     response['Content-Disposition'] = 'attachment; filename=promesa%s.docx'%str(RT.getvalue())
#     tpl.save(response)

#     return response

def doc_test(request):
    doc = DocxTemplate(".\GeneradorPromesas\plan\promesaPrueba.docx")
    
    # your code here
    
    context = {'RT':'49520'}
    doc.render(context)
    

    # save in the memory
    doc_io = io.BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)
    response = HttpResponse(doc_io.read())
    response["Content-Disposition"] = "attachment; filename=generated_doc.docx"
    response["Content-Type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

    return response
