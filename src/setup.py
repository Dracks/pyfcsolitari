from distutils.core import setup
#from setuptools import setup
import sys, os, shutil, string
import pygame

from control.joc import *



PYTHON_MINIMUM = (2, 4)
PYGAME_MINIMUM = (1, 7, 1)



DATA_DIRS = ['Data', 'idioma']

SOL_MODULES = []
def run_checks ():

    pygame_version = None
    try:
        import pygame
        if pygame.version.vernum < PYGAME_MINIMUM:
            raise Exception ("")
        pygame_version = pygame.version.ver
    except ImportError:
        pass

def get_data_files():

    # carreguem la lletra i el icona del pygame per defecte
    pygamedir = os.path.split(pygame.base.__file__)[0]
    pygamefiles = [os.path.join(pygamedir, pygame.font.get_default_font()), os.path.join(pygamedir, 'pygame_icon.bmp')]
    datafiles = [('./pygame', pygamefiles)]
    datafiles=[]

    # segon carreguem els moduls del solitari
    #datafiles.append(('.', SOL_MODULES))
    
    # Agafem altres arxius com els leeme i la configuracio
    datafiles.append(('.', ['LEEME.TXT', 'LEEME.RTF', 'config.cfg']))
    # carreguem tambe els idiomes que soportara
    #datafiles.append(('.', ['idioma/catala.lng']))
    
    # Carreguem tots els directoris i archius recursivament de la carpeta data
    for directory in DATA_DIRS:
        for dirpath, dirnames, filenames in os.walk(directory):
            for name in filenames:
                datafiles.append((dirpath, [os.path.join(dirpath, name)]))
                
    return datafiles
    
    
if __name__ == "__main__":
    run_checks ()
    
    # Delete output directories
    try:
        shutil.rmtree('build')
        shutil.rmtree('dist')
        print('Output directories deleted')
    except:
        print('ERROR: Could not delete output directories')
    
    # Standard distutils.core arguments
    generic_data = {
        "name": "PyFCSolitari",
        "version": VERSIO,
        "description": "Solitari de 8 cartes (Alpha-build for test only)",
        "author": "Jaume Singla Valls",
        "author_email": "",
        "maintainer": "Jaume - Windows/Mac versions",
        "license": "CC nc nd",
        "packages": [],
        "data_files": get_data_files(),
        }
       # "cmdclass": { "install_data" : InstallData },
       # }
    #print generic_data
    
    
    if sys.argv[1] == 'py2exe':
        # Making Windows executable and installer
        import py2exe
        
        # Extra keywords related to py2exe
        extra_data = {
            "windows": [{ "script": "./Solitari.py" #,
    #                      "icon_resources": [(1, "Childsplay.ico")]
                       }],
            "options": {"py2exe": { 
                            "optimize": 0,
                            "bundle_files": 3,
          #                  "excludes": ['dotblas', 'email'],
                            "includes": ['pygame.*', 'control', 'view', 'model'],}
            },
        }        
        
        setup_data = {}
        setup_data.update(generic_data)
        setup_data.update(extra_data)
        
        # Now make the executable
        #sys.argv += ["--skip-archive"]
        setup(**setup_data)
        
        
        # Make InnoSetup script setup.iss from generic.iss
  #      print "Adapting the InnoSetup script: generic.iss..."
  #      setupfile =  os.path.join(os.path.dirname(os.path.abspath (sys.argv[0])), 'dist', 'setup.iss')
        
  #      fpin = open('generic.iss', 'r').read()
  #      fpin = fpin.replace('$AppVerName$', 'PFC- Solitari')
  #      fpin = fpin.replace('$AppVersion$', 'PFC')
  #      fpin = fpin.replace('$VersionInfoVersion$', 'Projecte Final de Carrera')
  #      fpin = fpin.replace('$OutputBaseFilename$', 'Solitari')
  #      fpin = fpin.replace('$BaseDir$', os.path.join(os.path.dirname(os.path.abspath (sys.argv[0]))))
  #      fpout = open(setupfile, 'w')
  #      fpout.write(fpin)        
  #      fpout.close()
        
        # Launch InnoSetup
  #      print "Running Innosetup with setup.iss, please wait..."
  #      cmd = "C:\Programs\Innose~1\Compil32.exe /cc " + setupfile
  #      print cmd
  #      os.system(cmd)
        
  #      print "Finished!"
        
        
#***************************************************************************
# current problems:
# **************************************************************************        
        
        
    
    elif sys.argv[1] == 'py2app':
        # Making Mac OSX executable and disk image
        from setuptools import setup
        OPTIONS= { "argv_emulation": True} #, "iconfile": os.path.join(os.path.dirname(os.path.abspath (sys.argv[0])), "data","Childsplay.icns")}

        # Extra keywords related to py2app
        extra_data = {
            "app": ['Solitari.py'],
            "setup_requires": ['py2app'],
            "options": {'py2app': OPTIONS},
        }
        
        setup_data = {}
        setup_data.update(generic_data)
        setup_data.update(extra_data)
        print generic_data
        print extra_data
        # Now make the application
        setup(**setup_data)          
        
        # Adapt the Disc iMaGe and let ??? make it

#***************************************************************************
# current problems:
# Timer.py not included -> maybe solved by data_files???
# others?
# **************************************************************************          
        
   
    elif sys.argv[1] == 'install':
        # Install in existing Python environment
        print get_data_files()
        shutil.copyfile(ocemp_copy, ocemp_orig)        
        pass
    
    else: 
        print "What do you want to do?"
        print "python setup.py py2exe  -> makes Windows exe"
        print "python setup.py py2app  -> makes Mac OSX exe"
        print "python setup.py install -> installs in Python"

