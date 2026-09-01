%global tl_name zhmetrics
%global tl_revision 79618
%global tl_version r206

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	TFM subfont files for using Chinese fonts in 8-bit TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/psfonts/zhmetrics
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zhmetrics.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zhmetrics.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zhmetrics.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{version}

%description
These are metrics to use existing Chinese TrueType fonts in workflows
that use LaTeX & dvipdfmx, or pdfLaTeX. The fonts themselves are not
included in the package. Six font families are supported: kai, song,
lishu, fangsong, youyuan and hei. Two encodings (GBK and UTF-8) are
supported.

