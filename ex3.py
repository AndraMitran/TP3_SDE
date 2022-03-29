def on_forever():
    led.plot(2, 3)
    basic.pause(100)
    led.unplot(2, 3)
basic.forever(on_forever)
