from conans import ConanFile, tools, os

class BoostGraph_ParallelConan(ConanFile):
    name = "Boost.Graph_Parallel"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/graph_parallel"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "graph_parallel"
    requires =  "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Concept_Check/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Detail/1.64.0@bincrafters/testing", \
                      "Boost.Disjoint_Sets/1.64.0@bincrafters/testing", \
                      "Boost.Dynamic_Biset/1.64.0@bincrafters/testing", \
                      "Boost.Filesystem/1.64.0@bincrafters/testing", \
                      "Boost.Foreach/1.64.0@bincrafters/testing", \
                      "Boost.Function/1.64.0@bincrafters/testing", \
                      "Boost.Functional/1.64.0@bincrafters/testing", \
                      "Boost.Graph/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Lexical_Cast/1.64.0@bincrafters/testing", \
                      "Boost.Mpi/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Optional/1.64.0@bincrafters/testing", \
                      "Boost.Property_Map/1.64.0@bincrafters/testing", \
                      "Boost.Random/1.64.0@bincrafters/testing", \
                      "Boost.Serialization/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.System/1.64.0@bincrafters/testing", \
                      "Boost.Tuple/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Variant/1.64.0@bincrafters/testing"

                      #assert1 concept_check5 config0 core2 detail5 disjoint_sets14 dynamic_bitset12 filesystem8 foreach8 function5 functional5 graph14 iterator5 lexical_cast8 mpi14 mpl5 optional5 property_map14 random9 serialization11 smart_ptr4 static_assert1 tuple4 type_traits3 variant9
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)

    def package_id(self):
        self.info.header_only()