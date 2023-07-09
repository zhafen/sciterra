"""Test basic pipeline functionality with each librarian."""

from sciterra.librarians import adslibrarian, librarian, s2librarian

from multiprocessing import Pool

from tqdm import tqdm


##############################################################################
# Semantic Scholar
##############################################################################


class TestSemanticScholarLibrarian:
    librarian = s2librarian.SemanticScholarLibrarian()

    def test_semanticscholar_convert_single(self):
        identifier = "DOI:10.1093/mnras/stx952"
        paper_id = "f2c251056dee4c6f9130b31e5e3e4b3296051c49"
        papers = TestSemanticScholarLibrarian.librarian.get_publications(
            [identifier],
            convert=False,
        )
        pub = TestSemanticScholarLibrarian.librarian.convert_publication(
            paper=papers[0]
        )
        assert papers[0].paperId == paper_id
        assert papers[0].abstract == pub.abstract
        assert papers[0].paperId == pub.identifier  # n.b., paperId != DOI id

    def test_semanticscholar_convert_parallel(self):
        identifier = "DOI:10.1093/mnras/stx952"
        papers = TestSemanticScholarLibrarian.librarian.get_publications(
            [identifier],
            convert=False,
        )

        converted_pubs = TestSemanticScholarLibrarian.librarian.convert_publications(
            papers
        )
        assert papers[0].abstract == converted_pubs[0].abstract

    def test_semanticscholar_convert_100(self):
        identifiers = ["DOI:10.1093/mnras/stx952"] * 100
        paper_id = "f2c251056dee4c6f9130b31e5e3e4b3296051c49"

        papers = TestSemanticScholarLibrarian.librarian.get_publications(
            identifiers,
            convert=False,
        )

        converted = TestSemanticScholarLibrarian.librarian.convert_publications(
            papers,
        )
        assert len(converted) == 100
        assert all([pub.identifier == paper_id for pub in converted])

    def test_semanticscholar_single_query(self):
        # construct an atlas w a single identifier
        identifier = "DOI:10.1093/mnras/stx952"
        paper_id = "f2c251056dee4c6f9130b31e5e3e4b3296051c49"

        pubs = TestSemanticScholarLibrarian.librarian.get_publications(
            [identifier],
        )
        assert len(pubs) == 1

        # assumes converted
        assert pubs[0].identifier == paper_id

    def test_semanticscholar_100_query(self):
        identifiers = ["DOI:10.1093/mnras/stx952"] * 100
        paper_id = "f2c251056dee4c6f9130b31e5e3e4b3296051c49"

        pubs = TestSemanticScholarLibrarian.librarian.get_publications(
            identifiers,
        )

        assert len(pubs) == 100
        assert all([pub.identifier == paper_id for pub in pubs])
