from json import loads
from os import makedirs
from os.path import expanduser, join, isdir
from subprocess import call
from urlparse import parse_qs

BACKUP_ROOT = expanduser( '~/scm/bitbucket' )  # change this according to your server setup

def application( environ, start_response ):
	headers = [ ( 'Content-type', 'text/plain' ) ]
	try:
		length = int( environ[ 'CONTENT_LENGTH' ] )
		post = parse_qs( environ[ 'wsgi.input' ].read( length ), True )
		data = loads( post[ 'payload' ][ 0 ] )
		repository = data[ 'repository' ]
		repo = repository[ 'slug' ]
		owner = repository[ 'owner' ]
		owner_dir = join( BACKUP_ROOT, owner )
		repo_dest = join( owner_dir, repo )
		if not isdir( repo_dest ):
			if not isdir( owner_dir ): makedirs( owner_dir, 0700 )
			call([ 'hg', 'clone', '-U', 'https://{0}@bitbucket.org/{0}/{1}'.format( owner, repo ), repo_dest ])
		else:
			call([ 'hg', '-R', repo_dest, 'pull' ])
	except:
		start_response( '500 Internal server error', headers )
		return [ "Internal server error" ]
	else:
		start_response( '200 OK', headers )
		return [ "OK" ]
