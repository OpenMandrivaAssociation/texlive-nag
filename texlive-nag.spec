%global tl_name nag
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	Detecting and warning about obsolete LaTeX commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nag
License:	lppl1.3a
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nag.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nag.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nag.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Old habits die hard. All the same, there are commands, classes and
packages which are outdated and superseded. The nag package provides
routines to warn the user about the use of such obsolete things. As an
example, we provide an extension that detects many of the "sins"
described in l2tabu.

