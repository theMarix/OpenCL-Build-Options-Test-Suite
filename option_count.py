#!/usr/bin/env python
# coding=utf8

# This file is part of the OpenCL Build Options Test Suite.
#
# The OpenCL Build Options Test Suite is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# The OpenCL Build Options Test Suite is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with the OpenCL Build Options Test Suite.  If not, see <http://www.gnu.org/licenses/>.
#
# (c) 2012 Matthias Bach <bach@compeng.uni-frankfurt.de>

import pyopencl as cl
import optparse

def file2string(filename):
	f = open(filename, 'r')
	fstr = ''.join(f.readlines())
	return fstr

if __name__ == '__main__':
	parser = optparse.OptionParser(description='Test whether the compiler can handle a given number of build options.', usage='option_count.py')
	parser.add_option('-d', '--device', type=int, metavar='I', help='The device for which to compile the kernels')
	parser.add_option('-m', '--min', type=int, metavar='N', default=0, help='The minimum number of options to test')
	parser.add_option('-n', '--max', type=int, metavar='N', default=42, help='The maximum number of options to test')
	parser.add_option('-t', '--template', default='-D FOO{0}', help='The template for the option name. Will be python-formatted with an integer')

	(args, files) = parser.parse_args()

	if args.device != None: # compare with None to make device = 0 truthy
		platforms = cl.get_platforms()
		if len(platforms) > 1:
			raise Exception('Found more then one platform, giving up.')
		platform = platforms[0]
		properties = [(cl.context_properties.PLATFORM, platform)]
		devices = [platform.get_devices()[args.device]]
		ctx = cl.Context(devices, properties)
	else:
		ctx = cl.create_some_context()

	device = ctx.devices[0]

	source = file2string('dummy.cl')

	print '# Build Options      Build Result'
	print '---------------------------------'

	for n in xrange(args.min, args.max + 1):
		result = 'success'
		build_options = [args.template.format(i) for i in range(1, n + 1)]
		prg = cl.Program(ctx, source)
		try:
			prg.build(build_options)
		except cl.RuntimeError as err:
			if err.code == -43:
				result = 'invalid build args'
			else:
				result = 'OpenCL error: {0}'.format(err.code)

		print '{0:>15}      {1}'.format(n, result)

