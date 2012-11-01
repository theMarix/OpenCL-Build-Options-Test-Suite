/*
 * This file is part of the OpenCL Build Options Test Suite.
 *
 * The OpenCL Build Options Test Suite is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * The OpenCL Build Options Test Suite is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with the OpenCL Build Options Test Suite.  If not, see <http://www.gnu.org/licenses/>.
 *
 * (c) 2012 Matthias Bach <bach@compeng.uni-frankfurt.de>
 */

__kernel void vecAdd(__global float * const restrict out, __global const float * const restrict in1, __global const float * const restrict in2)
{
	const size_t id = get_global_id(0);
	out[id] = in1[id] + in2[id];
}
