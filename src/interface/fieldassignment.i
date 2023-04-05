/**
 * fieldassignment.i
 * 
 * Swig interface file for wrapping api functions in zinc/fieldassignment.hpp
 */
/*
 * Zinc Library
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

%module(package="cmlibs.zinc") fieldassignment

%import "field.i"
%import "node.i"

%{
#include "cmlibs/zinc/fieldassignment.hpp"
#include "cmlibs/zinc/fieldmodule.hpp"
%}

%include "cmlibs/zinc/fieldassignment.hpp"

