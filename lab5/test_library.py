import pytest
from datetime import datetime
from library import Book


class TestBook:
    """Test suite for the Book class"""
    
    @pytest.fixture
    def sample_book(self):
        """Fixture providing a sample book for testing"""
        return Book("The Pragmatic Programmer", "Hunt & Thomas", 1999, "978-0201616224")
    
    @pytest.fixture
    def another_book(self):
        """Another book with different data but same ISBN for equality testing"""
        return Book("Different Title", "Anyone", 2000, "978-0201616224")
    
    def test_everything_is_object(self, sample_book):
        """Test that both instances and classes are objects in Python"""
        # Instance is an object
        assert isinstance(sample_book, object)
        assert type(sample_book).__name__ == 'Book'
        
        # Class itself is an object (of type 'type')
        assert isinstance(Book, object)
        assert type(Book).__name__ == 'type'
    
    def test_instance_attributes(self, sample_book):
        """Test that instance attributes are correctly set"""
        assert sample_book.title == "The Pragmatic Programmer"
        assert sample_book.author == "Hunt & Thomas"
        assert sample_book.year == 1999
        assert sample_book.isbn == "978-0201616224"
    
    def test_str_method(self, sample_book):
        """Test __str__ returns human-friendly format"""
        expected = "The Pragmatic Programmer by Hunt & Thomas (1999)"
        assert str(sample_book) == expected
    
    def test_repr_method(self, sample_book):
        """Test __repr__ returns developer-friendly format"""
        expected = "Book('The Pragmatic Programmer', 'Hunt & Thomas', 1999, '978-0201616224')"
        assert repr(sample_book) == expected
        
    def test_equality_by_isbn(self, sample_book, another_book):
        """Test that books are equal if ISBNs match, regardless of other attributes"""
        # Same ISBN = equal
        assert sample_book == another_book
        
        # Different ISBN = not equal
        different_isbn_book = Book("The Pragmatic Programmer", "Hunt & Thomas", 1999, "different-isbn")
        assert sample_book != different_isbn_book
    
    def test_equality_with_non_book(self, sample_book):
        """Test that comparing with non-Book objects returns False, not error"""
        assert sample_book != "not a book"
        assert sample_book != 42
        assert sample_book != None
        assert sample_book != ["list", "of", "things"]
    
    def test_checkout_increments_counter(self, sample_book):
        """Test that checkout() increments the private counter"""
        # Initial checkouts should be 0
        stats = sample_book.get_stats()
        assert stats['checkouts'] == 0
        
        # After one checkout
        sample_book.checkout()
        stats = sample_book.get_stats()
        assert stats['checkouts'] == 1
        
        # After multiple checkouts
        sample_book.checkout()
        sample_book.checkout()
        stats = sample_book.get_stats()
        assert stats['checkouts'] == 3
    
    def test_get_stats_returns_dict(self, sample_book):
        """Test that get_stats returns proper dictionary"""
        sample_book.checkout()
        stats = sample_book.get_stats()
        
        assert isinstance(stats, dict)
        assert 'title' in stats
        assert 'checkouts' in stats
        assert stats['title'] == "The Pragmatic Programmer"
        assert stats['checkouts'] == 1
    
    def test_age_calculation(self, sample_book):
        """Test that age() correctly calculates book age"""
        current_year = datetime.now().year
        expected_age = current_year - 1999
        assert sample_book.age() == expected_age
        
        # Test with a recent book
        new_book = Book("Modern Python", "Author", current_year, "123")
        assert new_book.age() == 0
    
    def test_sortable_by_year(self):
        """Test that books can be sorted by year using __lt__"""
        book1 = Book("Old", "Author", 1990, "1")
        book2 = Book("Middle", "Author", 2000, "2")
        book3 = Book("New", "Author", 2020, "3")
        
        books = [book2, book3, book1]
        books.sort()
        
        assert books[0] == book1  # 1990
        assert books[1] == book2  # 2000
        assert books[2] == book3  # 2020


