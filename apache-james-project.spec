%{?_javapackages_macros:%_javapackages_macros}
%global server_ver      2.2.0
%global short_name      apache-james

Name:             %{short_name}-project
Version:          1.8.1
Release:          9.2
Summary:          Main project POM files and resources
License:          ASL 2.0
Group:            Development/Java
URL:              http://james.apache.org/
# ./create-tarball.sh %%{VERSION}
Source0:          james-project-1.8.1-clean.tar.gz
Source1:          create-tarball.sh
BuildArch:        noarch

BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    maven-local


%description
Main project POM files and resources for Apache James project

%prep
%setup -q -n james-project-%{version}

# generates erroneous runtime dependency
%pom_remove_plugin :maven-doap-plugin

%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-ssh-external']]"
%pom_xpath_remove "pom:dependency[pom:artifactId[text()='wagon-ssh']]"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-8
- Rebuild to regenerate Maven auto-requires

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-7
- Remove BuildRequires on maven-surefire-provider-junit4

* Thu Mar 06 2014 Michal Srb <msrb@redhat.com> - 1.8.1-6
- Remove wagon deps

* Fri Aug 02 2013 Michal Srb <msrb@redhat.com> - 1.8.1-5
- Add create-tarball.sh script to SRPM

* Wed Jul 17 2013 Michal Srb <msrb@redhat.com> - 1.8.1-4
- Build from clean tarball

* Thu Feb  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-3
- Fix maven-local BR

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.8.1-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 09 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8.1-1
- Update to latest upstream, use xmvn to build

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Mar 28 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.6-1
- New upstream version

* Mon Feb 21 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.5-1
- Initial version of the package

