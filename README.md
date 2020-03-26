# Contest-Monitor
Online contest results monitor.

<img src="https://i.ibb.co/nLM2fqW/Untitled-1.png" width="1000">

# Table of contents

* [Introduction](#introduction)
* [Materials](#materials)
* [Connection Diagram](#connection-diagram)
* [Laptop Setup](#laptop-setup)
* [EPIC DEMO](#epic-demo)

# Introduction:

Si eres un usuario activo en comunidades que realizan increíbles concursos como lo son plataformas como hackster, habrás tenido el problema de estar esperando a que los organizadores suban los resultados de un concurso y habrás estado como loco, presionando el refresh de la pagina web con la esperanza de ver como aparece tu proyecto en alguno de los premios.

Si ese es tu caso, entonces tenemos la solución a tu problema!

# Materials:

Hardware:
- Laptop.                                            x1.

Software:
- Python Anaconda:
https://www.anaconda.com/distribution/

# Connection Diagram:

## Laptop:
<img src="https://i.ibb.co/5k01tdy/cheme.png" width="1000">

# Laptop Setup:

En mi caso programe un algoritmo que revisa si una pagina web ha sufrido algún cambio, en el caso particular de hackster, las paginas de los concursos, una vez publican los anuncios pasan de verse asi:

<img src="https://i.ibb.co/y4FrTkR/image.png" width="1000">

A verse asi:

<img src="https://i.ibb.co/wdx3B24/image.png" width="1000">

Por lo tanto la primera etapa para que funcione el sistema es instalar algun software que permita correr python de forma correcta en tu OS, en el caso de windows usare Anaconda.

## Install Firefox:

Si tu navegador principal no es firefox, descargalo, es necesario para el funcionamiento correcto del script, no es necesario que lo conviertas en tu navegador principal.

https://www.mozilla.org/en-US/firefox/new/

## Install Geckodriver:

Windows:

Añade la carpeta llamada "Monitor" del repositorio de Github a las Environment Variables:

<img src="https://i.ibb.co/hstkt8X/image.png" width="1000">

MacOS:

https://www.kenst.com/2016/12/installing-marionette-firefoxdriver-on-mac-osx/

Linux:

Here are the steps:

Go to the geckodriver releases page. Find the latest version of the driver for your platform and download it. For example:

    wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz

Extract the file with:

    tar -xvzf geckodriver*

Make it executable:

    chmod +x geckodriver

Add the driver to your PATH so other tools can find it:

    export PATH=$PATH:/path-to-extracted-file/.

There are many ways to do this that will work. The above works for me on Ubuntu 16.10 64-bit.

## Install Anaconda:

La documentación de anaconda ya tiene esta guiá para hacer la instalación:

https://docs.anaconda.com/anaconda/install/

## Create the OpenCv Environment:

En tu consola de comandos escribe el siguiente comando para crear un environment especializado para este proyecto:

    conda create --name myenv

<img src="https://i.ibb.co/n6HMQm9/image.png" width="1000">

Una vez se termine de crear el environment, escribe los siguientes comandos para activar el environment e instalar las librerías necesarias, un comando por linea:

    activate myenv
    pip install selenium opencv-python webbrowser

Si todo lo realizas correctamente, ya podras ejecutar el script, el script se ejecuta con el siguiente comando.

    python check.py "YOUR_URL_CONTEST"

Real Example para el dia April 17, 2020:

    python check.py "https://www.hackster.io/contests/OnSemi"

EPIC DEMO:

Video: Click on the image
[![Demo](https://i.ibb.co/nLM2fqW/Untitled-1.png)](https://youtu.be/d2KIuQ6N6Nk)





