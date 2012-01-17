VERSION = (0, 2, 'unofficial-alpha')


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    try:
        version = '%s.%s.%s' % (version, VERSION[1], VERSION[2])
    except IndexError:
        pass

    return version
