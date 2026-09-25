# Guía de explicación (para presentar en primera persona)

## Lo que hice en mi taller, de principio a fin

Primero elegí una pieza pequeña y con nombre, `sitio-portafolio`, que no es más que una página web de un solo archivo. La hice pequeña a propósito: lo importante no era la página, sino el despliegue. Después planteé dos formas de publicar esa página. La primera, que fue la que yo elegí, usa un servidor con Docker: un contenedor con nginx muestra mi carpeta de la página. La segunda usa un hosting gratuito en la nube. Cada forma la escribí como código Terraform en su propia carpeta, de modo que cualquiera puede reproducirlas.

Luego calculé mis costos: la del laboratorio me cuesta cero siempre, y la gratuita me cuesta cero hasta que yo supere los 500 despliegues mensuales incluidos, punto que calculé con mi script y dejé documentado. Después escribí cómo devolverme si algo me sale mal, lo que se llama reversión, y dejé por escrito por qué gané con la primera opción, documento que se llama ADR. Subí todo a mi repo de GitHub con su README, su guía y su evidencia.

Mi ejecución real fue así: cloné mi repo en una máquina Ubuntu con Docker, instalé Terraform a mano porque venía vacío, corrí `init` y `validate`, y al aplicar me topé con dos cosas que resolví. Primera: mi variable traía el socket de Windows y allá es Linux, así que apliqué con `-var='docker_host=unix:///var/run/docker.sock'`. Segunda: mi provider traía un cliente Docker viejo (API 1.41) y el daemon exigía mínimo 1.44, así que exporté `DOCKER_API_VERSION=1.44`. Con eso escribí `yes`, el `apply` terminó en `Apply complete!` y mi `curl http://localhost:8080` trajo mi página. Todo eso junto —mis supuestos, mi código, mis costos, mi reversión, mi justificación y mi evidencia— es mi entrega del taller.

## Mis comandos, en cinco líneas

Yo trabajo siempre en el mismo orden. Con `init` preparo el terreno descargando el conector que habla con Docker o con la nube. Con `validate` reviso que lo escrito esté bien redactado, sin construir nada. Con `plan` veo lo que se va a construir antes de construirlo. Con `apply` construyo de verdad, escribiendo `yes` cuando me lo pide. Y con `destroy` deshago lo construido. Mi frase para recordarlo: mi `plan` promete y mi `apply` cumple.

## Dónde corre cada cosa

En mi casa hice todo lo que no necesita Docker: validé mi código, calculé mis costos y subí mi proyecto a GitHub. Mi despliegue de verdad —mi contenedor nginx creado por `terraform apply`— lo corrí en una máquina Ubuntu con Docker, donde también verifiqué mi página con `curl` y en el navegador. Y GitHub es mi vitrina: guarda mi código para que el profesor lo lea, pero no ejecuta nada; subir archivos no es desplegar.
