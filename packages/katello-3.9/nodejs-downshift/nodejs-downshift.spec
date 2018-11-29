%global npm_name downshift
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.31.15
Release: 1%{?dist}
Summary: A set of primitives to build simple, flexible, WAI-ARIA compliant React autocomplete components
License: MIT
Group: Development/Libraries
URL: https://github.com/paypal/downshift#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr preact %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr typings %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Thu Jun 07 2018 Eric D. Helms <ericdhelms@gmail.com> 1.31.15-1
- Update to 1.31.15

* Thu Apr 19 2018 Eric D. Helms <ericdhelms@gmail.com> 1.28.0-1
- Add nodejs-downshift generated by npm2rpm using the single strategy

