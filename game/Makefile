# Project dirs
TARGET   := $(notdir $(CURDIR))
BUILD    := build

# Butano vendored under third_party (RELATIVE paths only)
LIBBUTANO := ../third_party/butano/butano
COMMONREL := ../third_party/butano/common

PYTHON   := python
SOURCES  := src $(COMMONREL)/src
INCLUDES := include $(COMMONREL)/include
DATA     :=
GRAPHICS := graphics $(COMMONREL)/graphics
AUDIO    := audio $(COMMONREL)/audio
DMGAUDIO := dmg_audio $(COMMONREL)/dmg_audio

ROMTITLE := GAME
ROMCODE  := SBTP
USERFLAGS   := -flto
USERASFLAGS :=
USERLDFLAGS :=
USERLIBDIRS :=
USERLIBS    :=
DEFAULTLIBS :=
USERBUILD   :=
EXTTOOL     :=

ifndef LIBBUTANOABS
	export LIBBUTANOABS	:=	$(realpath $(LIBBUTANO))
endif

include $(LIBBUTANOABS)/butano.mak

