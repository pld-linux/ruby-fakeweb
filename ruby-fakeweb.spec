#
# Conditional build:
%bcond_with	tests		# build without tests

%define	gem_name	fakeweb
Summary:	A tool for faking responses to HTTP requests
Name:		ruby-%{gem_name}
Version:	1.3.0
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	6417e2bed496a716e6247fa474796426
Patch0:		patch_out_samuel.patch
URL:		http://github.com/chrisk/fakeweb
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-http_connection
BuildRequires:	ruby-minitest
BuildRequires:	ruby-mocha
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FakeWeb is a helper for faking web requests in Ruby. It works at a
global level, without modifying code or writing extensive stubs.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}
cd test
%patch0 -p0
cd -

# Don't vendor all your gems...srsly
mv test/vendor .

%build
%if %{with tests}
testrb -Ilib test
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc CHANGELOG LICENSE.txt
%{ruby_vendorlibdir}/fakeweb.rb
%{ruby_vendorlibdir}/fake_web.rb
%{ruby_vendorlibdir}/fake_web
