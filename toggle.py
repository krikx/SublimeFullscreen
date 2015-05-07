import sublime, sublime_plugin

class CustomFullScreen(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command('toggle_full_screen')
		self.window.run_command('toggle_menu')

def plugin_loaded():
	for window in sublime.windows():
		window.run_command('toggle_full_screen')
		window.run_command('toggle_menu')
