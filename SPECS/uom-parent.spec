Name: uom-parent
Version: 1.0.3
Release: 3%{?dist}
Summary: Units of Measurement Project Parent POM
License: BSD
URL: https://github.com/unitsofmeasurement/uom-parent
Source0: https://github.com/unitsofmeasurement/uom-parent/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: maven-local
BuildRequires: maven-install-plugin

%description
Main parent POM for all Units of Measurement Maven projects.

%prep
%setup -q -n %{name}-%{version}
%pom_remove_parent

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
* Fri Apr 07 2017 Nathan Scott <nathans@redhat.com> - 1.0.3-3
- Rebuilt with a Java 8 buildroot.

* Wed Mar 22 2017 Nathan Scott <nathans@redhat.com> - 1.0.3-2
- Incorporate feedback from gil cattaneo on all uom packages.

* Mon Mar 06 2017 Nathan Scott <nathans@redhat.com> - 1.0.3-1
- Update to latest upstream sources.

* Tue Feb 28 2017 Nathan Scott <nathans@redhat.com> - 1.0.2-2
- Resolve lintian errors - source, license, documentation.

* Fri Feb 17 2017 Nathan Scott <nathans@redhat.com> - 1.0.2-1
- Add unitsofmeasurement prefix to package name.
- Update to latest upstream sources.

* Thu Oct 13 2016 Nathan Scott <nathans@redhat.com> - 1.0.1-1
- Initial version.
