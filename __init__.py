# -*- coding: utf-8 -*-
#TYPO-ECTOMY: an english and medical spellchecker
#Credits
#
#The spellchecker:
#The code for enabling the spell checker was by Lovac42 (https://github.com/lovac42/SpellingPolice).
#Joseph Yasmeh (jyasmeh@gmail.com) edited the code to simplify the settings, and added code to automatically install US English and Medical dictionaries.
#
#The dictionaries:
#Joseph made the .bdic medical dictionary file from the .dic file by Glutanimate (https://github.com/glutanimate/wordlist-medicalterms-en)
#I used the qwebengine_convert_dict tool in Qt to convert to bdic.
#
#Changelog
#2020-03-10: Published.
#
#License
#GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
#This file was shared privately among Joseph's peers. Do not share this file on AnkiWeb or social media.
################################################################################

# Add names of dictionary files here.
# Make sure you added them to the parent directory, in a folder called "dictionaries"
DICT_FILES = {
    "en-US-9-0",
    "Medicine",
    #An example:
    # "fr-FR-3-0"
}

from aqt.qt import *
from aqt.webview import AnkiWebView
from anki.hooks import wrap, addHook
from anki.lang import _
from functools import partial

#Code that was commented out was from Spelling Police.
#Joseph chose to remove these in order to simplify the settings for the average user.
# from .config import Config
# ADDON_NAME='Typo-ectomy'
# conf = Config(ADDON_NAME)

def replaceMisspelledWord(page, sug_word):
    page.replaceMisspelledWord(sug_word)

def onContextMenuEvent(editor, menu):
    p=editor._page.profile()
    data=editor._page.contextMenuData()
    b=p.isSpellCheckEnabled()
    menu.addSeparator()
    a=menu.addAction(_("Spell Checker"))
    a.setCheckable(True)
    a.setChecked(b)
    a.triggered.connect(lambda:p.setSpellCheckEnabled(not b))
    # if b and conf.get("duck_mode", False):
    if b:
        firstAct=menu.actions()[0]
        for sug_word in data.spellCheckerSuggestions():
            a=menu.addAction(sug_word)
            menu.insertAction(firstAct, a)
            a.triggered.connect(partial(replaceMisspelledWord, editor._page, sug_word))
            # if conf.get("bold_text", True):
            # f=a.font()
            # f.setBold(True)
            # a.setFont(f)
        menu.insertSeparator(firstAct)

addHook("EditorWebView.contextMenuEvent", onContextMenuEvent)

def setupBDIC(web, parent=None):
    p=web._page.profile()
    # p.setSpellCheckEnabled(conf.get("auto_startup", False))
    p.setSpellCheckEnabled(True)
    p.setSpellCheckLanguages(DICT_FILES)

AnkiWebView.__init__=wrap(AnkiWebView.__init__, setupBDIC, "after")

######################################################################
#The next section installs the bundled dictionaries in the right location. Written by Joseph.
######################################################################

import os
import shutil
from aqt import mw

#Gets the parent of the addons21 folder, which is where we want to install the file.
TargetFolder = os.path.join(mw.pm.base)

#Appends two folder names to the Addons folder path, locating the folder we want to move.
File = os.path.join(TargetFolder, 'addons21', '913929891', 'dictionaries')
MissionComplete = os.path.join(TargetFolder, 'dictionaries', 'Medicine.bdic')

#Sets up some pathways to rename an old folder if it exists. For the second condition explained below.
OldDictionaries = os.path.join(TargetFolder, 'dictionaries')
RenamedDictionaries = os.path.join(TargetFolder, 'olddictionaries')

# I like to move it move it.
#The first condition is a workaround in case a previous spellchcker was added. Prevents error saying "dictionaries file already exists."
#The second condition checks if the file was already moved, by asking if File exists as directory.
if os.path.isdir(File) and os.path.isdir(OldDictionaries):
    shutil.move(OldDictionaries, RenamedDictionaries)
if os.path.isdir(File) and not os.path.isfile(MissionComplete):
    shutil.move(File, TargetFolder)

#By the way, if you try to make the TargetFolder with these commands, it won't work.
#Probably due to a relative path being returned. abspath didn't help.
# AddonsFolder = os.getcwd()
# TargetFolder = os.path.dirname(AddonsFolder)
