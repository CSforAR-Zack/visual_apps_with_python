import unittest
import os
from model import TodoModel


class TestTodoModel(unittest.TestCase):
    """Test suite for the database logic."""

    def setUp(self):
        """Runs BEFORE every single test. Sets up a fresh environment."""
        self.test_db = "test_todos.db"
        # We pass our temporary database name here!
        self.model = TodoModel(db_name=self.test_db) 

    def tearDown(self):
        """Runs AFTER every single test. Cleans up the mess."""
        self.model.conn.close()
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_add_task(self):
        """Testing if we can add a task to the database."""
        # 1. ACT: Do the thing we are testing
        self.model.add_task("Grade math papers")
        
        # 2. CHECK: Look directly into the database to see if it worked
        cursor = self.model.conn.cursor()
        cursor.execute("SELECT task, is_completed FROM todos")
        rows = cursor.fetchall()
        
        # 3. ASSERT: Prove that the results match our expectations
        self.assertEqual(len(rows), 1)                     # Is there exactly 1 task?
        self.assertEqual(rows[0][0], "Grade math papers")  # Is the text correct?
        self.assertEqual(rows[0][1], 0)                    # Is it marked incomplete (0)?

    def test_delete_task(self):
        """Testing if we can delete a task."""
        # 1. SETUP: Add a task first, then grab its ID
        self.model.add_task("Prepare lesson plan")
        cursor = self.model.conn.cursor()
        cursor.execute("SELECT id FROM todos")
        task_id = cursor.fetchone()[0]
        
        # 2. ACT: Try to delete it
        self.model.delete_task(task_id)
        
        # 3. ASSERT: Prove the database is now empty
        cursor.execute("SELECT * FROM todos")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 0)

if __name__ == "__main__":
    unittest.main()