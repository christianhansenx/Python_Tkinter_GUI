; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{3AF5685A-2605-4DDB-96D8-5F81A9D0F1AD}
AppName=Dice Rolling Simulator
AppVersion=2020-11-15
;AppVerName=Dice Rolling Simulator
AppPublisher="Christian Hansen"
DefaultDirName={autopf}\Dice Rolling Simulator
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir="dist"
OutputBaseFilename=Tkinter_Dice
SetupIconFile="..\..\Tkinter_Dice.ico"
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\pyinstaller\dist\Tkinter_Dice\Tkinter_Dice.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\_queue.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\_tkinter.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\Tkinter_Dice.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-console-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-datetime-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-debug-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-errorhandling-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-file-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-file-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-file-l2-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-handle-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-heap-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-interlocked-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-libraryloader-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-localization-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-memory-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-namedpipe-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-processenvironment-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-processthreads-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-processthreads-l1-1-1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-profile-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-rtlsupport-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-string-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-synch-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-synch-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-sysinfo-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-timezone-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-core-util-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-conio-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-convert-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-environment-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-filesystem-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-heap-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-locale-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-math-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-process-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-runtime-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-stdio-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-string-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-time-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\api-ms-win-crt-utility-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\base_library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\libcrypto-1_1-x64.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\libssl-1_1-x64.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\python37.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\tcl86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\tk86t.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\Tkinter_Dice.exe.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\ucrtbase.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\pyinstaller\dist\Tkinter_Dice\tcl\*"; DestDir: "{app}\tcl"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\pyinstaller\dist\Tkinter_Dice\tk\*"; DestDir: "{app}\tk"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\Dice Rolling Simulator"; Filename: "{app}\Tkinter_Dice.exe"
Name: "{autodesktop}\Dice Rolling Simulator"; Filename: "{app}\Tkinter_Dice.exe"; Tasks: desktopicon
Name: "{autoprograms}\Dice Rolling Simulator"; Filename: "{app}\Tkinter_Dice.exe"; IconFilename: "{app}\Tkinter_Dice.ico"
Name: "{autodesktop}\Dice Rolling Simulator"; Filename: "{app}\Tkinter_Dice.exe"; IconFilename: "{app}\Tkinter_Dice.ico"

[Run]
Filename: "{app}\Tkinter_Dice.exe"; Description: "{cm:LaunchProgram,Dice Rolling Simulator}"; Flags: nowait postinstall skipifsilent

