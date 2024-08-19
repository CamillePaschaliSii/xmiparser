# -*- coding: utf-8 -*-
import logging
log = logging.getLogger('utils')

specialrpl = {
    u'ö': u'oe',
    u'ü': u'ue',
    u'ä': u'ae',
    u'Ö': u'Oe',
    u'Ü': u'Ue',
    u'Ä': u'Ae',
    u'ß': u'ss',
    # add more for other language here
}

def mapName(oldName):
    return oldName.replace('-', '_')

def toBoolean(v):
    if isinstance(v, (str, str)):
        v = v.lower().strip()
    if v in (0, '0', 'false', False):
        return False
    if v in (1, '1', 'true', True):
        return True
    if v:
        return True
    return False

def normalize(data, doReplace=False):
    """Converts a unicode to string, stripping blank spaces."""
    log.debug("Normalizing %r.", data)
    if not isinstance(data, str):
        log.debug("Not string, returning as-is.")
        return data
    try:
        data = int(data)
        log.debug("Converted to integer, returning %r.",
                  data)
        return data
    except ValueError:
        pass
    try:
        data = float(data)
        log.debug("Converted to float, returning %r.",
                  data)
        return data
    except ValueError:
        pass
    if isinstance(data, bytes):
        # make unicode
        data = data.decode('utf-8')
    if isinstance(data, str):
        data = data.strip()
        if doReplace:
            for key in specialrpl:
                data = data.replace(key, specialrpl[key])    
    if not data is None:
        log.debug("Normalized, returning %r.", data)
        return data
    else:
        return None

# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/148061
def wrap(text, width):
    """
    A word-wrap function that preserves existing line breaks
    and most spaces in the text. Expects that existing line
    breaks are posix newlines (\\n).
    """
    import textwrap
    wrapped = textwrap.wrap(text, width)
    return "".join(wrapped)

