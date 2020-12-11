library(readxl)
datos<-read_xlsx("F:/uni/DESI/Proyecto final/hdro_statistical_data_table_5.xlsx")
datos<-datos[-c((1:7),70,125,163,200,(207:263)),]
datos<-datos[,-c(1,4,6,8,10,12,14,16,18,20)]
colnames(datos)<-c("Pais","GII","Ranking","Mort.Maternal","Nac.Adolescentes","AsientosParlamento","M.Educacion","H.Educacion","M.Pob.Activa","H.Pob.Activa")
for(j in 1:195){
  if(datos$GII[j]==".."){
    datos$GII[j]=""
  }
}
for(j in 1:195){
  if(datos$Ranking[j]==".."){
    datos$Ranking[j]=""
  }
}
for(j in 1:195){
  if(datos$Mort.Maternal[j]==".."){
    datos$Mort.Maternal[j]=""
  }
}
for(j in 1:195){
  if(datos$Nac.Adolescentes[j]==".."){
    datos$Nac.Adolescentes[j]=""
  }
}
for(j in 1:195){
  if(datos$AsientosParlamento[j]==".."){
    datos$AsientosParlamento[j]=""
  }
}
for(j in 1:195){
  if(datos$M.Educacion[j]==".."){
    datos$M.Educacion[j]=""
  }
}
for(j in 1:195){
  if(datos$H.Educacion[j]==".."){
    datos$H.Educacion[j]=""
  }
}
for(j in 1:195){
  if(datos$M.Pob.Activa[j]==".."){
    datos$M.Pob.Activa[j]=""
  }
}
for(j in 1:195){
  if(datos$H.Pob.Activa[j]==".."){
    datos$H.Pob.Activa[j]=""
  }
}

datos$Pais[datos$Pais=="Czechia"]<-"Czech Republic (Czechia)"
datos$Pais[datos$Pais=="Cabo Verde"]<-"Cape Verde"
datos$Pais[datos$Pais=="Gambia"]<-"The Gambia"
datos$Pais[datos$Pais=="Hong Kong, China (SAR)"]<-"Hong Kong"
datos$Pais[datos$Pais=="Congo (Democratic Republic of the)"]<-"Democratic Republic of the Congo"
datos$Pais[datos$Pais=="Congo"]<-"Republic of Congo"
datos$Pais[datos$Pais=="Korea (Republic of)"]<-"Republic of Korea"
datos$Pais[datos$Pais=="Korea (Democratic People's Rep. of)"]<-"Dem. Rep. Korea"
datos$Pais[datos$Pais=="Eswatini (Kingdom of)"]<-"Swaziland"
write.csv2(datos,"F:/uni/DESI/Proyecto final/DesigualdadGenero.csv",na ="")
