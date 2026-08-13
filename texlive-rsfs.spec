%global tl_name rsfs
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Ralph Smiths Formal Script font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/rsfs
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rsfs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rsfs.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The fonts provide uppercase 'formal' script letters for use as symbols
in scientific and mathematical typesetting (in contrast to the informal
script fonts such as that used for the 'calligraphic' symbols in the TeX
maths symbol font). The fonts are provided as Metafont source, and as
derived Adobe Type 1 format. LaTeX support, for using these fonts in
mathematics, is available via one of the packages calrsfs and mathrsfs.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from rsfs:
MixedMap rsfs.map
TL_DROPIN_EOF
