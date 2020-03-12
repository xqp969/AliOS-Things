src = ['board.c']

component = aos_board_component('board_esp32sram', 'esp32', src)

if aos_global_config.get('hci_h4', 0):
    component.add_global_macros('CONFIG_BLE_HCI_H4_UART_PORT=1')


linux_only_targets="blink bluetooth.bleadv bluetooth.bleperipheral bluetooth.breezeapp coapapp helloworld http2app httpapp httpclient_app httpdns_app jsengine_app linkkit_gateway linkkitapp lwm2m_app modbus_app mqttapp otaapp uai_demo.uai_cifar10_demo uai_demo.uai_kws_demo udata_demo.sensor_cloud_demo udata_demo.sensor_local_demo udataapp ulocation.baseapp ulog_app websoc_app wifi_at_app yloop_app yts"
