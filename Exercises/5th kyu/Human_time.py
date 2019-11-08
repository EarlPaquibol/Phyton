def make_readable(seconds):
    return '{0:02}:{1:02}:{2:02}'.format(int(seconds/3600),int(seconds/60%60),seconds%60)


print(make_readable(86399))
