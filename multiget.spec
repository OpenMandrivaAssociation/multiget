Name:           multiget
Version:        1.2.0
Release:        %mkrel 2
Summary:	Easy-to-use GUI file downloader for Windows/Linux/BSDs/MacOs
Group:          Networking/File transfer
License:        GPLv2+
URL:            http://multiget.sourceforge.net/
Source0:        http://nchc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.src.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  wxGTK2.8-devel ImageMagick intltool libtool glib2-devel libglade2-devel

%description
MultiGet is an easy-to-use GUI file downloader for Windows/Linux/
BSDs/MacOs.  It's programmed in C++ and has a GUI based on wxWidgets.
It supports HTTP/FTP protocols which covers the requirements of most
users. It supports multi-task with multi-thread on multi-server. It
supports resuming downloads if the Web server supports it, and if
you like, you can reconfig the thread number without stopping the
current task. It's also support SOCKS 4,4a,5 proxy, ftp proxy, http
proxy.

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

rm -fr %buildroot%_prefix/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT
