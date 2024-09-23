import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server: ERROR_MESSAGE', err));

client.on('connect', () => console.log('Redis client connected to the server'));

await client.connect();

const setNewSchool = async (schoolName, value) => {
    await client.set(schoolName, value);
}

const displaySchoolValue = async (schoolName) => {
    await client.get(schoolName);
}

console.log(displaySchoolValue('Holberton'));
console.log(setNewSchool('HolbertonSanFrancisco', '100'));
console.log(displaySchoolValue('HolbertonSanFrancisco'));
