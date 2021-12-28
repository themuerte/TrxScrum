# Project4 "cs50w-project4"

# TrxScrum
Es una plataforma en la que usuarios pueden crear y elimina projectos, tambien en estos proyectos pueden definir tareas basadas en la metodolgia de scrum. Tambien se pueden definir equipos los cuales se pueden agregar a miembros y definirles un rol. 

psdt: TrxScrum esta pensado como una plataforma privada para cualquier organizacion por eso esta no tiene roles mas los propios de Django y cuando se agrega un usuario a un equipo no se le pregunta si se quiere unir solo se agregar y ya.

## Instalacion
- comprobar si esta instalado el: `pipenv`
- colocarse dentro del directorio: `TrxScrum/`
- ejecutar el comando: `pipenv install Pipfile`
- ejecutar el comando: `pipenv shell`

## Paginas
- Lo primero que tenemos es el login y el registro donde en el registro definira el sera nombres, correo, etc. En el login se podra loguear con el username y su password
- Despues de loguearnos tenemos la vista de inicio donde tendriamos los proyectos y los equipos que son nuestros y somos parte en esta vista tambien podemos crear tanto proyectos como equipos
- En la misma vista mencionada anteriormente tenemos una barra de navegacion donde podremos redirigirnos a una seccion de solo nuestros equipos o projectos y tambien podremos modificar nuestra perfil
- En los proyectos podremos hacer todas las operaciones de un CRUD como añadir miempbros y darles un rol, en la parte de info tenemos todo los detalles de un proyecto, tambien sus miembros y tambien podemos crear product backlogs, springs y las tareas del proyecto como aquienes les toca
- En los equipos tambien tenemos todas las funcionalidades de un CRUD, como añadir miembros. En info del equipo tenmos mas detalles como quienes pertenecen a estos quipos

### Bugs 
- Campos de agragar a miembros dequipos y proyectos no validados
- Cuando se agrega alguien a un equipo o proyecto aparece 2 veces 
- Opciones de agregar sprint no funcionales (problemas con la fecha) 

## Links
- Diagrama de BD: https://drive.google.com/file/d/1wBgDz-_JCIosvUVNZB45q5K6dXmtwAUz/view?usp=sharing
- Metodologia Scrum: https://www.wearemarketing.com/es/blog/metodologia-scrum-que-es-y-como-funciona.html

