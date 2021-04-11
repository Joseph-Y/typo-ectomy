# typo-ectomy
English and medical spellchecker for Anki flashcard software. Download <a href=https://ankiweb.net/shared/info/190806271>here</a>, to ensure folder names are set up correctly during installation. 

**Credit**

**Spellchecker**: Lovac42's add-on Spelling Police was modified to enable Anki's built-in spellchecker.

Changes made: Joseph Yasmeh simplified the settings and added code to automatically install the English and medical dictionaries, without requiring user input. 

**Dictionaries**: The medical <a href="https://github.com/glutanimate/hunspell-en-med-glut-workaround">.dic file</a> was made by Glutanimate (Aristotelis P.), using works by R. Robinson and Rajasekharan N. 

Changes made: Joseph converted the dictionary into a .bdic file that Anki can read. At the time of original publishing (March 2020), this was the first time a medical .bdic file was publicly available, as far as I'm aware. I have since found others <a href="https://github.com/lovac42/SpellingPolice/issues/8" rel="nofollow">here.</a> For anyone curious for how the .dic was converted to .bdic, I used <a href="https://www.qt.io/download">Qt Creator</a> and messed with its built-in qwebengine_convert_dict tool, which is described a bit <a href="https://doc.qt.io/qt-5/qtwebengine-webenginewidgets-spellchecker-example.html">here</a>. You can also try using a <a href="https://chromium.googlesource.com/chromium/src/+/1156a8e6ba080e8890e2a9695bd75c34800d0808/chrome/tools/convert_dict/convert_dict.cc">similar tool</a> in Chromium, but you'd have to build it from source.

The works above were used under a GPL license and with permission of respective authors. 
