Name:		texlive-nag
Version:	0.622
Release:	1
Summary:	Detecting and warning about obsolete LaTeX commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nag
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nag.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nag.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nag.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Old habits die hard. All the same, there are commands, classes
and packages which are outdated and superseded. The nag package
provides routines to warn the user about the use of such
obsolete things. As an example, we provide an extension that
detects many of the "sins" described in l2tabu.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nag/nag-abort.cfg
%{_texmfdistdir}/tex/latex/nag/nag-experimental.cfg
%{_texmfdistdir}/tex/latex/nag/nag-l2tabu.cfg
%{_texmfdistdir}/tex/latex/nag/nag-orthodox.cfg
%{_texmfdistdir}/tex/latex/nag/nag.sty
%doc %{_texmfdistdir}/doc/latex/nag/README
%doc %{_texmfdistdir}/doc/latex/nag/nag.pdf
%doc %{_texmfdistdir}/doc/latex/nag/nagdemo.tex
#- source
%doc %{_texmfdistdir}/source/latex/nag/nag.dtx
%doc %{_texmfdistdir}/source/latex/nag/nag.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
