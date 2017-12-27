from veganpizza import *

l = Listeners()

p = WordListener("pizza", case_insensitive=True)
p.set_action(lock_screen)
l.add_listener(p)

r = replace_text("blurb", "Some long text that you don't want to type again and again.")
l.add_listener(r)

l.wait()
