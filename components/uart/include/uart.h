#ifndef UART_H
#define UART_H

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#include "esp_log.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/uart.h"

#define BUF_SIZE (128) // buffer size
#define TXD_PIN 1  // UART TX pin
#define RXD_PIN 3  // UART RX pin
#define UART_NUM UART_NUM_0   // UART port number
#define BAUD_RATE 115200   // Baud rate

#define REDIRECT_LOGS 1 // if redirect ESP log to another UART

// Function for sending things to UART1
int uart1_printf(void *ap, uint64_t length);

void uart_setup();

// Función para leer desde el serial
int serial_read(char *buffer, int size);

#endif