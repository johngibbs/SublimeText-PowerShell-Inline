SublimeText PowerShell Inline
=============================

Executes highlighted text as a PowerShell command, pipes the output back to the editor, and replaces the highlighted text with the output.

How to Use
----------

To use it, simply type in a command that can be executed in PowerShell in the Sublime Text editor:

	The quick brown fox jumped over the lazy dog...
	date

Highlight the text ``date`` and press ``CTRL + SHIFT + R``, and the command will be replaced with the result of its execution in PowerShell:

	The quick brown fox jumped over the lazy dog...
	February 9, 2013 8:11:55 PM

Another handy usage is when you need quick math calculations:

	The accuracy of the classifer was 252/(23+344+234+234+344)
	The quick brown fox jumped over the lazy dog...

With this plugin, it becomes:

	The accuracy of the classifer was 0.213740458015267
	The quick brown fox jumped over the lazy dog....

And since PowerShell treats a command as a .NET object, you can do things like this:

	The quick brown fox jumped over the lazy dog....
	"watch out for the dolphins!".ToUpper()

Becomes:

	The quick brown fox jumped over the lazy dog....
	WATCH OUT FOR THE DOLPHINS!