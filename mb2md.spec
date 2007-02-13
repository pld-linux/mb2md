%include        /usr/lib/rpm/macros.perl
Summary:	Converting Mbox mailboxes to Maildir format
Summary(pl.UTF-8):	Konwerter skrzynek Mbox do formatu Maildir
Name:		mb2md
Version:	3.20
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://batleth.sapienti-sat.org/projects/mb2md/%{name}-%{version}.pl.gz
# Source0-md5:	b47eaa6ae4231a42f4a15564a08eb439
URL:		http://batleth.sapienti-sat.org/projects/mb2md/
BuildRequires:	perl-devel >= 1:5.6.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Perl script that takes one or more Mbox format mailbox files in a
directory and convert them to Maildir format mailboxes. As the Mbox
format has some drawbacks, D. J. Bernstein created the Maildir format
when he wrote Qmail. With the Mbox format all mail of a specific
folder is stored as one large text file. The Maildir format stores
each mail as a seperate file. It is a faster and more efficient way to
store mail. It works particularly well over NFS, which has a long
history of locking-related woes. The Mbox format is used by some of
the POP3/IMAP servers, most mail servers (MTAs) and mail readers
(MUAs). The Maildir format is used by Qmail, Courier-MTA and can be
also used as a alternative mail storage format by Postfix and Exim. A
good POP3/IMAP server for Maildirs is Courier IMAP.

%description -l pl.UTF-8
mb2md to skrypt Perla, który bierze jeden lub więcej plików skrzynek w
formacie Mbox z katalogu i konwertuje je do formatu Maildir. Ponieważ
format Mbox ma pewne wady, D. J. Bernstein przy pisaniu Qmaila
stworzył format Maildir. W formacie Mbox wszystkie wiadomości w danym
folderze są zapisywane w jednym dużym pliku tekstowym. W formacie
Maildir każda wiadomość jest zapisywana jako oddzielny plik. Maildir
jest szybszym i bardziej wydajnym sposobem zapisywania poczty. Działa
szczególnie dobrze po NFS, mającym długą historię problemów związanych
z blokowaniem plików. Format Mbox jest używany przez część serwerów
POP3/IMAP, większość serwerów pocztowych (MTA) oraz czytników poczty
(MUA). Format Maildir jest używany przez Qmaila, Courier-MTA i może
być używany jako alternatywny format także przez Postfiksa i Exima.
Dobrym serwerem POP3/IMAP dla skrzynek Maildir jest Courier IMAP.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

gzip -d -c %{SOURCE0} > $RPM_BUILD_ROOT%{_bindir}/mb2md.pl
# let rpm find deps
chmod 755 $RPM_BUILD_ROOT%{_bindir}/mb2md.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mb2md.pl
