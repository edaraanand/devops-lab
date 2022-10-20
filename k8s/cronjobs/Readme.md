Minutes (0-59), Hours(0-23), Days(1-31), Month(1-12), Day of the month (0-6)

M
*/5  - Every 5 minutes - 12am.5m, 1am.5m, 2am.5m

H
*/2 - Every two hours - 0am, 2am, 4am

D
*/2 - Every 2 Days

Month
*/3 - Every 3 months

Day
1,3 - Monday, Wednesday

Its almost same like Linux/Unix Cronjob

Whatever we mention in the image gets run based on the schedule what we set

We can have multiple jobs at the same time and set concurrency 

If we wanted to run a specific job, mention the time in UTC time not in others

We can set the limit on the number of jobs at the same time.

We can see the successful jobs history and failed/barren jobs history 
SuccesfullJobHistoryLimit 3
Failedjobhistorylimit 1

Deleting cronjobs  - Kcal delete cronjob jobname - Make sure its delete

Describe 
	Last 3 successful jobs, 3 failed jobs


Suspending the cronjobs - 
	It doesn’t touch the current jobs but not create future jobs
	suspend: true
	Force apply if jobs exists already - No new jobs 
	suspend: false

Kcal patch cronjob hello-world-cron -p {spec: {suspend: false}}

Concurrency (Allow, Forbid, Replace)
	Default - Allow - There is a job running or in progress and which is taking long time and then it allows a new job
	Forbid - Don’t schedule new job - when job is running
	Replace - If first job is taking long time and then replaces it

It keeps last 3 pods and jobs - Default
SuccesfullJobHistoryLimit 3
Failedjobhistorylimit 1