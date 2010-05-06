%define name	jinput
%define version	1.1.0
%define release	%mkrel 1

Name:		%{name}
Summary:	Java input API
Version:	%{version}
Release:	%{release} 
Source0:	jinput-src-svn-20100422.tar.bz2
Patch0:		%{name}-%{version}-indexed-jar.patch
URL:		https://jinput.dev.java.net/

Group:		Development/Java
License:	BSD

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ant
BuildRequires:	ant-nodeps
BuildRequires:	java-rpmbuild
BuildRequires:	jutils

Requires:	jutils
Requires:	java

%description
The JInput Project hosts an implementation of an API for game controller
discovery and polled input. It is part of a suite of open-source technologies
initiated by the Game Technology Group with intention of making the development 
of high performance games in Java a reality.

%files
%defattr(-,root,root,-)
%doc www/index.html
%doc README.txt
%doc CHANGES
%_javadir/*.jar
%_libdir/*.so

#--------------------------------------------------------------------

%package	javadoc
Summary:	Javadoc for jinput
Group:		Development/Java

%description javadoc
Javadoc for jinput.

%files javadoc
%defattr(-,root,root,-)
%_javadocdir/*

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p0
pushd lib
rm -f *.jar
ln -s %_javadir/jutils.jar .

%build
export CLASSPATH="." 
%ant all javadoc

%install
rm -rf $RPM_BUILD_ROOT

%__install -dm 755 $RPM_BUILD_ROOT%_javadir
%__install -m 644 dist/jinput.jar $RPM_BUILD_ROOT%_javadir/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%_javadir/%{name}.jar

# native lib
%__install -dm 755 $RPM_BUILD_ROOT%_libdir
%__install -m 644 dist/libjinput-linux*.so $RPM_BUILD_ROOT%_libdir

# javadoc
%__install -dm 755 $RPM_BUILD_ROOT%_javadocdir/%{name}-%{version}
pushd coreAPI/apidocs
cp -pr * $RPM_BUILD_ROOT%_javadocdir/%{name}-%{version}
popd
ln -s %{name}-%{version} $RPM_BUILD_ROOT%_javadocdir/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

