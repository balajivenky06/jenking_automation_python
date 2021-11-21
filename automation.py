from os import environ
import click
from jenkins import Jenkins

token = environ["JENKINS_TOKEN"]
user = environ["JENKINS_USER"]
url = environ["JENKINS_URL"]

@click.command
@click.argument("job", type=click.STRING)
def main(job):
    conn = Jenkins(username=user, password=token, url=url)
    result = conn.build_job(job)
    print(f"Triggered job {job} with build number {result}")
    
if __name__ == "__main__":
    main()

#use export command to set values for token, user, url
#pip install click

