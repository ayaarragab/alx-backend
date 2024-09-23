import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server: ERROR_MESSAGE', err));
client.on('connect', () => console.log('Redis client connected to the server'));
await client.connect();
const channel = 'holberton school channel';

client.subscribe(channel, (message, channel) => {
    console.log(`Received message: ${message} on channel: ${channel}`);
    if (message === 'KILL_SERVER') {
        client.unsubscribe(channel);
        client.quit();
    }
});
