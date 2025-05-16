import click
import datetime
import time
import subprocess
import os

@click.command()
@click.option('--name', prompt='What is your name')
@click.option('--age', prompt='What is your age')
@click.option('--sex', prompt='What is your sex (enter male or female)')
@click.option('--birthplace', prompt='What is your birthplace (enter your native place)')
@click.option('--occupation', prompt='What is your occupation (working or non-working)')
@click.option('--married_status', prompt='Are you married (say married or un-married)')
@click.option('--playbook', prompt='Do you want to run ansible playbook now (say yes or no)')
def main(name, age, sex, birthplace, occupation, married_status, playbook):
    clock_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    click.echo(f"Script executed at: {clock_now}\n")
    click.echo("The 'click' module is used to build command-line interfaces.")
    click.echo("It helps create CLI tools and handles argument parsing.\n")
    click.echo(f"Your good name is: {name}")
    click.echo(f"Your age is: {age}")
    click.echo(f"Your sex is: {sex}")
    click.echo(f"Your birthplace is: {birthplace}")
    click.echo(f"Your occupation is: {occupation}")
    click.echo(f"Your married_status is: {married_status}")
    time.sleep(2)
    click.echo("\nGoing to run a simple Ansible playbook now...")
    if playbook.lower() == 'yes':
        playbook_path = os.path.join(os.getcwd(), 'ping.yaml')
        click.echo("Running Ansible playbook shortly...")
        subprocess.run(['ansible-playbook', playbook_path])
    else:
        click.echo("Playbook execution skipped.")

if __name__ == '__main__':
    main()
