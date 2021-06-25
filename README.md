## SubGrep is a Sublime Grep plugin

The SubGrep can grep or trim lines by keyword or regular expression. The grep output
still keep origin syntax for better reading.

### Installation by sublime's package control

- ctrl-shift-P brings up command dialog 
- input: "install package"

Or clone/ download this source to the SublimeText package folder.

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

- Grep lines containing current selected text 
- Grep lines containing text in sublime's "find input-bar"
- Grep lines matches regular expression in sublime's "find input-bar"
- Trim lines containing selected text
- Trim lines 

![grep](screenshots/showtime.gif?raw=true)

### Usage examples

- Select "hello" and press "ctrl-shift-g"
- Press "ctrl-f", input text "hello" in find input-bar and press "ctrl-shift-g"
- Press "ctrl-f", input regular express "hello.*" in find input-bar and press "ctrl-shift-g"
