# revision 24741
# category Package
# catalog-ctan /macros/latex/contrib/nag
# catalog-date 2011-12-03 11:39:13 +0100
# catalog-license lppl
# catalog-version 0.7
Name:		texlive-nag
Version:	0.700
Release:	10
Summary:	Detecting and warning about obsolete LaTeX commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nag
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nag.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nag.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nag.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Old habits die hard. All the same, there are commands, classes
and packages which are outdated and superseded. The nag package
provides routines to warn the user about the use of such
obsolete things. As an example, we provide an extension that
detects many of the "sins" described in l2tabu.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.700-2
+ Revision: 754245
- Rebuild to reduce used resources

* Sat Dec 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.700-1
+ Revision: 740020
- texlive-nag

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.622-1
+ Revision: 719098
- texlive-nag
- texlive-nag
- texlive-nag
- texlive-nag

