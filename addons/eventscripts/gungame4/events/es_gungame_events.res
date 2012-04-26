//=========== (C) Copyright 2007 GunGame 4 All rights reserved. ===========
//
// Events triggered by GunGame mod


// No spaces in event names, max length 32
// All strings are case sensitive
// total game event byte length must be < 1024
//
// valid data key types are:
//   none   : value is not networked
//   string : a zero terminated string
//   bool   : unsigned int, 1 bit
//   byte   : unsigned int, 8 bit
//   short  : signed int, 16 bit
//   long   : signed int, 32 bit
//   float  : float, 32 bit

"gungame_events"
{
	"gg_popup_select"
	{
		"userid"	"short"		// userid of the person that selected from the popup
		"selection"	"short"		// the # they chose from the menu
		"menu"		"string"	// the name of the active menu
		"submenu"	"string"	// If there is a submenu set for the menu, this is set to the submenu name
	}
	"gg_levelup"
	{
		"userid"	"short"		// userid of player
		"steamid"	"string"	// steamid of player
		"old_level"	"byte"		// old player level
		"new_level"	"byte"		// new player level
		"team"		"byte"		// player team 2= Terrorists, 3= CT
		"name"		"string"	// player name
		"victim"	"short"		// userid of victim
		"victimname" "string"	// victim's name
	}
	"gg_leveldown"
	{
		"userid"	"short"		// userid of player
		"attacker"	"short"		// userid of the attacker
		"steamid"	"string"	// steamid of player
		"old_level"	"byte"		// old player level
		"new_level"	"byte"		// new player level
		"team"		"byte"		// player team 2= Terrorists, 3= CT
		"name"		"string"	// player name
		"attackername"	"string"	// attacker's name
	}
	"gg_win"
	{
		"userid"	"short"		// userid of player
		"steamid"	"string"	// steamid of player
		"team"		"byte"		// player team 2= Terrorists, 3= CT
		"name"		"string"	// player name
		"loser"		"short"		// userid of player that gave up the win
	}
	"gg_start"
	{
		// No event_vars for this event
		// This event only fires at the end of the warmup round.
		// If your server has no warmup round, use es_map_start.
	}
}
