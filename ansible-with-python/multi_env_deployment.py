import click
import datetime
import os
import subprocess

@click.command()
@click.option('--playbook', prompt='Do you want to run the deployment now (enter yes or no)')
@click.option('--env', prompt='Select the environment you want to run the deployment (enter dev, qa, prod)')
@click.option('--cr', prompt='Enter the Change Number please (starts with CHG023456)')
def deployment(playbook, env, cr):
    clock_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    click.echo(f"\nScript executed time at: {clock_now}\n")
    click.echo(f"\nYour selection on deployment is: {playbook}\n")
    click.echo(f"\nEnvironment name is: {env}\n")
    click.echo(f"\nChange Number is: {cr}\n")
    if playbook.lower() == 'go-ahead':
        if env.lower() == 'dev':
            playbook_path = os.path.join(os.getcwd(), 'dev.yaml')
            click.echo("DEV deployment will start shortly...")
            subprocess.run(['ansible-playbook', playbook_path])
        elif env.lower() == 'qa':
            playbook_path = os.path.join(os.getcwd(), 'qa.yaml')
            click.echo("QA deployment will start shortly...")
            subprocess.run(['ansible-playbook', playbook_path])
        elif env.lower() == 'prod':
            playbook_path = os.path.join(os.getcwd(), 'prod.yaml')
            click.echo("PROD deployment will start shortly...")
            subprocess.run(['ansible-playbook', playbook_path])
        else:
            click.echo("Deployment execution skipped due to wrong environment selection.")
            return
    else:
        click.echo("Playbook execution skipped.")

if __name__ == '__main__':
    deployment()
