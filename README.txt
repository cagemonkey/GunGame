Requirements:
Mattie's Eventscripts v1.3+ (download)
	Go to http://www.eventscripts.com/pages/EventScriptsGuide for help installing
	Eventscripts.
ES_Tools v0.417a+
	This is only required to run the Deathmatch Addon
Mani's Admin Plugin (optional, only used for map voting)
	Recommended Mani Settings:

		// 0 = calculate once per map, 1 = calculate at end of each round (CSS Only)
		mani_stats_mode 0
		
		// This defines whether the tk freeze bomb option can be used or not
		mani_tk_allow_freeze_bomb_option 0
		
		// Allow voting 1 = on, 0 = off (this cvar controls ALL voting)
		mani_voting 1
		
		// 1 = enable cheat detection
		// 0 = disable cheat detection
		// This is recommended by Mani to be disabled, since Valve updated the VAC
		// to catch these.
		mani_protect_against_cheat_cvars 0
		
		// 0 = No warmup time on map load
		// Greater than 0 = number of seconds after map load until map restarts and
		// play continues as normal.
		mani_warmup_timer 0
________________________________________________________________________________
Installation:
Unzip the contents into your cstrike directory.
Edit es_gungame3.txt config section at the top of the file.
Save it as /cstrike/addons/eventscripts/gungame3/es_gungame3.txt on your server
Edit es_gg_votemaps_db.txt in the gg_voting subdirectory if you want to use
Eventscripts for map voting or a mapcycle file. This is experimental ONLY.
Be sure the gungame3 directory and subdirectories are NOT set to READ-ONLY or
your winner and top10 databases will not work.

Sample autoexec.cfg:

mani_reverse_admin_flags 0 // Set the option to reverse the meaning of the admin
flags set in adminlist.txt
mani_reverse_immunity_flags 0 // Set the option to reverse the meaning of the
immunity flags set in immunitylist.txt

mattie_eventscripts 1
eventscripts_subdirectory events

es_load gungame3