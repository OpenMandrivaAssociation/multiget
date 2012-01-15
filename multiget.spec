Name:		multiget
Version:	1.2.0
Release:	%mkrel 7
Summary:	Easy-to-use GUI file downloader for Windows/Linux/BSDs/MacOs
Group:		Networking/File transfer
License:	GPLv2+
URL:		http://multiget.sourceforge.net/
Source0:	http://nchc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.src.tar.bz2
Patch0:		multiget-1.2-fix-gcc46.patch
Patch1:		multiget-1.2-fix-wx.patch
BuildRequires:	wxgtku-devel
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	glib2-devel
BuildRequires:	pkgconfig(libglade-2.0)

%description
MultiGet is an easy-to-use GUI file downloader for Windows/Linux/
BSDs/MacOs.  It's programmed in C++ and has a GUI based on wxWidgets.
It supports HTTP/FTP protocols which covers the requirements of most
users. It supports multi-task with multi-thread on multi-server. It
supports resuming downloads if the Web server supports it, and if
you like, you can reconfig the thread number without stopping the
current task. It's also support SOCKS 4,4a,5 proxy, ftp proxy, http
proxy.

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_datadir}/applications/*.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%__mkdir_p %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert newicons/16/logo_16.xpm %{buildroot}%{_miconsdir}/%{name}.png
convert newicons/32/logo_32.xpm %{buildroot}%{_iconsdir}/%{name}.png
convert newicons/48/logo_48.xpm %{buildroot}%{_liconsdir}/%{name}.png

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
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

%__rm -fr %{buildroot}%{_prefix}/doc/%{name}

%clean
%__rm -rf %{buildroot}
