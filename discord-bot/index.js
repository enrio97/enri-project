const Discord= require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`봇이 준비되었습니다`);
});

client.on('message', msg  => {
 

  if (msg.content === '야!') {
     msg.reply('호!');
  }
});

client.login('ODg3OTQxMTg3OTg4NzgzMTU0.YULdrA.q4tQuAEubtlnKir5H_rCITI_YbY');
