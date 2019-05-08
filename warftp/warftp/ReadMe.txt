WAR FTP DAEMON
Copyright (C) 1996, 1997 by Jarle (jgaa) Aase. All rights reserved.

WAR FTP Daemon is the premier FTP server for Windows 95 and NT. No other FTP 
server application brings together the UNIX style security features, a BBS 
like Windows interface for the system operator, the extreme flexibility, 
Win95 and NT 4 OLE support, the multithreading design and the advanced 
software technology and performance provided by this package!

PURPOSE:
	FTP server

PLATFORMS:
	Windows95
	NT 3.51 (Intel)
	NT 4.0 (Intel)

	Note: Windows 3.1 is *not* supported and will *not be* supported.

DISTRIBUTION:
	Copyrighted freeware. See the lisence agreement in the online
	help for details. In general: You can use this software unless
	you are the government or the army.

INSTALLATION:
	1) Extract the achive into an empty directory
	2) Run Setup.exe
	3) Delete the extracted files in the temporary dir.

AUTHOR:
	Jarle Aase
	Email: jgaa@online.no
	http://www.jgaa.com

SUPPORT:
	news://alt.comp.jgaa
	Undernet IRC: #war_ftpd
	See also updated support info at http://www.jgaa.com
	

Compatibility 

·	Follows the RFC 959 and 1123 FTP specifications. 
·	Works with Cute-FTP, WS_FTP, ftp (the one following Win95 and NT), 
	MS Internet Explorer, Netscape Navigator, AmFTP, M-FTP, GuiFTP, 
	- in fact, there is hardly reported any incompatibility at all. 
·	Emulates standard UNIX ftp servers, including most ls line 
	parameters and ls formatted output.
·	ABOR command supported. (Yes - it's listed in the RFC, but not 
	all PC based FTP servers can handle it). 

·	REST command supported (Resume an aborted transfer) 
·	Import filter for Serv-U user database
·	Native support for NT service process mode.  
·	Optional Wu-ftpd compatible log for file transfers
·	Operates on Windows95, Windows NT 3.51 (Intel only) and 
	Windows NT 4.0 (Intel only). War FTP Daemon is a native 32 
	bit application and will not work on Windows 3.*. 
	Requires 486 processor or better.

Design 

·	Multithreading 
·	Dialog based system console 
·	Simple and advanced mode of operation, making it perfect for both 
	small and large FTP services. 
·	Users are organized in user-groups and user-classes to ease 
	maintenance of time-out, directory/file access etc. 
·	Automatic shutdown option when the last user has logged off 
·	Displays a list of all users online where you can kick one of them, 
	edit the user database entry, send a message to the user or even spy 
	at the user (see the last given command, current directory, file 
	transfers and a list of all files this user has sent/received 
	during the current session. 
·	Supports user supplied messages to the console through the SITE MSG command. 
·	Supports personal greeting messages to all users, groups and classes. 
·	Full OLE support for Win95/NT4 .lnk shortcuts 
·	Online and off-line operation 
·	In-memory transfer of directory listings 
·	DOS or UNIX style directory paths 
·	Mapping of paths to the root path 
·	Support for long filenames 
·	Virtual file system for improved performance and functionality, 
	including full UNIX-like security and links on directory and file level. 
·	Scheduled re-scans of the Virtual File system to handle changes made 
	on the file system outside the server.
·	"On the fly" generation of index files for the current directory/all 
	files on the system (that the user is allowed to see)
·	Support for comments on any file/directory in "on the fly" 
	generated .index files. 
·	Macros in the welcome files to display the users name, 
	time-out limit etc. 
·	On single network/ppp connections, the server shows the current IP number 
	in an edit window, allowing copy/paste of the number to other applications. 
	It also saves this number to a file.
·	Multihoming/multihosting support allows setup of several virtual FTP servers 
	based on the IP number the user connect to.
·	Context-sensitive Help 
·	Mounting of network drives at startup (NT service mode only)
·	Denial of upload if the free disk  space runs too low
·	Flexible verification option on incoming files. This feature allows you to use 
	"plug-in" modules (external programs) to verify and validate incoming 
	files before the upload is accepted by the server. Can be used for CRC checking, 
	virus scanning, processing of file_id.dix files etc. Several free plug-in 
	modules are made available by experienced War FTP daemon users.

Security 

·	High level of security with directory-level permissions for 
	read, write, execute, dir, mdkdir, rmdir and delete. 
·	Full UNIX security with user group and rwx permissions if 
	the Virtual File System is used 
·	Upload/Download ratio option for anonymous and regular users. 
	Supports file or byte check (upload # files/bytes for each # files/bytes to download). 
	Free files can be defined. 
·	Reports of user access privileges, directory access privileges, etc. 
·	Maximum number of concurrent connections for users, groups and classes.
·	Maximum number of connections based on login IP number (allows you to 
	have ## anonymous logins, but just # concurrent connections from one workstation. 
	Handy to prevent one user from taking up too many connections.
·	Simple one-button enable or disable option for users, groups and classes 
·	IP level access control for the system, users, groups and classes. 
	Incoming connections can be refused before and after login based on 
	the callers IP address.
·	Automatic disable of an account if a selectable number of bad passwords are given 
·	"Not Wanted" list of files that will be refused. 
·	"Dupe checker" that can deny upload of any filename that exist within the paths of the server 
·	Disconnect single users without shutting the system down 
·	No built-in limitations ("crippling"), "secret" connections to my site or any other ugly stuff. 


Significant changes since 1.20b

·	Several important bug-fixes
·	The memory usage in the Virtual File System is reduced by 68%
·	The Virtual File System is optimized. Load time is reduced 
	~70% and flush time reduced to ~ 10 - 100 ms.
·	Many new features. NT users will especially appreciate the NT service mode.
·	Improved performance
·	Improved stability


