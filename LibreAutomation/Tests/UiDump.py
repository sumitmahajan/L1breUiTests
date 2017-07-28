from uiautomator import device as d

d.info
d.screen.on()
d(text="Settings").click()
d(scrollable=True).scroll.vert.forward()
d().gestureM((100,200),(100,300),(100,400)).to((100,400),(100,400),(100,400),100)