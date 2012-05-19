from HTMLParser import HTMLParser

import urllib

class _CustomizableHTMLParser(HTMLParser):

    def __passing_function(self):
        pass

    def __add_to_output(self,data):
        if data != None:
            for a in data:
                self.__output_dict[a[0]]=a[1]

    #Initial implementation, it needs to be refactoring
    def __init__(self,func_dict):
        HTMLParser.__init__(self)
        
        self.__output_dict={}
        self.__handle_starttag=self.__passing_function
        self.__handle_startendtag=self.__passing_function
        self.__handle_endtag=self.__passing_function
        self.__handle_data=self.__passing_function
        self.__handle_charref=self.__passing_function
        self.__handle_entityref=self.__passing_function
        self.__handle_comment=self.__passing_function
        self.__handle_decl=self.__passing_function
        self.__handle_pi=self.__passing_function
        for name in custom_dict.keys():
            if name == 'handle_starttag':
                self.__handle_starttag=func_dict['handle_starttag']
            elif name == 'handle_startendtag':
                self.__handle_startendtag=func_dict['handle_startendtag']
            elif name == 'handle_endtag':
                self.__handle_endtag=func_dict['handle_endtag']
            elif name == 'handle_data':
                self.__handle_data=func_dict['handle_data']
            elif name == 'handle_charref':
                self.__handle_charref=func_dict['handle_charref']
            elif name == 'handle_entityref':
                self.__handle_entityref=func_dict['handle_entityref']
            elif name == 'handle_comment':
                self.__handle_comment=func_dict['handle_comment']
            elif name == 'handle_decl':
                self.__handle_decl=func_dict['handle_decl']
            elif name == 'handle_pi':
                self.__handle_pi=func_dict['handle_pi']
    
    def handle_starttag(self,tag,attrs):
        result=self.__handle_starttag(tag,attrs)
        self.__add_to_output(result)

    def handle_startendtag(self,tag,attrs):
        result=self.__handle_startendtag(tag,attrs)
        self.__add_to_output(result)

    def handle_endtag(self,tag):
        result=self.__handle_endtag(tag)
        self.__add_to_output(result)

    def handle_data(self,data):
        result=self.__handle_data(data)
        self.__add_to_output(result)

    def handle_charref(self,name):
        result=self.__handle_charref(name)
        self.__add_to_output(result)
    
    def handle_entityref(self,name):
        result=self.__handle_entityref(name)
        self.__add_to_output(result)

    def handle_comment(self,data):
        result=self.__handle_comment(data)
        self.__add_to_output(result)

    def handle_decl(self,decl):
        result=self.__handle_decl(decl)
        self.__add_to_output(result)

    def handle_pi(self,data):
        result=self.__handle_pi(data)
        self.__add_to_output(result)

    def get_result(self):
        return self.__output_dict

class FeatureExtractor(object):
    
    def __parser_factory_method(self,func_dict):
        return _CustomizableHTMLParser(func_dict)

    def __init__(self,urls,func_dict):
        self.__output_list=[]
        self.__url_list=urls
        self.__parser=__parser_factory_method(func_dict)
    
    def __get_html_file(self,url):
        try:
            connection=urllib.urlopen(url)
            page=connection.read()
        except:
            page=""
        return page
    
    def extract(self):
        for url in self.__url_list:
            #retrieve url page
            page=__get_html_file(url)
            if page != "":
                parser.feed(page)
                parser.close()
                self.__output_list.append((url,parser.get_result()))
                parser.
        return self.__output_list
