/*const { Client } = require('ssh2');

const conn = new Client();
conn.on('ready', () => {
  console.log('Client :: ready');
  conn.shell((err, stream) => {
    if (err) throw err;
    stream.on('close', () => {
      console.log('Stream :: close');
      conn.end();
    }).on('data', (data) => {
      console.log('OUTPUT: ' + data);
    });
    stream.write('ping localhost\n\n');
    stream.write('^C\n\n');
  });
}).connect({
  host: 'localhost',
  port: 22,
  username: 'kali',
  password: 'kali'
});
*/
var SSH=require('simple-ssh');
var ssh=SSH({host:'localhost',user:'kali',password:'kali'})
ssh.exec('sudo echo "Pseduo"',{
  pty:true,
  out:console.log.bind(console)
}).start();