## SubGrep is a Sublime Grep plugin

Greps contents of current file or view based on text, current selection text or regular express.
The grep output still keep its original syntax for better reading.

### Quick Start
- Clone/download plugin to your SublimeText User folder under SubGrep

### Hotkeys
`Preferences: Package Settings > SubGrep > Key Bindings – User`:


### Hotkeys configuration:

```
  {
    "keys": ["shift+control+g"],
    "command": "sub_grep"
  }
```

### Functions

- Grep current file/view for selected text.
- Grep current file/view based on string in the sublime's "find input-bar"
- Grep current file/view based on regular express in the sublime's "find input-bar"

![grep](screenshots/showtime.gif?raw=true)

### Usage examples

- Select "hello" and press "ctrl-shift-g"
- Press "ctrl-f", input text "hello" in find input-bar and press "ctrl-shift-g"
- Press "ctrl-f", input regular express "hello.*" in find input-bar and press "ctrl-shift-g"
