#!/usr/bin/python
import bobo

@bobo.query('/')
def index():
	return """<html><head><title>Brother QL-580N wrapper by Matthias Bock</title></head><body bgcolor=blue>
	<center>
	<br/>
	<h1>Brother QL-580N</h1>
    <hr />
    <form action='/print' method=post>
	<textarea rows=5 name=text>Text</textarea>
	<br/>
	<input type=submit value=Print />
	</form>
    </body></html>
    """

@bobo.post('/print')
def lp(bobo_request, text):
	from subprocess import Popen
	from shlex import split
	open('tempfile','w').write('\n'+text.encode('ascii', 'replace'))
	Popen(split('lp tempfile -d Brother_QL-580N')).wait()
	return bobo.redirect('/printed')

@bobo.query('/printed')
def printed():
	return "OK. Sent to printer. <a href='/'>Print more</a>"

