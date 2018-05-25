import os
import sys
import shutil

def main():
	basePath = 'C:\\\\Program Files\\\\'
	manPath = basePath + 'AbdAlMoniem AlHifnawy\\\\'
	progPath = manPath + 'Subtitle-Renamer\\\\'
	assetsPath = progPath + 'assets\\\\'
	binaryPath = progPath + 'bin\\\\'
	
	try:
		print 'checking if program base folder exits...'
		if not os.path.exists(manPath):
			print 'program base folder doesn\'t exit, creating folder...'
			os.makedirs(manPath)

		print 'checking if program folder exits...'
		if not os.path.exists(progPath):
			print 'program folder doesn\'t exit, creating folder...'
			os.makedirs(progPath)

		print 'copying assets...'
		if not os.path.exists(assetsPath):
			shutil.copytree('..\\assets\\', progPath + 'assets')
		print 'assets copied.'
		
		print 'copying binaries...'
		if not os.path.exists(binaryPath):
			shutil.copytree('..\\src\\', progPath + 'bin')
		print 'binaries copied.'
	except WindowsError as err:
		print err
		exit(1)

	print 'installation directory:', binaryPath

	pythonInstallationDirectory = sys.exec_prefix.replace("\\", "\\\\")
	print 'python installation directory:', pythonInstallationDirectory
	
	pyw = pythonInstallationDirectory + "\\\\pythonw.exe"
	print 'python executable path:', pyw

	print 'creating installation registery file...'
	addRegText = 'Windows Registry Editor Version 5.00\n\n'
	addRegText += '[HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\rename_subs]\n'
	addRegText += '@="Rename Subtitles"\n'
	addRegText += '"NoWorkingDirectory"=""\n'
	addRegText += '"Icon"="%ssubtitle_renamer_icon_modern.ico"\n\n' %assetsPath
	addRegText += '[HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\rename_subs\\command]\n'
	addRegText += '@="\\"%s\\" \\"%srename_subtitles.py\\" \\"%%V\\""' %(pyw, binaryPath)

	addRegFile = open("add-subtitle-renamer.reg", 'w')
	addRegFile.write(addRegText)
	addRegFile.close
	print 'installation registery file created.'
	
	print 'creating uninstallation registery file...'
	remRegText = 'Windows Registry Editor Version 5.00\n\n'
	remRegText += '[-HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\rename_subs]'

	remRegFile = open("remove-subtitle-renamer.reg", 'w')
	remRegFile.write(remRegText)
	remRegFile.close
	print 'uninstallation registery file created.'

	print 'installation complete.'
	
if __name__ == '__main__':
	main()