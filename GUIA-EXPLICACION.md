# Guía de explicación (para presentar en primera persona)

## Lo que hice en mi taller, de principio a fin

Primero elegí una pieza pequeña y con nombre, `sitio-portafolio`, que no es más que una página web de un solo archivo. La hice pequeña a propósito: lo importante no era la página, sino el despliegue. Después planteé dos formas de publicar esa página. La primera, que fue la que yo elegí, usa el servidor del laboratorio con Docker: un contenedor con nginx muestra mi carpeta de la página. La segunda usa un hosting gratuito en la nube. Cada forma la escribí como código Terraform en su propia carpeta, de modo que cualquiera puede reproducirlas.

Luego calculé mis costos: la del laboratorio me cuesta cero siempre, y la gratuita me cuesta cero hasta que yo supere los 500 despliegues mensuales incluidos, punto que calculé con mi script y dejé documentado. Después escribí cómo devolverme si algo me sale mal, lo que se llama reversión, y dejé por escrito por qué gané con la primera opción, documento que se llama ADR. Más adelante conecté mi repo con HCP Terraform y corrí un plan y un apply que salieron en verde, pero aplicaban un código equivocado que solo generaba un nombre aleatorio; ese verde demostraba que mi tubería GitHub-HCP funciona, no que existiera un sitio, y por eso revertí esos cambios y dejé el código correcto. Finalmente validé mi código con `terraform validate`, calculé mis costos con mi script, subí todo a GitHub y dejé listo el despliegue real para ejecutarlo donde hay Docker. Todo eso junto —mis supuestos, mi código, mis costos, mi reversión, mi justificación y mi evidencia— es mi entrega del taller.

## Mis comandos, en cinco líneas

Yo trabajo siempre en el mismo orden. Con `init` preparo el terreno descargando el conector que habla con Docker o con la nube. Con `validate` reviso que lo escrito esté bien redactado, sin construir nada. Con `plan` veo lo que se va a construir antes de construirlo. Con `apply` construyo de verdad, escribiendo `yes` cuando me lo pide. Y con `destroy` deshago lo construido. Mi frase para recordarlo: mi `plan` promete y mi `apply` cumple.

## Dónde corre cada cosa

En mi casa hice todo lo que no necesita Docker: validé mi código, calculé mis costos y subí mi proyecto a GitHub. La página que vi en `localhost:8080` en mi casa salió de un servidor temporal de Python, que muestra mi misma página pero no es mi despliegue Terraform. Mi despliegue de verdad —mi contenedor nginx creado por `terraform apply`— solo ocurre donde hay Docker: mi laboratorio o un playground en el navegador. Y GitHub es mi vitrina: guarda mi código para que el profesor lo lea, pero no ejecuta nada; subir archivos no es desplegar.
