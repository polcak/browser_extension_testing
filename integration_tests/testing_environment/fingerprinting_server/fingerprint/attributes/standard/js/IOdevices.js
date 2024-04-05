(function() {
    api.register("io_devices", function() {
        return new Promise((resolve, reject) => {
            navigator.mediaDevices.enumerateDevices()
                .then(devices => {
                        const result = {
                            name: 'io_devices',
                            data: devices
                        };
                        resolve(result);                 
                })
                .catch(error => {
                    const result = {
                        name: 'io_devices',
                        data: 'ERROR'
                    };
                    reject(result);
                });

            setTimeout(() => {
                const result = {
                    name: 'io_devices',
                    data: 'ERROR'
                };
                reject(result);
            }, 10000);
        });
    });
})();
