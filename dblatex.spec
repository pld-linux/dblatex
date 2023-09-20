Summary:	Convert DocBook to LaTeX, DVI, PostScript, and PDF
Summary(pl.UTF-8):	Przekształcanie DocBooka do LaTeXa, DVI, PostScriptu i PDF
Name:		dblatex
Version:	0.3.8
Release:	2
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://downloads.sourceforge.net/dblatex/%{name}-%{version}.tar.bz2
# Source0-md5:	7bd20e712f697e3626d2760fb36451ba
Patch0:		%{name}-nodebian.patch
URL:		http://dblatex.sourceforge.net/
BuildRequires:	python >= 2
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.717
BuildRequires:	texlive-latex-ams
BuildRequires:	texlive-latex-appendix
BuildRequires:	texlive-latex-effects
BuildRequires:	texlive-latex-extend
BuildRequires:	texlive-latex-wasysym
BuildRequires:	texlive-makeindex
BuildRequires:	transfig
Requires:	python-modules >= 2
Requires:	texlive-fonts-rsfs
Requires:	texlive-format-pdflatex
Requires:	texlive-latex-ams
Requires:	texlive-latex-appendix
Requires:	texlive-latex-effects
Requires:	texlive-latex-extend
Requires:	texlive-latex-wasysym
Requires:	transfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dblatex is a program that transforms your SGML/XML DocBook documents
to DVI, PostScript or PDF by translating them into pure LaTeX
as a first process. MathML 2.0 markups are supported, too.

%description -l pl.UTF-8
dblatex to program przekształcający dokumenty w formacie SGML/XML
DocBook do formatów DVI, PostScript lub PDF poprzez tłumaczenie ich
najpierw do czystego LaTeXa. Obsługiwane są także znaczniki MathML
2.0.

%prep
%setup -q
%patch0 -p1

# fix #!/usr/bin/env python -> #!/usr/bin/python:
%{__sed} -i -e '1s,^#!.*python,#!%{__python},' scripts/%{name}

%build
#%%py_build

%install
rm -rf $RPM_BUILD_ROOT
#%%py_install

# dblatex script hackery in setup.py doesn't work with split build/install stages
# nor "build --build-base ... install" args
%{__python} setup.py install \
	%{py_install_opts} \
	--root=$RPM_BUILD_ROOT

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT docs/{manual,release-notes}.pdf
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
%{py_sitescriptdir}/dbtexmf/dblatex/grubber/xindylang.xml
%dir %{py_sitescriptdir}/dbtexmf/dblatex/xetex
%{py_sitescriptdir}/dbtexmf/dblatex/xetex/*.py[co]
%dir %{py_sitescriptdir}/dbtexmf/xslt
%{py_sitescriptdir}/dbtexmf/xslt/*.py[co]
%{py_sitescriptdir}/dblatex-*.egg-info
%{_datadir}/%{name}
%{_mandir}/man1/dblatex.1*
