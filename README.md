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

If you are an active user in communities that carry out incredible contests such as platforms like hackster, you will have had the problem of waiting for the organizers to upload the results of a contest and you will have been like crazy, pressing the refresh of the website with the Hope to see how your project appears in one of the awards.

If that is your case, then we have the solution to your problem!

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

In my case, program an algorithm that checks if a web page has undergone any change, in the particular case of hackster, the pages of the contests, once the ads are published, look like this:

<img src="https://i.ibb.co/y4FrTkR/image.png" width="1000">

To look like this:

<img src="https://i.ibb.co/wdx3B24/image.png" width="1000">

Therefore the first stage for the system to work is to install some software that allows python to run correctly on your OS, in the case of windows I will use Anaconda.

## Install Firefox:

If your main browser is not firefox, download it, it is necessary for the script to work properly, you do not need to make it your main browser.

https://www.mozilla.org/en-US/firefox/new/

## Install Geckodriver:

### Windows:

Add the folder called "Monitor" from the Github repository to the Environment Variables:

<img src="https://i.ibb.co/hstkt8X/image.png" width="1000">

### MacOS:

https://www.kenst.com/2016/12/installing-marionette-firefoxdriver-on-mac-osx/

### Linux:

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

Anaconda documentation already has this guide to do the installation:

https://docs.anaconda.com/anaconda/install/

## Create the OpenCv Environment:

In your command console type the following command to create a specialized environment for this project:

    conda create --name myenv

<img src="https://i.ibb.co/n6HMQm9/image.png" width="1000">

Once the environment is finished, write the following commands to activate the environment and install the necessary libraries, one command per line:

    activate myenv
    pip install selenium opencv-python webbrowser

If everything is done correctly, you can already run the script, the script is executed with the following command.

    python check.py "YOUR_URL_CONTEST"

Real Example for April 17, 2020:

    python check.py "https://www.hackster.io/contests/OnSemi"

# EPIC DEMO:

Video: Click on the image
[![Demo](https://i.ibb.co/nLM2fqW/Untitled-1.png)](https://youtu.be/d2KIuQ6N6Nk)