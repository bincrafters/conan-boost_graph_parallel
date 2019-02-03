#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostGraph_ParallelConan(base.BoostBaseConan):
    name = "boost_graph_parallel"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_graph_parallel"
    lib_short_names = ["graph_parallel"]
    cycle_group = "boost_cycle_group_d"
    b2_requires = ["boost_cycle_group_d"]
