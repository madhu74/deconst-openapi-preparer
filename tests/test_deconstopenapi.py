#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
test_deconstopenapi
----------------------------------
Tests for `deconstopenapi` module.
'''

import unittest
import subprocess
import sys
import os
import json
from unittest import mock
from os import path
from bs4 import BeautifulSoup

sys.path.append(path.join(path.dirname(__file__), '..'))

from openapipreparer.deconstopenapi import enveloper
from openapipreparer.deconstopenapi import submit
from openapipreparer.deconstopenapi import find_all
from openapipreparer.config import Configuration
import json

class DeconstOPENAPITestCase(unittest.TestCase):
    '''
    Tests for the deconstraml methods
    '''

    def test_enveloper_pass(self):
        '''
        Does the enveloper link things together properly?
        '''
        self.maxDiff = None
        openapi_location = path.join(
            os.getcwd(), 'tests', 'src', 'openapi.json')
        html_location = path.join(
            os.getcwd(), 'tests', 'dest')
        actual_result = enveloper(openapi_location, html_location)
        # print("Test")
        # data =str(actual_result)
        # print(data.encode('utf-8', "strict").decode('utf-8', "strict"))
        # print("Test")
        expected_result = {
        'body': '\n<h1>Swagger Petstore</h1>\n<div class="app-desc">No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)</div>\n<div class="app-desc">More information: <a href="https://helloreverb.com">https://helloreverb.com</a></div>\n<div class="app-desc">Contact Info: <a href="hello@helloreverb.com">hello@helloreverb.com</a></div>\n<div class="app-desc">Version: 1.0.0</div>\n<div class="app-desc">BasePath:/v1</div>\n<div class="license-info">MIT</div>\n<div class="license-url">http://apache.org/licenses/LICENSE-2.0.html</div>\n<h2>Access</h2>\n<h2><a name="__Methods">Methods</a></h2>\n  [ Jump to <a href="#__Models">Models</a> ]\n\n  <h3>Table of Contents </h3>\n<div class="method-summary"></div>\n<h4><a href="#Pets">Pets</a></h4>\n<ul>\n<li><a href="#createPets"><code><span class="http-method">post</span> /pets</code></a></li>\n<li><a href="#listPets"><code><span class="http-method">get</span> /pets</code></a></li>\n<li><a href="#showPetById"><code><span class="http-method">get</span> /pets/{petId}</code></a></li>\n</ul>\n<h1><a name="Pets">Pets</a></h1>\n<div class="method"><a name="createPets"></a>\n<div class="method-path">\n<a class="up" href="#__Methods">Up</a>\n<pre class="post"><code class="huge"><span class="http-method">post</span> /pets</code></pre></div>\n<div class="method-summary">Create a pet (<span class="nickname">createPets</span>)</div>\n<div class="method-notes"></div>\n<!--Todo: process Response Object and its headers, schema, examples -->\n<h3 class="field-label">Produces</h3>\n    This API call produces the following media types according to the <span class="header">Accept</span> request header;\n    the media type will be conveyed by the <span class="header">Content-Type</span> response header.\n    <ul>\n<li><code>application/json</code></li>\n</ul>\n<h3 class="field-label">Responses</h3>\n<h4 class="field-label">201</h4>\n    Null response\n        <a href="#"></a>\n<h4 class="field-label">default</h4>\n    unexpected error\n        <a href="#Error">Error</a>\n</div> <!-- method -->\n<hr/>\n<div class="method"><a name="listPets"></a>\n<div class="method-path">\n<a class="up" href="#__Methods">Up</a>\n<pre class="get"><code class="huge"><span class="http-method">get</span> /pets</code></pre></div>\n<div class="method-summary">List all pets (<span class="nickname">listPets</span>)</div>\n<div class="method-notes"></div>\n<h3 class="field-label">Query parameters</h3>\n<div class="field-items">\n<div class="param">limit (optional)</div>\n<div class="param-desc"><span class="param-type">Query Parameter</span> — How many items to return at one time max 100 format: int32</div>\n</div> <!-- field-items -->\n<h3 class="field-label">Return type</h3>\n<div class="return-type">\n<a href="#Pets">Pets</a>\n</div>\n<!--Todo: process Response Object and its headers, schema, examples -->\n<h3 class="field-label">Example data</h3>\n<div class="example-data-content-type">Content-Type: application/json</div>\n<pre class="example"><code>null</code></pre>\n<h3 class="field-label">Produces</h3>\n    This API call produces the following media types according to the <span class="header">Accept</span> request header;\n    the media type will be conveyed by the <span class="header">Content-Type</span> response header.\n    <ul>\n<li><code>application/json</code></li>\n</ul>\n<h3 class="field-label">Responses</h3>\n<h4 class="field-label">200</h4>\n    An paged array of pets\n        <a href="#Pets">Pets</a>\n<h4 class="field-label">default</h4>\n    unexpected error\n        <a href="#Error">Error</a>\n</div> <!-- method -->\n<hr/>\n<div class="method"><a name="showPetById"></a>\n<div class="method-path">\n<a class="up" href="#__Methods">Up</a>\n<pre class="get"><code class="huge"><span class="http-method">get</span> /pets/{petId}</code></pre></div>\n<div class="method-summary">Info for a specific pet (<span class="nickname">showPetById</span>)</div>\n<div class="method-notes"></div>\n<h3 class="field-label">Path parameters</h3>\n<div class="field-items">\n<div class="param">petId (required)</div>\n<div class="param-desc"><span class="param-type">Path Parameter</span> — The id of the pet to retrieve </div>\n</div> <!-- field-items -->\n<h3 class="field-label">Return type</h3>\n<div class="return-type">\n<a href="#Pets">Pets</a>\n</div>\n<!--Todo: process Response Object and its headers, schema, examples -->\n<h3 class="field-label">Example data</h3>\n<div class="example-data-content-type">Content-Type: application/json</div>\n<pre class="example"><code>null</code></pre>\n<h3 class="field-label">Produces</h3>\n    This API call produces the following media types according to the <span class="header">Accept</span> request header;\n    the media type will be conveyed by the <span class="header">Content-Type</span> response header.\n    <ul>\n<li><code>application/json</code></li>\n</ul>\n<h3 class="field-label">Responses</h3>\n<h4 class="field-label">200</h4>\n    Expected response to a valid request\n        <a href="#Pets">Pets</a>\n<h4 class="field-label">default</h4>\n    unexpected error\n        <a href="#Error">Error</a>\n</div> <!-- method -->\n<hr/>\n<h2><a name="__Models">Models</a></h2>\n  [ Jump to <a href="#__Methods">Methods</a> ]\n\n  <h3>Table of Contents</h3>\n<ol>\n<li><a href="#Error"><code>Error</code> - </a></li>\n<li><a href="#Pet"><code>Pet</code> - </a></li>\n<li><a href="#Pets"><code>Pets</code> - </a></li>\n</ol>\n<div class="model">\n<h3><a name="Error"><code>Error</code> - </a> <a class="up" href="#__Models">Up</a></h3>\n<div class="model-description"></div>\n<div class="field-items">\n<div class="param">code </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  format: int32</div>\n<div class="param">message </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span> </div>\n</div> <!-- field-items -->\n</div>\n<div class="model">\n<h3><a name="Pet"><code>Pet</code> - </a> <a class="up" href="#__Models">Up</a></h3>\n<div class="model-description"></div>\n<div class="field-items">\n<div class="param">id </div><div class="param-desc"><span class="param-type"><a href="#long">Long</a></span>  format: int64</div>\n<div class="param">name </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span> </div>\n<div class="param">tag (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span> </div>\n</div> <!-- field-items -->\n</div>\n<div class="model">\n<h3><a name="Pets"><code>Pets</code> - </a> <a class="up" href="#__Models">Up</a></h3>\n<div class="model-description"></div>\n<div class="field-items">\n</div> <!-- field-items -->\n</div>\n',
        'docname': str(path.join(html_location,"index.html")),
        'title': 'Swagger Petstore',
        'toc': '<ul><li><a href="#Access">Access</a></li><li><a href="#Methods">Methods</a></li><ul><li><a href="#TableofContents">Table of Contents </a></li><ul><li><a href="#Pets">Pets</a></li></ul></ul><ul><li><a href="#201">201</a></li><li><a href="#default">default</a></li></ul><ul><li><a href="#200">200</a></li><li><a href="#default">default</a></li></ul><ul><li><a href="#200">200</a></li><li><a href="#default">default</a></li></ul><li><a href="#Models">Models</a></li><ul><li><a href="#TableofContents">Table of Contents</a></li></ul><ul><li><a href="#Error----Up"></a></li></ul><ul><li><a href="#Pet----Up"></a></li></ul><ul><li><a href="#Pets----Up"></a></li></ul></ul>',
        'unsearchable': None,
        'content_id': str(path.join(html_location,"index.html")),
        'meta': {
            'someKey': 'someValue',
            'preferGithubIssues': True,
            'github_issues_url': 'https://github.com/deconst/fake-repo/issues',
            'github_edit_url': 'https://github.com/deconst/fake-repo/edit/master/tests/dest/test_is_html/index.html'
        },
        'asset_offsets': {},
        'addenda': None,
        'per_page_meta': {}}
        self.assertEqual(actual_result, expected_result)
    
    def test_submit_pass(self):
        '''
        Does the submit method pass the json properly?
        '''
        config = Configuration(os.environ)
        self.maxDiff = None
        the_envelope_passed = {
            'body': '\n<h1>Swagger Petstore</h1>\n<div class="app-desc">No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)</div>\n<div class="app-desc">More information: <a href="https://helloreverb.com">https://helloreverb.com</a></div>\n<div class="app-desc">Contact Info: <a href="hello@helloreverb.com">hello@helloreverb.com</a></div>\n<div class="app-desc">Version: 1.0.0</div>\n<div class="app-desc">BasePath:/v1</div>\n<div class="license-info">MIT</div>\n<div class="license-url">http://apache.org/licenses/LICENSE-2.0.html</div>\n<h2>Access</h2>\n<h2><a name="__Methods">Methods</a></h2>\n  [ Jump to <a href="#__Models">Models</a> ]\n\n  <h3>Table of Contents </h3>\n<div class="method-summary"></div>\n<h4><a href="#Pets">Pets</a></h4>\n<ul>\n<li><a href="#createPets"><code><span class="http-method">post</span> /pets</code></a></li>\n<li><a href="#listPets"><code><span class="http-method">get</span> /pets</code></a></li>\n<li><a href="#showPetById"><code><span class="http-method">get</span> /pets/{petId}</code></a></li>\n</ul>\n<h1><a name="Pets">Pets</a></h1>\n<div class="method"><a name="createPets"></a>\n<div class="method-path">\n<a class="up" href="#__Methods">Up</a>\n<pre class="post"><code class="huge"><span class="http-method">post</span> /pets</code></pre></div>\n<div class="method-summary">Create a pet (<span class="nickname">createPets</span>)</div>\n<div class="method-notes"></div>\n<!--Todo: process Response Object and its headers, schema, examples -->\n<h3 class="field-label">Produces</h3>\n    This API call produces the following media types according to the <span class="header">Accept</span> request header;\n    the media type will be conveyed by the <span class="header">Content-Type</span> response header.\n    <ul>\n<li><code>application/json</code></li>\n</ul>\n<h3 class="field-label">Responses</h3>\n<h4 class="field-label">201</h4>\n    Null response\n        <a href="#"></a>\n<h4 class="field-label">default</h4>\n    unexpected error\n        <a href="#Error">Error</a>\n</div> <!-- method -->\n<hr/>\n<div class="method"><a name="listPets"></a>\n<div class="method-path">\n<a class="up" href="#__Methods">Up</a>\n<pre class="get"><code class="huge"><span class="http-method">get</span> /pets</code></pre></div>\n<div class="method-summary">List all pets (<span class="nickname">listPets</span>)</div>\n<div class="method-notes"></div>\n<h3 class="field-label">Query parameters</h3>\n<div class="field-items">\n<div class="param">limit (optional)</div>\n<div class="param-desc"><span class="param-type">Query Parameter</span> — How many items to return at one time max 100 format: int32</div>\n</div> <!-- field-items -->\n<h3 class="field-label">Return type</h3>\n<div class="return-type">\n<a href="#Pets">Pets</a>\n</div>\n<!--Todo: process Response Object and its headers, schema, examples -->\n<h3 class="field-label">Example data</h3>\n<div class="example-data-content-type">Content-Type: application/json</div>\n<pre class="example"><code>null</code></pre>\n<h3 class="field-label">Produces</h3>\n    This API call produces the following media types according to the <span class="header">Accept</span> request header;\n    the media type will be conveyed by the <span class="header">Content-Type</span> response header.\n    <ul>\n<li><code>application/json</code></li>\n</ul>\n<h3 class="field-label">Responses</h3>\n<h4 class="field-label">200</h4>\n    An paged array of pets\n        <a href="#Pets">Pets</a>\n<h4 class="field-label">default</h4>\n    unexpected error\n        <a href="#Error">Error</a>\n</div> <!-- method -->\n<hr/>\n<div class="method"><a name="showPetById"></a>\n<div class="method-path">\n<a class="up" href="#__Methods">Up</a>\n<pre class="get"><code class="huge"><span class="http-method">get</span> /pets/{petId}</code></pre></div>\n<div class="method-summary">Info for a specific pet (<span class="nickname">showPetById</span>)</div>\n<div class="method-notes"></div>\n<h3 class="field-label">Path parameters</h3>\n<div class="field-items">\n<div class="param">petId (required)</div>\n<div class="param-desc"><span class="param-type">Path Parameter</span> — The id of the pet to retrieve </div>\n</div> <!-- field-items -->\n<h3 class="field-label">Return type</h3>\n<div class="return-type">\n<a href="#Pets">Pets</a>\n</div>\n<!--Todo: process Response Object and its headers, schema, examples -->\n<h3 class="field-label">Example data</h3>\n<div class="example-data-content-type">Content-Type: application/json</div>\n<pre class="example"><code>null</code></pre>\n<h3 class="field-label">Produces</h3>\n    This API call produces the following media types according to the <span class="header">Accept</span> request header;\n    the media type will be conveyed by the <span class="header">Content-Type</span> response header.\n    <ul>\n<li><code>application/json</code></li>\n</ul>\n<h3 class="field-label">Responses</h3>\n<h4 class="field-label">200</h4>\n    Expected response to a valid request\n        <a href="#Pets">Pets</a>\n<h4 class="field-label">default</h4>\n    unexpected error\n        <a href="#Error">Error</a>\n</div> <!-- method -->\n<hr/>\n<h2><a name="__Models">Models</a></h2>\n  [ Jump to <a href="#__Methods">Methods</a> ]\n\n  <h3>Table of Contents</h3>\n<ol>\n<li><a href="#Error"><code>Error</code> - </a></li>\n<li><a href="#Pet"><code>Pet</code> - </a></li>\n<li><a href="#Pets"><code>Pets</code> - </a></li>\n</ol>\n<div class="model">\n<h3><a name="Error"><code>Error</code> - </a> <a class="up" href="#__Models">Up</a></h3>\n<div class="model-description"></div>\n<div class="field-items">\n<div class="param">code </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  format: int32</div>\n<div class="param">message </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span> </div>\n</div> <!-- field-items -->\n</div>\n<div class="model">\n<h3><a name="Pet"><code>Pet</code> - </a> <a class="up" href="#__Models">Up</a></h3>\n<div class="model-description"></div>\n<div class="field-items">\n<div class="param">id </div><div class="param-desc"><span class="param-type"><a href="#long">Long</a></span>  format: int64</div>\n<div class="param">name </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span> </div>\n<div class="param">tag (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span> </div>\n</div> <!-- field-items -->\n</div>\n<div class="model">\n<h3><a name="Pets"><code>Pets</code> - </a> <a class="up" href="#__Models">Up</a></h3>\n<div class="model-description"></div>\n<div class="field-items">\n</div> <!-- field-items -->\n</div>\n',
            'docname': "fake_content_id",
            'title': 'Swagger Petstore',
            'toc': '<ul><li><a href="#Access">Access</a></li><li><a href="#Methods">Methods</a></li><ul><li><a href="#TableofContents">Table of Contents </a></li><ul><li><a href="#Pets">Pets</a></li></ul></ul><ul><li><a href="#201">201</a></li><li><a href="#default">default</a></li></ul><ul><li><a href="#200">200</a></li><li><a href="#default">default</a></li></ul><ul><li><a href="#200">200</a></li><li><a href="#default">default</a></li></ul><li><a href="#Models">Models</a></li><ul><li><a href="#TableofContents">Table of Contents</a></li></ul><ul><li><a href="#Error----Up"></a></li></ul><ul><li><a href="#Pet----Up"></a></li></ul><ul><li><a href="#Pets----Up"></a></li></ul></ul>',
            'unsearchable': None,
            'content_id': "fake_content_id",
            'meta': {
                'someKey': 'someValue',
                'preferGithubIssues': True,
                'github_issues_url': 'https://github.com/deconst/fake-repo/issues',
                'github_edit_url': 'https://github.com/deconst/fake-repo/edit/master/tests/dest/index.html'
            },
            'asset_offsets': {},
            'addenda': None,
            'per_page_meta': {}}
        dest_path = submit(the_envelope_passed)
        with open(dest_path, 'r') as written_file:
            actual_file = json.load(written_file)
        fake_json_envelope = os.path.join(
            os.getcwd(), 'tests', 'src', 'input_file_writeout.json')
        with open(fake_json_envelope, 'r') as fake_envelope:
            expected_json_output = json.load(fake_envelope)
        self.assertEqual(actual_file, expected_json_output)

    def test_find_all_pass(self):
        '''
        Does the find_all method really find all the openapi it can?
        '''
        config_file = Configuration(os.environ)
        actual_list = find_all(config_file)
        expected_list = [os.path.join(os.getcwd(), 'tests', 'src', 'openapi.json'),
            os.path.join(os.getcwd(), 'tests', 'src','small_test', 'openapi.json')]
        self.assertEqual(actual_list, expected_list)
# 
# 
if __name__ == '__main__':
    unittest.main()
