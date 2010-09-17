%define	oname	rr

Summary:	RR (Double Ruby)
Name:		rubygem-%{oname}
Version:	1.0.0
Release:	%mkrel 1
License:	GPLv2
Group:		Development/Ruby
URL:		http://rubygems.org/gems/%{oname}
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
Requires:	ruby
BuildArch:	noarch

%description
RR (Double Ruby) is a double framework that features a rich selection of double
techniques and a terse syntax.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

chmod g-w,g+r,o+r -R %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

