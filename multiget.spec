Name:           multiget
Version:        1.2.0
Release:        %mkrel 1
Summary:        Multiget is multi-thread download utility
Group:          Networking/File transfer
License:        GPLv2+
URL:            http://multiget.sourceforge.net/
Source0:        http://nchc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.src.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  wxGTK2.8-devel ImageMagick intltool

%description

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_datadir}/applications/*.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %name

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x 
%make 

%install
rm -rf %buildroot
%makeinstall_std

mkdir -p %buildroot{%_iconsdir,%_miconsdir,%_liconsdir}
convert newicons/16/logo_16.xpm %buildroot%_miconsdir/%{name}.png
convert newicons/32/logo_32.xpm %buildroot%_iconsdir/%{name}.png
convert newicons/48/logo_48.xpm %buildroot%_liconsdir/%{name}.png

mkdir -p %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Icon=%{name}
Exec=%{name}
Comment=Multiget is multi-thread download utility
Terminal=false
Type=Application
Categories=GTK;FileTransfer;Network;
StartupNotify=false
EOF

%clean
rm -rf $RPM_BUILD_ROOT
