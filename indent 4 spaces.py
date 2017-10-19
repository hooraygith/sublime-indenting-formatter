import sublime
import sublime_plugin

class Indent4SpacesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        tab_size = self.view.settings().get("tab_size")
        syntax = self.view.settings().get("syntax")
        syntax = syntax.split('/').pop()
        print(syntax)
        print(tab_size)

        if tab_size == 2:
            synataxList = [
                'HTML.sublime-syntax',
                'JavaScript.sublime-syntax',
                'CSS.sublime-syntax',
                'SCSS.sublime-syntax',
                'Sass.sublime-syntax',
                'LESS.sublime-syntax',
                'Vue.sublime-syntax',
                'JSX.sublime-syntax',
                'TSX.sublime-syntax',
                'TypeScript.sublime-syntax'
            ]
            if syntax in synataxList:
                # space to tab
                self.view.run_command("unexpand_tabs")
                self.view.settings().set('tab_size', 4)
                # tab to space
                self.view.run_command('expand_tabs')
                self.view.run_command("save")
