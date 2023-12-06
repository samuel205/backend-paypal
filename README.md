# Orden de pago PAYPAL

Aplicación para el consumo del sdk de paypal.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/samuel205/name_repositorie.git
   cd tu-proyecto
   
2. Crar entonor virutal
   1. Primero instalamos la libreria virtualenv
   ```bash
    python -m pip install virtualenv
      ```
   2. Luego creamos el entorno virutal
   ```bash
    python -m pip virtualenv venv
      ```
   3. Activar entrono virtual
   ```bash
    source venv/Scripts/activate.bat
      ```
   4. Desactivar entorno virutal
    ```bash
   source venv/Scripts/deactivate.bat
      ```
3. Instala las dependencias
   ```bash
   pip install -r req.txt
3. Ejecuta
   ```bash
   npm run dev 
   ```
Si estás viendo esto, probablemente ya hayas hecho este paso. ¡Felicitaciones!

> **Nota:** Se debe contar con el archivo .env con la siguiente estructura - Consulta el tema ***"Cómo manipular el archivo de variables de entorno .env"*** dentro de este documento

```bash
CLIENT_ID="CLIENT_ID"
CLIENT_SECRET="CLIENT_SECRET"
```
> **Nota:** El `CLIENT_ID` y `CLIENT_SECRET` son variables de acceso a la conexión con la api de paypal que ellos mismo proveen para las pruebas de desarrollo y producción

Tener en cuenta antes de ejecutar en el `index.html` actualizar `CLIENTE-ID` segun el que obtengas desde paypal
```
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT-ID"></script>
```