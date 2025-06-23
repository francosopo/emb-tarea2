#include <uart.h>

// Function for sending things to UART1
// length: total size of ap, in bytes
int uart1_printf(void *ap, uint64_t length) {
    uart_write_bytes(UART_NUM, ap, (size_t) length);
    return 0;
}

// Setup of UART connections 0 and 1, and try to redirect logs to UART1 if asked
void uart_setup() {
    uart_config_t uart_config = {
        .baud_rate = 115200,
        .data_bits = UART_DATA_8_BITS,
        .parity = UART_PARITY_DISABLE,
        .stop_bits = UART_STOP_BITS_1,
        .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
    };

    uart_param_config(UART_NUM_0, &uart_config);
    uart_param_config(UART_NUM_1, &uart_config);
    uart_driver_install(UART_NUM_0, BUF_SIZE * 2, 0, 0, NULL, 0);
    uart_driver_install(UART_NUM_1, BUF_SIZE * 2, 0, 0, NULL, 0);

    // Redirect ESP log to UART1
    /*if (REDIRECT_LOGS) {
        esp_log_set_vprintf(uart1_printf);
    }*/
}

// Read UART_num for input with timeout of 1 sec
int serial_read(char *buffer, int size){
    int len = uart_read_bytes(UART_NUM, (uint8_t*)buffer, size, pdMS_TO_TICKS(1000));
    return len;
}

int serial_raw_read(void *buffer, int size){
    int len = uart_read_bytes(UART_NUM, buffer, size, pdMS_TO_TICKS(1000) );
    return len;
}
int serial_int_read(int *buffer, int size){
    int len = uart_read_bytes(UART_NUM, (int32_t*) buffer, size, pdMS_TO_TICKS(1000) );
    return len;
}