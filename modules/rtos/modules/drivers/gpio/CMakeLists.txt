
if((${CMAKE_SYSTEM_NAME} STREQUAL XCORE_XS3A) OR (${CMAKE_SYSTEM_NAME} STREQUAL XCORE_XS2A))
    ## Create library target
    add_library(framework_rtos_drivers_gpio INTERFACE)
    target_sources(framework_rtos_drivers_gpio
        INTERFACE
            src/rtos_gpio.c
            src/rtos_gpio_rpc.c
    )
    target_include_directories(framework_rtos_drivers_gpio
        INTERFACE
            api
    )
    target_link_libraries(framework_rtos_drivers_gpio
        INTERFACE
            rtos::osal
    )

    ## Create an alias
    add_library(rtos::drivers::gpio ALIAS framework_rtos_drivers_gpio)
endif()
