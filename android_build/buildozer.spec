[app]

# Application name
title = SKADOSH

# Package name
package.name = skadosh

# Package domain
package.domain = org.skadosh

# Source directory
source.dir = ../android_client

# Python files
source.include_exts = py,png,jpg,jpeg,wav,ogg,json,ttf

# Version
version = 0.1.0

# Requirements
requirements = python3,kivy

# Android orientation
orientation = landscape

# Fullscreen
fullscreen = 1

# Android permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,VIBRATE

# Android API
android.api = 35

# Minimum Android API
android.minapi = 23

# Architecture
android.archs = arm64-v8a

# Android entry point
p4a.bootstrap = sdl2

# Presplash
presplash.filename = %(source.dir)s/assets/presplash.png

# Icon
icon.filename = %(source.dir)s/assets/icon.png

# Screen handling
android.allow_backup = True

# Android log level
log_level = 2


[buildozer]

# Build directory
build_dir = .buildozer

# Output directory
bin_dir = bin

# Warning level
warn_on_root = 0

# Verbose output
log_level = 2
