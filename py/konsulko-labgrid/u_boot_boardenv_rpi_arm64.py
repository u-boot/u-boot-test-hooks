# Copyright (c) 2025, Konsulko Group. All rights reserved.
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


env__net_uses_usb = True

env__net_dhcp_server = True

# The file 1MiBtest.bin is created with:
# dd if=/dev/urandom of=1MiBtest.bin bs=1M count=1
env__net_tftp_readable_file = {
    "fn": "1MiBtest.bin",
    "size": 1048576,
    "crc32": "2fa737e0",
    "fnu": "ubtest-upload.bin",
}

# Extracted from a previous U-Boot build.
env__efi_loader_helloworld_file = {
    'fn': 'EFI/arm64/helloworld.efi',
    'size': 4528,
    'addr': 0x00200000,
    'crc32': '2b466005',
}

# Taken from an existing functional binary elsewhere.
env__efi_loader_grub_file = {
    'fn': 'EFI/arm64/grubaa64.efi',
    'size': 724992,
    'addr': 0x00200000,
    'crc32': '8db3f0f1',
}

env__tftp_boot_test_skip = False

# A build of upstream v6.13 arm64 defconfig and image.fit
env__net_tftp_bootable_file = {
    'timeout': 50000,
    'addr': 0x00200000,
    'fn': 'v6.13/image.fit.arm64',
    'size': 28574720,
    'crc32': '8513595c',
    'pattern': 'Booting Linux on physical CPU',
}

# Based on the explanation in test/py/tests/test_net_boot.py
env__net_pxe_bootable_file = {
    'fn': 'default',
    'addr': 0x00200000,
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
env__pxe_boot_test_skip = False

env__bootstage_cmd_file = {
    'addr': 0x2400000,
    'size': 0x1000,
    'bootstage_magic_addr': 0xb00757a3,
}
