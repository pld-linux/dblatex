Summary:	Convert DocBook to LaTeX, DVI, PostScript, and PDF
Name:		dblatex
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/dblatex/%{name}-%{version}.tar.bz2
# Source0-md5:	7de6bf72b8b2934169ce0ec911e966ed
URL:		http://dblatex.sourceforge.net/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	texlive-latex-appendix
BuildRequires:	texlive-latex-effects
BuildRequires:	texlive-latex-extend
BuildRequires:	transfig
Requires:	python-modules
Requires:	texlive-latex-appendix
Requires:	texlive-latex-effects
Requires:	texlive-latex-extend
Requires:	transfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dblatex is a program that transforms your SGML/XML DocBook documents
to DVI, PostScript or PDF by translating them into pure LaTeX
as a first process.  MathML 2.0 markups are supported, too.

%prep
%setup -q

# fix #!/usr/bin/env python -> #!/usr/bin/python:
%{__sed} -i -e '1s,^#!.*python,#!%{__python},' scripts/%{name}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

rm -r $RPM_BUILD_ROOT%{_datadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/dblatex
%dir %{py_sitescriptdir}/dbtexmf
%{py_sitescriptdir}/dbtexmf/*.py[co]
%dir %{py_sitescriptdir}/dbtexmf/core
%{py_sitescriptdir}/dbtexmf/core/*.py[co]
%{py_sitescriptdir}/dbtexmf/core/sgmlent.txt
%dir %{py_sitescriptdir}/dbtexmf/dblatex
%{py_sitescriptdir}/dbtexmf/dblatex/*.py[co]
%dir %{py_sitescriptdir}/dbtexmf/dblatex/grubber
%{py_sitescriptdir}/dbtexmf/dblatex/grubber/*.py[co]
%dir %{py_sitescriptdir}/dbtexmf/dblatex/xetex
%{py_sitescriptdir}/dbtexmf/dblatex/xetex/*.py[co]
%dir %{py_sitescriptdir}/dbtexmf/xslt
%{py_sitescriptdir}/dbtexmf/xslt/*.py[co]
%{py_sitescriptdir}/dblatex-*.egg-info
%{_datadir}/%{name}
%{_mandir}/man1/*.1*
