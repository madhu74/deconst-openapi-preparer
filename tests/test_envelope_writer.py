# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
test_envelope_writer
----------------------------------
Tests for `envelope_writer` module.
'''

import unittest
import subprocess
import sys
import os
import json
import filecmp
from os import path
from bs4 import BeautifulSoup
from unittest import mock

sys.path.append(path.join(path.dirname(__file__), '..'))

from openapipreparer.builders.envelope_writer import make_it_html
from openapipreparer.builders.envelope_writer import parsing_html
from openapipreparer.builders.envelope_writer import write_out
from openapipreparer.builders.envelope_writer import Envelope_OPENAPI


class EnvelopeWriterTestCase(unittest.TestCase):
    '''
    Tests for the envelope_writer methods
    '''

    def test_make_it_html_pass(self):
        '''
        Does the method post to the correct file?
        '''
        openapi_location = path.join(
            os.getcwd(), 'tests', 'src', 'small_test','openapi.json')
        html_location = path.join(
            os.getcwd(), 'tests', 'dest', 'test_make_it')
        expected_html_file = path.join(
            os.getcwd(), 'tests', 'src', 'tested_html.html')
        test_case_1 = make_it_html(openapi_location, html_location)
        html_location = os.path.join(html_location,"index.html")
        self.assertTrue(filecmp.cmp(html_location, expected_html_file),
                        'These two files are not equal.')

    def test_parsing_html_pass(self):
        '''
        Question?
        '''
        self.maxDiff = None
        the_html = path.join(os.getcwd(), 'tests', 'src', 'tested_html.html')
        parsed_html = parsing_html(the_html, page_title='fake_title')        
        expected_result = {
                "body": '\n<h1>Swagger Petstore</h1>\n<div class="app-desc">A sample API that uses a petstore as an example to demonstrate features in the swagger-2.0 specification</div>\n<div class="app-desc">More information: <a href="https://helloreverb.com">https://helloreverb.com</a></div>\n<div class="app-desc">Contact Info: <a href="hello@helloreverb.com">hello@helloreverb.com</a></div>\n<div class="app-desc">Version: 1.0.0</div>\n<div class="app-desc">BasePath:/api</div>\n<div class="license-info">MIT</div>\n<div class="license-url">http://apache.org/licenses/LICENSE-2.0.html</div>\n<h2>Access</h2>\n<h2><a name="__Methods">Methods</a></h2>\n  [ Jump to <a href="#__Models">Models</a> ]\n\n  <h3>Table of Contents </h3>\n<div class="method-summary"></div>\n<h4><a href="#Default">Default</a></h4>\n<ul>\n<li><a href="#petsGet"><code><span class="http-method">get</span> /pets</code></a></li>\n</ul>\n<h1><a name="Default">Default</a></h1>\n<div class="method"><a name="petsGet"></a>\n<div class="method-path">\n<a class="up" href="#__Methods">Up</a>\n<pre class="get"><code class="huge"><span class="http-method">get</span> /pets</code></pre></div>\n<div class="method-summary"> (<span class="nickname">petsGet</span>)</div>\n<div class="method-notes">Returns all pets from the system that the user has access to</div>\n<h3 class="field-label">Return type</h3>\n<div class="return-type">\n      array[<a href="#Pet">Pet</a>]\n      \n    </div>\n<!--Todo: process Response Object and its headers, schema, examples -->\n<h3 class="field-label">Example data</h3>\n<div class="example-data-content-type">Content-Type: application/json</div>\n<pre class="example"><code>{\n  "name" : "name",\n  "id" : 0,\n  "tag" : "tag"\n}</code></pre>\n<h3 class="field-label">Produces</h3>\n    This API call produces the following media types according to the <span class="header">Accept</span> request header;\n    the media type will be conveyed by the <span class="header">Content-Type</span> response header.\n    <ul>\n<li><code>application/json</code></li>\n</ul>\n<h3 class="field-label">Responses</h3>\n<h4 class="field-label">200</h4>\n    A list of pets.\n        \n  </div> <!-- method -->\n<hr/>\n<h2><a name="__Models">Models</a></h2>\n  [ Jump to <a href="#__Methods">Methods</a> ]\n\n  <h3>Table of Contents</h3>\n<ol>\n<li><a href="#Pet"><code>Pet</code> - </a></li>\n</ol>\n<div class="model">\n<h3><a name="Pet"><code>Pet</code> - </a> <a class="up" href="#__Models">Up</a></h3>\n<div class="model-description"></div>\n<div class="field-items">\n<div class="param">id </div><div class="param-desc"><span class="param-type"><a href="#long">Long</a></span>  format: int64</div>\n<div class="param">name </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span> </div>\n<div class="param">tag (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span> </div>\n</div> <!-- field-items -->\n</div>\n',
                "docname": str(the_html),
                "title": 'fake_title',
                "toc": '<ul><li><a href="#Access">Access</a></li><li><a href="#Methods">Methods</a></li><ul><li><a href="#TableofContents">Table of Contents </a></li><ul><li><a href="#Default">Default</a></li></ul></ul><ul><li><a href="#200">200</a></li></ul><li><a href="#Models">Models</a></li><ul><li><a href="#TableofContents">Table of Contents</a></li></ul><ul><li><a href="#Pet----Up"></a></li></ul></ul>',
                "unsearchable": None,
                "content_id": str(the_html),
                "meta": {
                    "someKey": 'someValue',
                    "preferGithubIssues": True,
                    "github_issues_url": 'https://github.com/deconst/fake-repo/issues',
                    "github_edit_url": 'https://github.com/deconst/fake-repo/edit/master/tests/src/tested_html.html'
                },
                "asset_offsets": {},
                "addenda": None,
                "per_page_meta": {}}
        self.assertEqual(parsed_html, expected_result)

    def test_write_out_pass(self):
        '''
        Does the file write out properly?
        '''
        self.maxDiff = None
        the_envelope_passed = {
            "body": '\n<h1>Swagger Petstore</h1>\n<div class="app-desc">No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)</div>\n<div class="app-desc">More information: <a href="https://helloreverb.com">https://helloreverb.com</a></div>\n<div class="app-desc">Contact Info: <a href="hello@helloreverb.com">hello@helloreverb.com</a></div>\n<div class="app-desc">Version: 1.0.0</div>\n<div class="app-desc">BasePath:/v1</div>\n<div class="license-info">MIT</div>\n<div class="license-url">http://apache.org/licenses/LICENSE-2.0.html</div>\n<h2>Access</h2>\n<h2><a name="__Methods">Methods</a></h2>\n  [ Jump to <a href="#__Models">Models</a> ]\n\n  <h3>Table of Contents </h3>\n<div class="method-summary"></div>\n<h4><a href="#Pets">Pets</a></h4>\n<ul>\n<li><a href="#createPets"><code><span class="http-method">post</span> /pets</code></a></li>\n<li><a href="#listPets"><code><span class="http-method">get</span> /pets</code></a></li>\n<li><a href="#showPetById"><code><span class="http-method">get</span> /pets/{petId}</code></a></li>\n</ul>\n<h1><a name="Pets">Pets</a></h1>\n<div class="method"><a name="createPets"></a>\n<div class="method-path">\n<a class="up" href="#__Methods">Up</a>\n<pre class="post"><code class="huge"><span class="http-method">post</span> /pets</code></pre></div>\n<div class="method-summary">Create a pet (<span class="nickname">createPets</span>)</div>\n<div class="method-notes"></div>\n<!--Todo: process Response Object and its headers, schema, examples -->\n<h3 class="field-label">Produces</h3>\n    This API call produces the following media types according to the <span class="header">Accept</span> request header;\n    the media type will be conveyed by the <span class="header">Content-Type</span> response header.\n    <ul>\n<li><code>application/json</code></li>\n</ul>\n<h3 class="field-label">Responses</h3>\n<h4 class="field-label">201</h4>\n    Null response\n        <a href="#"></a>\n<h4 class="field-label">default</h4>\n    unexpected error\n        <a href="#Error">Error</a>\n</div> <!-- method -->\n<hr/>\n<div class="method"><a name="listPets"></a>\n<div class="method-path">\n<a class="up" href="#__Methods">Up</a>\n<pre class="get"><code class="huge"><span class="http-method">get</span> /pets</code></pre></div>\n<div class="method-summary">List all pets (<span class="nickname">listPets</span>)</div>\n<div class="method-notes"></div>\n<h3 class="field-label">Query parameters</h3>\n<div class="field-items">\n<div class="param">limit (optional)</div>\n<div class="param-desc"><span class="param-type">Query Parameter</span> — How many items to return at one time max 100 format: int32</div>\n</div> <!-- field-items -->\n<h3 class="field-label">Return type</h3>\n<div class="return-type">\n<a href="#Pets">Pets</a>\n</div>\n<!--Todo: process Response Object and its headers, schema, examples -->\n<h3 class="field-label">Example data</h3>\n<div class="example-data-content-type">Content-Type: application/json</div>\n<pre class="example"><code>null</code></pre>\n<h3 class="field-label">Produces</h3>\n    This API call produces the following media types according to the <span class="header">Accept</span> request header;\n    the media type will be conveyed by the <span class="header">Content-Type</span> response header.\n    <ul>\n<li><code>application/json</code></li>\n</ul>\n<h3 class="field-label">Responses</h3>\n<h4 class="field-label">200</h4>\n    An paged array of pets\n        <a href="#Pets">Pets</a>\n<h4 class="field-label">default</h4>\n    unexpected error\n        <a href="#Error">Error</a>\n</div> <!-- method -->\n<hr/>\n<div class="method"><a name="showPetById"></a>\n<div class="method-path">\n<a class="up" href="#__Methods">Up</a>\n<pre class="get"><code class="huge"><span class="http-method">get</span> /pets/{petId}</code></pre></div>\n<div class="method-summary">Info for a specific pet (<span class="nickname">showPetById</span>)</div>\n<div class="method-notes"></div>\n<h3 class="field-label">Path parameters</h3>\n<div class="field-items">\n<div class="param">petId (required)</div>\n<div class="param-desc"><span class="param-type">Path Parameter</span> — The id of the pet to retrieve </div>\n</div> <!-- field-items -->\n<h3 class="field-label">Return type</h3>\n<div class="return-type">\n<a href="#Pets">Pets</a>\n</div>\n<!--Todo: process Response Object and its headers, schema, examples -->\n<h3 class="field-label">Example data</h3>\n<div class="example-data-content-type">Content-Type: application/json</div>\n<pre class="example"><code>null</code></pre>\n<h3 class="field-label">Produces</h3>\n    This API call produces the following media types according to the <span class="header">Accept</span> request header;\n    the media type will be conveyed by the <span class="header">Content-Type</span> response header.\n    <ul>\n<li><code>application/json</code></li>\n</ul>\n<h3 class="field-label">Responses</h3>\n<h4 class="field-label">200</h4>\n    Expected response to a valid request\n        <a href="#Pets">Pets</a>\n<h4 class="field-label">default</h4>\n    unexpected error\n        <a href="#Error">Error</a>\n</div> <!-- method -->\n<hr/>\n<h2><a name="__Models">Models</a></h2>\n  [ Jump to <a href="#__Methods">Methods</a> ]\n\n  <h3>Table of Contents</h3>\n<ol>\n<li><a href="#Error"><code>Error</code> - </a></li>\n<li><a href="#Pet"><code>Pet</code> - </a></li>\n<li><a href="#Pets"><code>Pets</code> - </a></li>\n</ol>\n<div class="model">\n<h3><a name="Error"><code>Error</code> - </a> <a class="up" href="#__Models">Up</a></h3>\n<div class="model-description"></div>\n<div class="field-items">\n<div class="param">code </div><div class="param-desc"><span class="param-type"><a href="#integer">Integer</a></span>  format: int32</div>\n<div class="param">message </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span> </div>\n</div> <!-- field-items -->\n</div>\n<div class="model">\n<h3><a name="Pet"><code>Pet</code> - </a> <a class="up" href="#__Models">Up</a></h3>\n<div class="model-description"></div>\n<div class="field-items">\n<div class="param">id </div><div class="param-desc"><span class="param-type"><a href="#long">Long</a></span>  format: int64</div>\n<div class="param">name </div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span> </div>\n<div class="param">tag (optional)</div><div class="param-desc"><span class="param-type"><a href="#string">String</a></span> </div>\n</div> <!-- field-items -->\n</div>\n<div class="model">\n<h3><a name="Pets"><code>Pets</code> - </a> <a class="up" href="#__Models">Up</a></h3>\n<div class="model-description"></div>\n<div class="field-items">\n</div> <!-- field-items -->\n</div>\n',
            "docname": "fake_content_id",
            "title": "Swagger Petstore",
            "toc": '<ul><li><a href="#Access">Access</a></li><li><a href="#Methods">Methods</a></li><ul><li><a href="#TableofContents">Table of Contents </a></li><ul><li><a href="#Pets">Pets</a></li></ul></ul><ul><li><a href="#201">201</a></li><li><a href="#default">default</a></li></ul><ul><li><a href="#200">200</a></li><li><a href="#default">default</a></li></ul><ul><li><a href="#200">200</a></li><li><a href="#default">default</a></li></ul><li><a href="#Models">Models</a></li><ul><li><a href="#TableofContents">Table of Contents</a></li></ul><ul><li><a href="#Error----Up"></a></li></ul><ul><li><a href="#Pet----Up"></a></li></ul><ul><li><a href="#Pets----Up"></a></li></ul></ul>',
            "unsearchable": None,
            "content_id": "fake_content_id",
            "meta": {
                "someKey": "someValue",
                "preferGithubIssues": True,
                "github_issues_url": "https://github.com/deconst/fake-repo/issues",
                "github_edit_url": "https://github.com/deconst/fake-repo/edit/master/tests/dest/index.html"
            },
            "asset_offsets": {},
            "addenda": None,
            "per_page_meta": {}}
        dest_path = os.path.join(os.getcwd(), 'tests',
                                 'dest', 'output_file.json')
        write_out(the_envelope_passed, file_path=dest_path)
        with open(dest_path, 'r') as written_file:
            actual_file = json.load(written_file)
        fake_json_envelope = os.path.join(
            os.getcwd(), 'tests', 'src', 'input_file_writeout.json')
        with open(fake_json_envelope, 'r') as fake_envelope:
            expected_json_output = json.load(fake_envelope)
        self.assertEqual(actual_file, expected_json_output)


class Envelope_OPENAPITestCase(unittest.TestCase):
    '''
    Tests for class methods in the Envelope_OPENAPI class
    '''

    def setUp(self):
        '''
        Instantiate the class.
        '''
        fake_deconst = {}
        fake_deconst['contentIDBase'] = 'https://github.com/deconst/fake-repo/'
        fake_deconst['meta'] = {
            'github_issues_url': 'https://github.com/deconst/fake-repo/issues',
            "someKey": "someValue",
            "preferGithubIssues": True}
        fake_deconst['github_url'] = 'https://github.com/deconst/fake-repo/'
        fake_deconst['envelope_dir'] = 'fake_envelope_dir'
        fake_deconst['git_root'] = os.getcwd()
        fake_deconst['github_branch'] = 'master'
        fake_deconst['originalAssetDir'] = os.path.join(
            os.getcwd(), 'tests', 'src', 'assets', '')
        original_file = os.path.join(
            os.getcwd(), 'tests', 'src', 'small_test', "openapi.json")
        self.envelope = Envelope_OPENAPI(os.path.join( os.getcwd(), 'tests', 'src', 'small_test'),
                                      '<body><p>testing</p></body>',
                                      originalFile=original_file,
                                      title='test_title',
                                      toc='<ul><li>test1</li><li>test2</li></ul>',
                                      publish_date='test_date',
                                      unsearchable='derp',
                                      content_id='https://github.com/deconst/fake-repo/small_test/openapi.json',
                                      meta=fake_deconst['meta'],
                                      asset_offsets='random',
                                      addenda='derpderp',
                                      deconst_config=fake_deconst,
                                      per_page_meta={'randomkey': 'random'},
                                      github_edit_url=fake_deconst['github_url'])
        return self.envelope

    def tearDown(self):
        self.envelope = None

    def test_serialization_path_pass(self):
        '''
        Does the correct serialization path appear from this class method?
        '''
        ##TODO: Check this once
        expected_serialization_path = "fake_envelope_dir/https%3A%2F%2Fgithub.com%2Fdeconst%2Ffake-repo%2Fsmall_test%2Fopenapi.json.json"
        actual_serialization_path = self.envelope.serialization_path()
        self.assertEqual(expected_serialization_path,
                         actual_serialization_path)

    def test__populate_meta_pass(self, testing=True):
        '''
        Does the class method pass the metadata to each per page metadata key?
        '''
        expected_meta_result = {
            'github_issues_url': 'https://github.com/deconst/fake-repo/issues',
            "someKey": "someValue",
            "preferGithubIssues": True,
            'randomkey': 'random'}
        
        self.envelope._populate_meta(test=testing)
        actual_meta_result = self.envelope.meta
        self.assertEqual(expected_meta_result, actual_meta_result)

    def test__populate_git_pass(self, testing=True):
        '''
        Does the class method pass the correct git url result?
        '''
        expected_git_path = 'https://github.com/deconst/fake-repo/edit/master/tests/src/asset_test_html.html'
        path_string = os.path.join( os.getcwd(), 'tests', 'src', 'small_test')
        self.envelope._populate_git(test=testing, path_string=path_string)
        actual_git_path = self.envelope.meta['github_edit_url']
        self.assertEqual(expected_git_path, actual_git_path)

    def test__populate_content_id_pass(self):
        '''
        Does the content_id populate correctly?
        '''
        expected_content_id = 'https://github.com/deconst/fake-repo/tests/src/small_test/openapi.json'
        self.envelope._populate_content_id(testing=True)
        actual_content_id = self.envelope.content_id
        self.assertEqual(expected_content_id, actual_content_id)

 
class Envelope_OPENAPI_deconstjsonTestCase(unittest.TestCase):
    '''
    Tests explicitly for the deconst.json populate method in Envelope_OPENAPI
    '''

    def setUp(self):
        '''
        Instantiate the class.
        '''
        original_file = os.path.join(
            os.getcwd(), 'tests', 'src', 'asset_test_html.html')
        self.envelope = Envelope_OPENAPI(os.path.join( os.getcwd(), 'tests', 'src', 'small_test'),
                                      '<body><p>testing</p></body>',
                                      originalFile=original_file,
                                      title='test_title',
                                      toc='<ul><li>test1</li><li>test2</li></ul>',
                                      publish_date='test_date',
                                      unsearchable='derp',
                                      content_id='https://github.com/deconst/fake-repo/test/src/openapi.json',
                                      meta='meta',
                                      asset_offsets='random',
                                      addenda='derpderp',
                                      per_page_meta={'randomkey': 'random'},
                                      github_edit_url='github_url')
        return self.envelope

    def tearDown(self):
        self.envelope = None

    def test__populate_deconst_config_pass(self):
        '''
        Question?
        '''
        expected_deconst_result = {
            "contentIDBase": "https://github.com/deconst/fake-repo/",
            "githubUrl": "https://github.com/deconst/fake-repo/",
            "meta": {
                "github_issues_url": "https://github.com/deconst/fake-repo/issues",
                "someKey": "someValue", "preferGithubIssues": True}}
        self.envelope._populate_deconst_config()
        actual_deconst_result = {}
        actual_deconst_result['contentIDBase'] = self.envelope.deconst_config.content_id_base
        actual_deconst_result['githubUrl'] = self.envelope.deconst_config.github_url
        actual_deconst_result['meta'] = self.envelope.deconst_config.meta
        self.assertEqual(expected_deconst_result, actual_deconst_result)

    @mock.patch.dict('os.environ', {
        'ASSET_DIR': os.path.join(os.getcwd(), 'tests', 'dest', 'assets', '')})
    def test__populate_asset_offsets_pass(self):
        '''
        Do the assets populate correctly?
        '''
        self.maxDiff = None
        expected_body_result = (
            '<p><img alt="test image" src="0"/></p><p><img alt="test image" src="1"/></p>')
        expected_asset_map = {
            os.path.join(os.getcwd(), 'tests', 'dest', 'assets', 'tool_time.jpg'): 58,
            os.path.join(os.getcwd(), 'tests', 'dest', 'assets', 'tool_time12.jpg'): 108}
        self.envelope._populate_asset_offsets(
            original_asset_dir=os.path.join(os.getcwd(), 'tests', 'src', 'assets', ''))
        actual_body_result = self.envelope.body
        actual_asset_map = self.envelope.asset_offsets
        self.assertEqual([expected_body_result, expected_asset_map], [
                         actual_body_result, actual_asset_map])


if __name__ == '__main__':
    unittest.main()
