
if((${CMAKE_SYSTEM_NAME} STREQUAL XCORE_XS3A) OR (${CMAKE_SYSTEM_NAME} STREQUAL XCORE_XS2A))
    ## Create library target
    add_library(framework_rtos_sw_services_dispatcher INTERFACE)
    target_sources(framework_rtos_sw_services_dispatcher
        INTERFACE
            src/dispatch_group.c
            src/dispatch_job.c
            src/dispatcher.c
            src/event_counter.c
    )
    target_include_directories(framework_rtos_sw_services_dispatcher
        INTERFACE
            api
            src
    )
    target_link_libraries(framework_rtos_sw_services_dispatcher
        INTERFACE
            rtos::osal
    )

    ## Create an alias
    add_library(rtos::sw_services::dispatcher ALIAS framework_rtos_sw_services_dispatcher)
endif()
