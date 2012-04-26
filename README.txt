## Requirements: ##
*********************************************************************
Eventscripts v1.5.0.171a+
ES_Tools 0.417a+



## Installation: ##
*********************************************************************
1) Make sure your server meets the requirements posted above first.
   If you do not have the requirements met, you will experience
   problems.

2) Download and unzip the GunGame 4 zip file

3) Edit the config file for your language located in the cfg/gungame
   directory.
   a. If you want to use the ggmaplist.txt for voting, you should edit
      that file.
   b. If you want to use the web stats option available in the
      config, edit the included gg4win.php script and place it on
      your web server.

4) Upload all files to your cstrike directory on your game server
   overwriting any existing files. This zip contains some bug fixes
   to a couple of corelib scripts that were included with
   Eventscripts.

5) Add
     es_load gungame4
   to your autoexec.cfg file.
   a. If you want to run the spawnpoint converter to use version 3.4
      spawnpoints in the version 4 Deathmatch addon, then add
        es_load gungame4/addons/gg_converter
      to your autoexec.cfg

6) Restart your server

Note: 
You should restart your server if you want to run version 4 and you
were previously running version 3.
You might get some erratic behavior if you try to just unload version
3 and load version 4 without restarting. 