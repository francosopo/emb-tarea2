set(COINES_SDK "/home/franco/COINES_SDK/v2.10.4")


idf_component_register(
    SRCS "force_mode.c"
    INCLUDE_DIRS "include" "${COINES_SDK}/coines-api"
    REQUIRES bme688 common coines
)