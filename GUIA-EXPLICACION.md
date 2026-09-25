# Guía de explicación (para presentar en primera persona)

## Qué es Terraform, según lo que yo entendí

Yo entendí Terraform como un programa que construye cosas siguiendo instrucciones que yo escribo en archivos. Yo describo lo que quiero —por ejemplo, "quiero un contenedor con mi página web"— y él lo hace realidad. Lo que más me gustó es que esas instrucciones se guardan, se pueden copiar a otro computador y repetir, y siempre sale lo mismo. Por eso hice mi taller con Terraform: para demostrar que un despliegue se puede describir como código y no solo como pasos hechos a mano.

## Qué hice en este taller, de principio a fin

Primero elegí una pieza pequeña y con nombre, `sitio-portafolio`, que no es más que una página web de un solo archivo. La hice pequeña a propósito: lo importante no era la página, sino el despliegue. Después planteé dos formas de publicar esa página. La primera, que fue la que yo elegí, usa el servidor del laboratorio con Docker: un contenedor con nginx muestra mi carpeta de la página. La segunda usa un hosting gratuito en la nube. Cada forma la escribí como código Terraform en su propia carpeta, de modo que cualquiera puede reproducirlas. Luego calculé los costos: la del laboratorio me cuesta cero siempre, y la gratuita me cuesta cero hasta que yo supere los 500 despliegues mensuales incluidos, punto que calculé con mi script y dejé documentado. También escribí cómo devolverme si algo me sale mal, lo que se llama reversión, y dejé por escrito por qué gané con la primera opción, documento que se llama ADR. Todo eso junto —mis supuestos, mi código, mis costos, mi reversión y mi justificación— es mi entrega del taller.

## Qué hace cada comando, como yo lo aprendí

Cuando yo trabajo con Terraform siempre voy en el mismo orden. Con el `init` preparo el terreno descargando el conector que habla con Docker o con la nube; lo hago una sola vez por carpeta. Con el `validate` reviso que lo que escribí esté bien redactado, como un corrector de ortografía: no construye nada. Con el `plan` veo lo que se va a construir antes de construirlo, para revisarlo con calma. Con el `apply` construyo de verdad: se descarga, se crea y se enciende. Por eso me pide que escriba `yes`, para que nada se construya por accidente. Y con el `destroy` deshago: apago y borro lo que mi `apply` había creado. Si me tengo que quedar con una sola frase, es esta: mi `plan` promete y mi `apply` cumple.

## Qué es Docker y por qué me aparece tanto

Yo aprendí que Docker es el programa que permite correr aplicaciones dentro de contenedores, que son como cajas livianas que llevan todo lo necesario para funcionar. En mi taller, el contenedor lleva el nginx, que es el servidor que muestra mi página, y mi carpeta con el `index.html` montada dentro. Sin Docker instalado no hay cajas ni servidor, y por eso en mi casa el `plan` se queja y mi navegador no muestra nada: no es un error de mi proyecto, es que me falta el programa que levanta todo. En el laboratorio Docker ya existe, así que allá mis mismos comandos sí funcionan.

## Qué significa localhost y por qué a veces no veo nada

Yo entendí que localhost es una forma de decir "este mismo computador". Cuando mi contenedor está corriendo en una máquina, si yo abro `http://localhost:8080` en el navegador de esa misma máquina veo mi página. Si mi contenedor no está corriendo —porque no hice el `apply`, porque hice el `destroy`, o porque no hay Docker—, mi navegador dice que se rechazó la conexión, y eso es normal: no hay nadie atendiendo en ese puerto. Y si intento abrir ese localhost desde otro dispositivo, tampoco veo nada, porque cada aparato tiene su propio localhost. Para verlo en otro dispositivo de mi misma red WiFi uso la dirección IP de mi computador en vez de localhost; desde otra red no puedo, salvo que mi página esté publicada en internet.

## Qué papel juega GitHub en mi trabajo

Para mí, GitHub es la vitrina y la bodega de mi código, nada más. Ahí guardé mi README, mi ADR, mi página y mi código Terraform para que el profesor lo lea y para que cualquiera lo descargue y lo repita en otra máquina. Pero GitHub no ejecuta mi Terraform ni muestra mi página: subir archivos no es desplegar. Mi ejecución pasa en mi computador o en el laboratorio, y mis pruebas de que funcionó —mis salidas del `validate`, del `plan`, del `curl` y de mi script de costos— son las que pegué en mi README como evidencia.

## Dónde hice cada cosa

En mi casa hice todo lo que no necesita Docker: instalé Terraform, validé mi código, calculé mis costos y subí mi proyecto a GitHub. En el laboratorio me falta la parte que sí necesita Docker: mi `plan` completo, mi `apply` que levanta el sitio, abrirlo en mi navegador y guardar esas salidas como mi evidencia final. Ninguna de las dos mitades sobra: la de mi casa demuestra que mi código está bien escrito y la del laboratorio demuestra que mi despliegue funciona de verdad.

## Dónde corre cada cosa (para no confundirme)

Durante mi taller pasaron tres ejecuciones distintas y cada una vive en un lugar diferente. Primera: en mi casa validé mi código con `terraform validate` y calculé mis costos; eso no levanta nada, solo revisa y calcula. Segunda: en HCP Terraform corrí un `plan` y un `apply` que salieron en verde, pero aplicaban un código equivocado que solo generaba un nombre aleatorio (`premium-anchovy`); ese verde demostraba que mi tubería GitHub-HCP funciona, no que existiera un sitio, y por eso revertí esos cambios. Tercera: la página `sitio-portafolio OK` que vi en `localhost:8080` salió de un servidor temporal de Python en mi computador, que muestra mi misma página pero no es mi despliegue Terraform. Mi despliegue de verdad —mi contenedor nginx creado por `terraform apply`— solo ocurre donde hay Docker: mi laboratorio o Play with Docker.
