OpenCL Build Options Test Suite
===============================

This is a collection of test cases to check how different OpenCL implementations handle build options passed to the OpenCL compiler.

Currently the only implemented test is a check for the number of build options that can be processed. This is implemented in the script `option_count.py`. Invoking the script with `--help` will give further details. One OpenCL implementation that shows a weak spot in that area is that of OS X Lion, which can only handle even numbers of build options:

	# Build Options      Build Result
	---------------------------------
	              0      success
	              1      invalid build args
	              2      success
	              3      invalid build args
	              4      success
	              5      invalid build args
	              6      success

A further test that should be done, but currently isn't, is specifying include paths containing spaces, as discussed on https://marix.org/content/opencl-und-include.

License
=======

The OpenCL Build Options Test Suite is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

The OpenCL Build Options Test Suite is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with the OpenCL Build Options Test Suite.  If not, see <http://www.gnu.org/licenses/>.

&copy; 2012 Matthias Bach <bach@compeng.uni-frankfurt.de>
