createPushNotificationsJobs = (jobs, queue) => {
    if (!typeof jobs === 'object')
        throw new Error('Jobs is not an array');
    for (const job of jobs) {
        const job_ = queue.create('push_notification_code_2', job);
        job_.on('complete', () => console.log(`Notification job ${job_.id} completed`));
        job_.on('failed', () => console.log(`Notification job ${job_.id} failed`));
        job_.progress('failed', () => console.log(`Notification job ${job_.id} failed`));
        job_.on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% completed`));
    }
}
