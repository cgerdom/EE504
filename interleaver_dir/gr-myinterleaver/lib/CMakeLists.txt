# Copyright 2011,2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

list(APPEND myinterleaver_sources
    interleaver_impl.cc
    deinterleaver_impl.cc
)

set(myinterleaver_sources "${myinterleaver_sources}" PARENT_SCOPE)
if(NOT myinterleaver_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT myinterleaver_sources)

add_library(gnuradio-myinterleaver SHARED ${myinterleaver_sources})
target_link_libraries(gnuradio-myinterleaver ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-myinterleaver PROPERTIES DEFINE_SYMBOL "gnuradio_myinterleaver_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-myinterleaver PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
install(TARGETS gnuradio-myinterleaver
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_myinterleaver_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_myinterleaver.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_myinterleaver.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_deinterleaver.cc
)

add_executable(test-myinterleaver ${test_myinterleaver_sources})

target_link_libraries(
  test-myinterleaver
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-myinterleaver
)

GR_ADD_TEST(test_myinterleaver test-myinterleaver)
