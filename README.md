# roundtrip

Template code for calling a Windows process from Linux, copying the Windows process output to Linux, then executing a Linux process on the received file.

Requires OpenSSH on Windows



*P.S.* Comment out the following line in the Windows `sshd_config` file (it's at `C:\ProgramData\ssh`)

    #Match Group administrators
    #   AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys
