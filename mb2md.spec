%include        /usr/lib/rpm/macros.perl
Summary:	Converting Mbox mailboxes to Maildir format
Name:		mb2md
Version:	3.10
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://batleth.sapienti-sat.org/projects/mb2md/%{name}-%{version}.pl
URL:		http://batleth.sapienti-sat.org/projects/mb2md/
BuildRequires:	perl >= 5.6.0
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Perl script that takes one or more Mbox format mailbox files in a
directory and convert them to Maildir format mailboxes.As the Mbox
format has some drawbacks, D. J. Bernstein created the Maildir format
when he wrote Qmail. With the Mbox format all mail of a specific
folder is stored as one large text file. The Maildir format stores
each mail as a seperate file. It is a faster and more efficient way to
store mail. It works particularly well over NFS, which has a long
history of locking-related woes. The Mbox format is used by most of
the POP3/IMAP servers, most mail servers (MTAs) and mail readers
(MUAs). The Maildir format is used by Qmail, Courier-MTA and can be
also used as a alternative mail storage format by Postfix and Exim. A
good POP3/IMAP server for Maildirs is Courier IMAP.

%setup -q -T -c

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/mb2md.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mb2md.pl
