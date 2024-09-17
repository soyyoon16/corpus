import datetime


"""Adapted from Python 3 Object-Oriented Programming 3rd edition 
by Dusty Phillips
"""

# store state for notes
last_id = 0

class Document:
    """
    Represents a single Document in the Corpus. A Document consists of
    contents and can be searched against. Documents are identified using
    ids.
    """

    def __init__(self, contents, tags="", id=None):
        """
        Creates a Document containing contents, with optional tags. Initializer
        also sets a unique id and timestamp of creation.
        :param contents: contents of document
        :param tags: optional list of keyword tags
        """
        self.contents = contents
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id if id is None else id

    # how we convert an object to a string
    def __str__(self):
        return f'{self.contents[:30]}...'

    # a __repr__ is supposed to be unambiguous and is called when no __str__
    # method is available
    def __repr__(self):
        return f'{self.__class__.__name__}({self.contents[:30]}...,' \
               f' {self.tags})'

    def match(self, filter):
        """
        Determine whether document matches filter text.
        :param filter:
        :return: bool
        """
        return filter in self.contents or filter in self.tags


class Corpus:
    """
    Represents a collection of Documents that can be tagged, modified,
    and searched.
    """

    def __init__(self):
        """Initialize Corpus with empty list of Documents"""
        self.docs = []

    def create_document(self, id, contents, tags=""):
        """Create a new Document and add it to the list"""
        self.docs.append(Document(contents, tags, id))

    # This doesn't do anything useful for the user, but it helps us write
    # better-looking software
    def _find_doc_by_id(self, doc_id):
        """Return the Document corresponding to given doc_id if it exists"""
        for doc in self.docs:
            if doc.id == doc_id:
                return doc
        return None

    def modify_document(self, doc_id, new_contents):
        """Change contents of Document with ID doc_id to new_contents"""
        """
        for doc in self.docs:
            if doc.id == doc_id:
                doc.contents = new_contents
                break
        """
        self._find_doc_by_id(doc_id).contents = new_contents

    def modify_tags(self, doc_id, new_tags):
        """Change tags of a Document with ID doc_id to new_tags"""
        """
        for doc in self.docs:
            if doc.id == doc_id:
                doc.tags = new_tags
                break
        """
        self._find_doc_by_id(doc_id).tags = new_tags

    def search(self, filter):
        """Find all Documents that match the filter string"""
        return [doc for doc in self.docs if Document.match(filter)]

