%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name object-assign

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:    4.1.0
Release:    1%{?dist}
Summary:        ES6 Object.assign() ponyfill
License:        MIT
URL:            https://github.com/sindresorhus/object-assign
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
Source1:        https://raw.githubusercontent.com/sindresorhus/object-assign/master/test.js
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
%endif

%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules

cp -p %{SOURCE1} .

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
mocha
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%doc license
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Sep 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.1.0-1
- Updated with script

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.0.1-7
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.0.1-6
- Rebuilt with updated metapackage

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 4.0.1-5
- Enable find provides and requires macro

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 4.0.1-4
- Enable scl macros

* Fri Dec 18 2015 Troy Dawson <tdawson@redhat.com> - 4.0.1-2
- Update to 4.0.1

* Wed Sep 09 2015 Troy Dawson <tdawson@redhat.com> - 2.0.0-3
- Disable tests until we have all the dependencies

* Sun Dec 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.0-2
- Add test.js from upstream and enable tests

* Thu Dec 04 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.0-1
- Initial packaging
