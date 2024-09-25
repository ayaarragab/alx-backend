import kue from 'kue'
const queue = kue.createQueue();

const blacklisted = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    },
    {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
    }
]

const sendNotification = (phoneNumber, message, job, done) => {
    job.progress(0, 100);

    const isBlacklisted = blacklisted.some(entry => entry.phoneNumber === phoneNumber);
    if (isBlacklisted)
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}
