#!/usr/bin/python -tt

__all__ = ['get_summary']

def get_summary(cmds, title=None):
    frags = []
    if title:
        frags.append(title)

    for name, cmd in cmds.iteritems():
        if hasattr(cmd, 'description'):
            frags.append('  %-14s %s' % (name, cmd.description))

    return '\n'.join(frags)
