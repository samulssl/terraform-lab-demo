# Guía de explicación (léeme con calma)

## Qué es Terraform, en una idea

Terraform es un programa que construye cosas siguiendo instrucciones escritas en archivos. Tú escribes lo que quieres —por ejemplo, "quiero un contenedor con mi página web"— y él lo hace realidad. La gracia es que esas instrucciones se pueden guardar, copiar a otro computador y repetir, y siempre sale lo mismo. Por eso el taller se hizo con Terraform: para demostrar que un despliegue se puede describir como código y no solo como pasos hechos a mano.

## Qué se hizo en este taller, de principio a fin

Primero se eligió una pieza pequeña y con nombre, `sitio-portafolio`, que no es más que una página web de un solo archivo. Hacerlo pequeño fue a propósito: lo importante no era la página, sino el despliegue. Después se plantearon dos formas de publicar esa página. La primera, que fue la elegida, usa el servidor del laboratorio con Docker: un contenedor con nginx muestra la carpeta de la página. La segunda usa un hosting gratuito en la nube. Cada forma quedó escrita como código Terraform en su propia carpeta, de modo que cualquiera puede reproducirlas. Luego se calcularon los costos: la del laboratorio cuesta cero siempre, y la gratuita cuesta cero hasta que se superan los 500 despliegues mensuales incluidos, punto que se calculó con un script y quedó documentado. También se escribió cómo devolverse si algo sale mal, lo que se llama reversión, y se dejó por escrito por qué ganó la primera opción, documento que se llama ADR. Todo eso junto —supuestos, código, costos, reversión y justificación— es la entrega del taller.

## Qué hace cada comando, sin enredos

Cuando trabajas con Terraform siempre vas en el mismo orden. El `init` prepara el terreno descargando el conector que habla con Docker o con la nube; se hace una sola vez por carpeta. El `validate` revisa que lo escrito esté bien redactado, como un corrector de ortografía: no construye nada. El `plan` te muestra lo que se va a construir antes de construirlo, para que lo revises con calma. El `apply` es el que construye de verdad: descarga, crea y enciende. Por eso pide que escribas `yes`, para que nada se construya por accidente. Y el `destroy` es el botón de deshacer: apaga y borra lo que el `apply` había creado. Si recuerdas una sola frase, que sea esta: el `plan` promete y el `apply` cumple.

## Qué es Docker y por qué aparece tanto

Docker es el programa que permite correr aplicaciones dentro de contenedores, que son como cajas livianas que llevan todo lo necesario para funcionar. En este taller, el contenedor lleva el nginx, que es el servidor que muestra tu página, y tu carpeta con el `index.html` montada dentro. Sin Docker instalado no hay cajas ni servidor, y por eso en tu casa el `plan` se queja y el navegador no muestra nada: no es un error del proyecto, es que falta el programa que levanta todo. En el laboratorio Docker ya existe, así que allá los mismos comandos sí funcionan.

## Qué significa localhost y por qué a veces no se ve nada

Localhost es una forma de decir "este mismo computador". Cuando el contenedor está corriendo en una máquina, abrir `http://localhost:8080` en el navegador de esa misma máquina muestra tu página. Si el contenedor no está corriendo —porque no se hizo el `apply`, porque se hizo el `destroy`, o porque no hay Docker—, el navegador dice que se rechazó la conexión, y eso es normal: no hay nadie atendiendo en ese puerto. Y si intentas abrir ese localhost desde otro dispositivo, tampoco se verá nada, porque cada aparato tiene su propio localhost. Para verlo en otro dispositivo de la misma red WiFi se usa la dirección IP del computador en vez de localhost; desde otra red no se puede, salvo que la página esté publicada en internet.

## Qué papel juega GitHub en todo esto

GitHub es la vitrina y la bodega del código, nada más. Ahí queda guardado el README, el ADR, la página y el código Terraform para que el profesor lo lea y para que cualquiera lo descargue y lo repita en otra máquina. Pero GitHub no ejecuta Terraform ni muestra tu página: subir archivos no es desplegar. La ejecución pasa en tu computador o en el laboratorio, y las pruebas de que funcionó —las salidas del `validate`, del `plan`, del `curl` y del script de costos— son las que se pegan en el README como evidencia.

## Dónde se hace cada cosa

En tu casa ya quedó hecho todo lo que no necesita Docker: instalar Terraform, validar el código, calcular los costos y subir el proyecto a GitHub. En el laboratorio falta la parte que sí necesita Docker: el `plan` completo, el `apply` que levanta el sitio, abrirlo en el navegador y guardar esas salidas como evidencia final. Ninguna de las dos mitades sobra: la de casa demuestra que el código está bien escrito y la del laboratorio demuestra que el despliegue funciona de verdad.

## Dónde corre cada cosa (para no confundirse)

Durante el taller pasaron tres ejecuciones distintas y cada una vive en un lugar diferente. Primera: en tu casa se validó el código con `terraform validate` y se calcularon los costos; eso no levanta nada, solo revisa y calcula. Segunda: en HCP Terraform se corrió un `plan` y un `apply` que salieron en verde, pero aplicaban un código equivocado que solo generaba un nombre aleatorio (`premium-anchovy`); ese verde demostraba que la tubería GitHub-HCP funciona, no que existiera un sitio. Tercera: la página `sitio-portafolio OK` que se vio en `localhost:8080` salió de un servidor temporal de Python en el computador de la casa, que muestra la misma página pero no es el despliegue Terraform. El despliegue de verdad —el contenedor nginx creado por `terraform apply`— solo ocurre donde hay Docker: el laboratorio o Play with Docker. Por eso el repositorio se revirtió a su código correcto: para que lo que está en GitHub sea lo mismo que se despliega.
