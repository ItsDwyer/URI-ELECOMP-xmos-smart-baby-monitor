## XCORE_XS3A only examples
if(${CMAKE_SYSTEM_NAME} STREQUAL XCORE_XS3A)
    include(${CMAKE_CURRENT_LIST_DIR}/freertos/iot/iot.cmake)
else()
    # Get the "version" value from the JSON element
    file(READ settings.json JSON_STRING)
    string(JSON SDK_VERSION GET ${JSON_STRING} ${IDX} version)

    # Determine OS, set up install dir
    if(${CMAKE_SYSTEM_NAME} STREQUAL Windows)
        set(HOST_INSTALL_DIR "$ENV{USERPROFILE}\\.xmos\\SDK\\${SDK_VERSION}\\bin")
    else()
        set(HOST_INSTALL_DIR "/opt/xmos/SDK/${SDK_VERSION}/bin")
    endif()

    install(TARGETS xscope_host_endpoint DESTINATION ${HOST_INSTALL_DIR})
endif()
