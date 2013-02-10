# Takes the currently highlighted text and uses it to run a PowerShell command. Pipes the output
# back to the editor and uses it to replace the highlighted text.

import sublime, sublime_plugin, os, subprocess

class ExecutePowerShellInlineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                continue
            s = self.view.substr(region)
            filepath = self.view.file_name()
            if filepath is None:
                current_working_directory = "C:\\"
            else:
                current_working_directory = os.path.dirname(filepath)
            process = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                     '-ExecutionPolicy',
                     'Unrestricted',
                     s], cwd=current_working_directory, stdout=subprocess.PIPE, shell=True)
            result = process.wait()
            if result == 0:
                output = process.stdout.read().strip()
                self.view.replace(edit, region, output)
            else:
            	self.view.replace(edit, region, "ERROR RESULTED FOR COMMAND \"%s\"" % s)
