#-
# Copyright 2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:           patterns-BLINUX-std
Version:        2.0
Release:        1
Summary:        Meta package for pattern STD
Group:          Metapackages
License:        BSD-2-Clause
Url:            http://www.blinux.fr
BuildRequires:  patterns
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Provides:       patterns-BLINUX-std

Requires:	patterns-BLINUX
Requires:	patterns-BLINUX-epitech-std

Requires:	grub2-branding-BLINUX
Requires:	grub2-x86_64-efi
Requires:	libexo-1-0-branding-upstream
Requires:	libxfce4ui-branding-upstream
Requires:	rdesktop
Requires:	skel-BLINUX
Requires:	xfce4-appfinder
Requires:	xfce4-appfinder-lang
Requires:	xfce4-dev-tools
Requires:	xfce4-dict
Requires:	xfce4-dict-lang
Requires:	xfce4-icon-theme
Requires:	xfce4-mixer
Requires:	xfce4-mixer-lang
Requires:	xfce4-notifyd
Requires:	xfce4-notifyd-branding-upstream
Requires:	xfce4-notifyd-lang
Requires:	xfce4-panel
Requires:	xfce4-panel-branding-upstream
Requires:	xfce4-panel-devel
Requires:	xfce4-panel-lang
Requires:	xfce4-panel-plugin-battery
Requires:	xfce4-panel-plugin-battery-lang
Requires:	xfce4-panel-plugin-brightness
Requires:	xfce4-panel-plugin-cellmodem
Requires:	xfce4-panel-plugin-cellmodem-lang
Requires:	xfce4-panel-plugin-clipman
Requires:	xfce4-panel-plugin-clipman-doc
Requires:	xfce4-panel-plugin-clipman-lang
Requires:	xfce4-panel-plugin-cpufreq
Requires:	xfce4-panel-plugin-cpufreq-lang
Requires:	xfce4-panel-plugin-cpugraph
Requires:	xfce4-panel-plugin-cpugraph-lang
Requires:	xfce4-panel-plugin-datetime
Requires:	xfce4-panel-plugin-datetime-lang
Requires:	xfce4-panel-plugin-dict
Requires:	xfce4-panel-plugin-diskperf
Requires:	xfce4-panel-plugin-diskperf-lang
Requires:	xfce4-panel-plugin-eyes
Requires:	xfce4-panel-plugin-eyes-lang
Requires:	xfce4-panel-plugin-fsguard
Requires:	xfce4-panel-plugin-fsguard-lang
Requires:	xfce4-panel-plugin-genmon
Requires:	xfce4-panel-plugin-genmon-lang
Requires:	xfce4-panel-plugin-mailwatch
Requires:	xfce4-panel-plugin-mailwatch-lang
Requires:	xfce4-panel-plugin-mixer
Requires:	xfce4-panel-plugin-mount
Requires:	xfce4-panel-plugin-mount-lang
Requires:	xfce4-panel-plugin-mpc
Requires:	xfce4-panel-plugin-mpc-lang
Requires:	xfce4-panel-plugin-multiload-nandhp
Requires:	xfce4-panel-plugin-netload
Requires:	xfce4-panel-plugin-netload-lang
Requires:	xfce4-panel-plugin-netspeed
Requires:	xfce4-panel-plugin-notes
Requires:	xfce4-panel-plugin-notes-lang
Requires:	xfce4-panel-plugin-places
Requires:	xfce4-panel-plugin-places-lang
Requires:	xfce4-panel-plugin-quicklauncher
Requires:	xfce4-panel-plugin-quicklauncher-lang
Requires:	xfce4-panel-plugin-radio
Requires:	xfce4-panel-plugin-radio-lang
Requires:	xfce4-panel-plugin-screenshooter
Requires:	xfce4-panel-plugin-sensors
Requires:	xfce4-panel-plugin-sensors-devel
Requires:	xfce4-panel-plugin-sensors-lang
Requires:	xfce4-panel-plugin-smartbookmark
Requires:	xfce4-panel-plugin-smartbookmark-lang
Requires:	xfce4-panel-plugin-systemload
Requires:	xfce4-panel-plugin-systemload-lang
Requires:	xfce4-panel-plugin-timeout
Requires:	xfce4-panel-plugin-timeout-lang
Requires:	xfce4-panel-plugin-timer
Requires:	xfce4-panel-plugin-timer-lang
Requires:	xfce4-panel-plugin-verve
Requires:	xfce4-panel-plugin-verve-lang
Requires:	xfce4-panel-plugin-wavelan
Requires:	xfce4-panel-plugin-wavelan-lang
Requires:	xfce4-panel-plugin-weather
Requires:	xfce4-panel-plugin-weather-lang
Requires:	xfce4-panel-plugin-whiskermenu
Requires:	xfce4-panel-plugin-whiskermenu-lang
Requires:	xfce4-panel-plugin-xkb
Requires:	xfce4-panel-plugin-xkb-lang
Requires:	xfce4-power-manager
Requires:	xfce4-power-manager-lang
Requires:	xfce4-screenshooter
Requires:	xfce4-screenshooter-doc
Requires:	xfce4-screenshooter-lang
Requires:	xfce4-session
Requires:	xfce4-session-branding-upstream
Requires:	xfce4-session-devel
Requires:	xfce4-session-lang
Requires:	xfce4-settings
Requires:	xfce4-settings-branding-upstream
Requires:	xfce4-settings-lang
Requires:	xfce4-taskmanager
Requires:	xfce4-taskmanager-lang
Requires:	xfce4-terminal
Requires:	xfce4-terminal-lang
Requires:	xfce4-vala
Requires:	xfce4-volumed
Requires:	xfconf
Requires:	xfconf-lang
Requires:	xfdesktop
Requires:	xfdesktop-branding-upstream
Requires:	xfdesktop-lang
Requires:	xfwm4
Requires:	xfwm4-branding-upstream
Requires:	xfwm4-lang
Requires:	xfwm4-themes
Requires:	hplip
Requires:	salt-BLINUX

%description
This is a meta-package for the needs in BLINUX STD

%prep

%build

%install

%files
