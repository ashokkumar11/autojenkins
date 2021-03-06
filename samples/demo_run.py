from datetime import datetime

from autojenkins import Jenkins


if __name__ == '__main__':
    j = Jenkins('https://builds.apache.org')
    jobs = j.all_jobs()
    print(jobs)
    for job, color in jobs:
        if color in ['red', 'blue', 'yellow']:
            full_info = j.job_info(job)
            last_build = j.last_build_info(job)
            when = datetime.fromtimestamp(last_build['timestamp'] / 1000)
        else:
            when = '(unknown)'
        print("{0!s:<19} {1:<6} {2}".format(when, color, job))
