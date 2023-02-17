const WebSocket = require('ws')
var os = require('os');
var pty = require('node-pty');
var process=require('node:process');
const wss = new WebSocket.Server({ port: 6060 })

console.log("Socket is up and running...")

var shell = os.platform() === 'win32' ? 'powershell.exe' : 'bash';
var ptyProcess;
wss.on('connection', ws => {
ptyProcess = pty.spawn(shell, [], {
    name: 'xterm-color',
    //   cwd: process.env.HOME,
    env: process.env,
});
    console.log("new session")
    ws.on('message', command => {
        ptyProcess.write(command);
    })

    ptyProcess.on('data', function (data) {
        if(data=='^C')
            ptyProcess.write('\x03');
        ws.send(data)
        console.log(data);

    });
})
