def on_forever():
    led.plot(1, 0)
    led.plot(2, 0)
    led.plot(3, 0)
    led.plot(4, 0)
    led.plot(2, 1)
    led.plot(3, 1)
    led.plot(4, 1)
    led.plot(3, 2)
    led.plot(4, 2)
    led.plot(4, 3)
    basic.pause(200)
    led.unplot(1, 0)
    led.unplot(2, 0)
    led.unplot(3, 0)
    led.unplot(4, 0)
    led.unplot(2, 1)
    led.unplot(3, 1)
    led.unplot(4, 1)
    led.unplot(3, 2)
    led.unplot(4, 2)
    led.unplot(4, 3)
basic.forever(on_forever)
