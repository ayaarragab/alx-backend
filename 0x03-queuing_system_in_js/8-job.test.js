import { createQueue } from 'kue';
import createPushNotificationsJobs from './8-job';
import { expect } from 'chai';

describe('createPushNotificationsJobs', () => {
    let queue;

    beforeEach(() => {
        queue = createQueue();
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('should create jobs in the queue', () => {
        const jobs = [
            {
                phoneNumber: '1234567890',
                message: 'This is a test message'
            },
            {
                phoneNumber: '0987654321',
                message: 'This is another test message'
            }
        ];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
    });

    it('should throw an error if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
    });
});
