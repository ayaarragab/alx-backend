import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server: ERROR_MESSAGE', err));

client.on('connect', () => console.log('Redis client connected to the server'));

await client.connect();

client.hSet('HolbertonSchools', 'Portland', 50, redis.print);
client.hSet('HolbertonSchools', 'Seattle', 80, redis.print);
client.hSet('HolbertonSchools', 'New York', 20, redis.print);
client.hSet('HolbertonSchools', 'Bogota', 20, redis.print);
client.hSet('HolbertonSchools', 'Cali', 40, redis.print);
client.hSet('HolbertonSchools', 'Paris', 2, redis.print);

await client.hGetAll(HolbertonSchools);
