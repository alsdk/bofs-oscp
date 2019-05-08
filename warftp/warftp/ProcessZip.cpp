// ProcessZip.cpp
// Simple CONSOLE program to process incoming .zip
// files for War FTP Daemon
//
// This is a C++ source code file. If you want to modify
// the ProcessZip.exe program you must have a C++ 
// compiler. You can not run this file from the
// command line.
// You can however use Process.Zip.exe as that file
// is the compiled version of this file.

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <process.h>
#include <string.h>

char *FileName;
struct _stat st;

main(int argc, char **argv)
{
	int iRval;
	int Pause = 0;

	if (argc < 2)
		return -1; // Missing filename
	--argc;

	FileName = *++argv;

	if (_stat(FileName,&st))
		return -2; // File does not exuist

	if ((iRval = _spawnlp(_P_WAIT,"unzip.exe","unzip.exe","-tqq",FileName,NULL)) == -1)
		return -3; // Failed to start unzip

	if (iRval)
		return iRval; // Error code returned from unzip

	// Archive is OK. If we have command line arguments, try to extract the file(s)

	while(--argc > 0)
	{
		++argv;
		if (!strcmp(*argv,"-p"))
		{
			++Pause;
			continue;
		}

		fprintf(stderr,"War: Trying to extract '%s'\n", *argv);
		
		// If the file exits, it will not be extracted.
		if(_spawnlp(_P_WAIT,"unzip.exe","unzip.exe","-Cqqn", FileName,*argv,NULL) == 0)
			break; // We have the file
	}

	if (Pause)
	{
		fprintf(stderr,"Press ENTER to continue...");
		getc(stdin);
	}
	return 0; // Archive is OK
}
