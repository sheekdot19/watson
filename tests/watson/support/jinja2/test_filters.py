# -*- coding: utf-8 -*-
from watson.support.jinja2 import filters
from watson.form import fields


class TestFilters(object):

    def test_qualified_name(self):
        assert filters.get_qualified_name(self) == 'tests.watson.support.jinja2.test_filters.TestFilters'

    def test_label(self):
        field = fields.Text(label='Test', name='test')
        assert filters.label(field) == '<label for="test">Test</label><input id="test" name="test" type="text" />'

    def test_merge_query(self):
        qs = filters.merge_query_string({'page': 1, 'extra': 'something'}, {'page': 2})
        assert 'extra=something' in qs
        assert 'page=2' in qs
