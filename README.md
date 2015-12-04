==============
nagiosctl
==============

You can control multiple nagios with nagiosctl.

wip

- ``nagiosctl list_hostgroup``
- ``nagiosctl list_host HOSTGROUP``
- ``nagiosctl save_notification HOSTGROUP [HOST]...``
- ``nagiosctl restore_notification``
- ``nagiosctl disable_notification HOSTGROUP [HOST]...``

# Requirement

- Server Side
    - Nagios 4.0.7+ (Require JSON CGI)
    - SSH Login
- Client Side
    - Python 2.7

# Install

TODO

# Usage

If you use on MacOSX, clear ``SSH_AUTH_SOCK`` environment variable.

```
SSH_AUTH_SOCK= nagiosctl list_hostgroup
```
