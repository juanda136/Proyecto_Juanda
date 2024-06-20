Usaremos este repositorio para nuestro trabajo colaborativo a través del curso. El objetivo es que afiancemos los conocimientos que vamos obteniendo en las clases.
Parte I: Realizar un Fork
Parte II: Clonar el repositorio local
   clona el repositorio de cuenta de GitHub en tu máquina local (la propia interfaz de GitHub te da la URL en el botón verde "<> Code") 
        git clone <<url de tu repositorio>>
   Establece un 'remote', siendo este el repositorio original:
       git remote add origin https://github.com/YuslyArboleda/Proyecto
Parte III: Mantener el repositorio local actualizado
    Busca cualquier cambio en el remote (en el repositorio original):
        git fetch origin
    Fusiona los cambios del 'remote' (repositorio original) en tu rama master (repositorio local):
        git merge origin/main
Parte IV: Modificar el contenido del repositorio
   En este punto, tienes el repositorio local actualizado. Haz las adiciones necesarias en el repositorio, de acuerdo con el ejercicio específico. 
   Recuerda que debes entregar los ejercicios dentro de la carpeta del tema correspondiente, y además crear una carpeta con tu nombre, donde pondrás los archivos de tus ejercicios.
       Indexa tus cambios, confirma tus cambios en el repositorio local y súbelos a tu repositorio de GitHub:
         git add .
         git commit -m "Mensaje que describa los cambios realizados"
         git push origin master
         
Parte V: Abrir una Pull Request
    En GitHub, haz una Pull Request o solicitd de cambios, para que pueda verificar tus ejercicios y aceptarlos en la rama master del repositorio original si todo está bien y no hay conflictos. 
    El origen debe ser el repositorio de tu cuenta de GitHub y, el destino, este repositorio.
