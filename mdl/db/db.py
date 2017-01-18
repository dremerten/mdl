#!/usr/bin/env python3

"""Class to process connection."""

# mdl libraries
from mdl.utils import log
from mdl.db import POOL
from mdl.db.db_orm import Drivers


class Database(object):
    """Class interacts with the connection.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self):
        """Function for intializing the class.

        Args:
            config: Config object

        Returns:
            None

        """
        # Intialize key variables
        self._session = POOL()

    def add_all(self, data_list, error_code, die=True):
        """Do a database modification.

        Args:
            data_list: List of sqlalchemy table objects
            error_code: Error number to use if one occurs
            die: Don't die if False, just return success

        Returns:
            success: True is successful

        """
        # Initialize key variables
        success = False

        # Open database connection. Prepare cursor
        session = self.session()

        try:
            # Update the database cache
            session.add_all(data_list)

            # Commit  change
            session.commit()

            # disconnect from server
            self.close()

            # Update success
            success = True

        except Exception as exception_error:
            success = False
            session.rollback()
            log_message = (
                'Unable to modify database connection. '
                'Error: \"%s\"') % (exception_error)
            if die is True:
                log.log2die(error_code, log_message)
            else:
                log.log2warning(error_code, log_message)

        except:
            success = False
            session.rollback()
            log_message = ('Unexpected database exception')
            if die is True:
                log.log2die(error_code, log_message)
            else:
                log.log2warning(error_code, log_message)

        # Return
        return success

    def session(self):
        """Create a session from the database pool.

        Args:
            None

        Returns:
            db_session: Session

        """
        # Initialize key variables
        db_session = self._session
        return db_session

    def close(self):
        """Return a session to the database pool.

        Args:
            None

        Returns:
            None

        """
        # Return session
        self.session().close()

    def commit(self, session, error_code):
        """Do a database modification.

        Args:
            session: Session
            error_code: Error number to use if one occurs

        Returns:
            None

        """
        # Do commit
        try:
            # Commit  change
            session.commit()

        except Exception as exception_error:
            session.rollback()
            log_message = (
                'Unable to modify database connection. '
                'Error: \"%s\"') % (exception_error)
            log.log2die(error_code, log_message)
        except:
            session.rollback()
            log_message = ('Unexpected database exception')
            log.log2die(error_code, log_message)

        # disconnect from server
        self.close()

    def add(self, record, error_code):
        """Add a record to the database.

        Args:
            record: Record object
            error_code: Error number to use if one occurs

        Returns:
            None

        """
        # Initialize key variables
        session = self.session()

        # Do add
        try:
            # Commit change
            session.add(record)
            session.commit()

        except Exception as exception_error:
            session.rollback()
            log_message = (
                'Unable to modify database connection. '
                'Error: \"%s\"') % (exception_error)
            log.log2die(error_code, log_message)
        except:
            session.rollback()
            log_message = ('Unexpected database exception')
            log.log2die(error_code, log_message)

        # disconnect from server
        self.close()


def connectivity():
    """Check connectivity to the database.

    Args:
        None

    Returns:
        valid: True if connectivity is OK

    """
    # Initialize key variables
    valid = False

    # Do test
    database = Database()
    session = database.session()

    try:
        result = session.query(Drivers.idx_driver).filter(
            Drivers.idx_driver == -1)
        for _ in result:
            break
        valid = True
    except:
        pass

    database.close()

    # Return
    return valid
