#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostGraph_ParallelConan(base.BoostBaseConan):
    name = "boost_graph_parallel"
    version = "1.70.0"
