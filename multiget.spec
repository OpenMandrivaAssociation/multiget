Name:           multiget
Version:        1.2.0
Release:        %mkrel 1
Summary:        Multiget is multi-thread download utility
Group:          Networking/File transfer
License:        GPLv2+
URL:            http://multiget.sourceforge.net/
Source0:        http://nchc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.src.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  wxGTK2.8-devel

%description

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
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

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	--add-category='GTK' \
	%buildroot%_datadir/applications/*.desktop

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
