import click

users_list = []
comments_list = []

# if the user is logged in, this is where
#  they will be stored for reference
session = dict(current_user=None)

@click.group()
def cli():
    pass

def create_user():
    pass

@cli.command()
def view_users():
    pass


@cli.command()
def register(username, password, role):
    pass

@cli.command()
def login():
    pass


@cli.command()
def comment():
    pass


@cli.command()
def view_comments():
    pass


@cli.command()
@click.argument(comment_id)
def delete(comment_id):
    for a_comment in comments_list[:]:
        if a_comment['id'] == comment_id:
            comments_list.remove(a_comment)
            click.echo('Comment deleted successfully...')
            return
    else:
        click.echo('Comment not found!')
        return

if __name__ == '__main__':
    cli()
