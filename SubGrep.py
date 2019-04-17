import sublime, sublime_plugin
import re

class SubGrepCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      if not region.empty():
        selection = self.view.substr(region)
        title = "Grep: [%s]" % selection
        syntax = self.view.settings().get('syntax')
        self.view.run_command( 'show_grep', {'title': title, 'selection': selection, 'syntax': syntax} )
class ShowGrepCommand(sublime_plugin.TextCommand):
  def run(self,edit,title,selection,syntax):
    self.grep_view(edit,title,selection, syntax)

  def grep_view(self, edit, title, selection, syntax):
    panel = self.view.window().new_file()
    panel.set_name(title)
    panel.set_scratch(True)
    panel.set_syntax_file(syntax)
    text = self.view.substr(sublime.Region(0, self.view.size()))
    result = ""
    for line in text.split('\n'):
      if selection in line:
        result += "%s\n" % line.rstrip(' ')

    panel.insert(edit, 0, result)
    panel.set_read_only(False)

    return panel

# grep while in find view
class SubRegCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    search_text = self.view.substr(sublime.Region(0, self.view.size()))
    if self.view != sublime.active_window().active_sheet().view():
        title = "RE [%s]" % search_text
        syntax = self.view.settings().get('syntax')
        text = self.get_text_from_active_sheet()
        self.view.run_command( 'show_reg', {'title': title, 'search_text': search_text, 'syntax': syntax, 'text': text} )

  # get text from active view
  def get_text_from_active_sheet(self):
    active_view = sublime.active_window().active_sheet().view()
    region = sublime.Region(0, active_view.size())
    text = active_view.substr(region) 
    return text   

class ShowRegCommand(sublime_plugin.TextCommand):
  def run(self,edit,title,search_text,syntax,text):
    self.grep_view(edit,title,search_text,syntax,text)

  def grep_view(self, edit, title, search_text,syntax,text):
    panel = self.view.window().new_file()
    panel.set_name(title)
    panel.set_scratch(True)
    panel.set_syntax_file(syntax)
    # do regular express here
    pattern = re.compile(search_text)
    result = ""
    for line in text.split('\n'):
      if pattern.search(line):
        result += "%s\n" % line.rstrip(' ')

    panel.insert(edit, 0, result)
    panel.set_read_only(False)

    return panel
