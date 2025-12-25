# Copyright (c) 2025 Konsulko Group. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

env__net_dhcp_server = True

env__net_tftp_readable_file = {
    "fn": "1MiBtest.bin",
    "size": 1048576,
    "crc32": "2fa737e0",
}

env__efi_loader_helloworld_file = {
    'fn': 'EFI/arm/helloworld.efi',
    'size': 2320,
    'addr': 0x82000000,
    'crc32': 'e37e06d4',
}
env__efi_helloworld_net_http_test_skip = False

env__efi_loader_grub_file = {
    'fn': 'EFI/arm/grubarm.efi',
    'size': 471040,
    'addr': 0x82000000,
    'crc32': '4a84b065',
}

# No console output from Linux
#env__tftp_boot_test_skip = False
#
#env__net_tftp_bootable_file = {
#    'fn': 'v6.13/image.fit.arm',
#    'addr': 0x82000000,
#    'size': 22348800,
#    'crc32': 'cecdd6f1',
#    'pattern': 'Booting Linux on physical CPU',
#}

# Details regarding a file that may be read from a TFTP server. This variable
# may be omitted or set to None if PXE testing is not possible or desired.
env__net_pxe_bootable_file = {
    'fn': 'default',
    'addr': 0x82000000,
    'size': 64,
    'timeout': 50000,
    'pattern': 'Linux',
    'valid_label': '1',
    'invalid_label': '2',
    'exp_str_invalid': 'Skipping install for failure retrieving',
    'local_label': '3',
    'exp_str_local': 'missing environment variable: localcmd',
    'empty_label': '4',
    'exp_str_empty': 'No kernel given, skipping boot',
}

# False or omitted if a PXE boot test should be tested.
# If PXE boot testing is not possible or desired, set this variable to True.

# For example: If pxe configuration file is not proper to boot
env__pxe_boot_test_skip = False
