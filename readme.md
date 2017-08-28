# Gimp Plugins

This is a repository of some python scripts I've written to automate some things in gimp, like aligning a bunch of layers etc. Hopefully this also serves to help others get into writing python-based plugins for gimp.

## Installing the plugins (on linux)

First, clone this repository (or you could download it as a zip)

```
git clone git@github.com:guysherman/gimp-plugins.git
cd gimp-plugins
```

Then, for each of the plugins you want to install, you can install for yourself only:

```
cp <plugin-filename> ~/.gimp-<your-gimp-verion-number>/plug-ins/
chmod +x ~/.gimp-<your-gimp-verion-number>/plug-ins/<plugin-filename>
```

eg:

```
cp align-all-layers.py ~/.gimp-2.8/plug-ins/
chmod +x ~/.gimp-2.8/plug-ins/align-all-layers.py
```

**Or**

You could install for all users. In this case you'll need to find where the global plugins folder is. You can look this up in Gimp by going `Edit > Preferences > Folders > Plugins`. In my case (Arch Linux) I use `/usr/lib/gimp/2.0/plug-ins/` instead of `~/.gimp-<your-gimp-verion-number>/plug-ins/`

eg:

```
cp align-all-layers.py /usr/lib/gimp/2.0/plug-ins/
chmod +x /usr/lib/gimp/2.0/plug-ins/align-all-layers.py
```


