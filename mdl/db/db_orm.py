#!/usr/bin/env python3
"""mdl ORM classes.

Manages connection pooling among other things.

"""

# SQLobject stuff
from sqlalchemy import UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, VARBINARY
from sqlalchemy import Column
from sqlalchemy import ForeignKey

BASE = declarative_base()


class DriverCompany(BASE):
    """Class defining the mdl_drivercompany table of the database."""

    __tablename__ = 'mdl_drivercompany'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
        )

    idx_drivercompany = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    drivercompany_name = Column(VARBINARY(512), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class DeviceMake(BASE):
    """Class defining the mdl_devicemake table of the database."""

    __tablename__ = 'mdl_devicemake'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
        )

    idx_devicemake = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    make_name = Column(VARBINARY(512), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class DeviceModel(BASE):
    """Class defining the mdl_devicemodel table of the database."""

    __tablename__ = 'mdl_devicemodel'
    __table_args__ = (
        UniqueConstraint('idx_devicemodel', 'idx_devicemake'),
        {
            'mysql_engine': 'InnoDB'
        }
        )

    idx_devicemodel = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_devicemake = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_devicemake.idx_devicemake'),
        nullable=False, server_default='1')

    model_name = Column(VARBINARY(512), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Route(BASE):
    """Class defining the mdl_route table of the database."""

    __tablename__ = 'mdl_route'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
        )

    idx_route = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    route_name = Column(VARBINARY(512), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Rider(BASE):
    """Class defining the mdl_rider table of the database."""

    __tablename__ = 'mdl_rider'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
        )

    idx_rider = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    first_name = Column(VARBINARY(512), nullable=True, default=None)

    last_name = Column(VARBINARY(512), nullable=True, default=None)

    password = Column(VARBINARY(512), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Driver(BASE):
    """Class defining the mdl_driver table of the database."""

    __tablename__ = 'mdl_driver'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
        )

    idx_driver = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_drivercompany = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_drivercompany.idx_drivercompany'),
        nullable=False, server_default='1')

    first_name = Column(VARBINARY(512), nullable=True, default=None)

    last_name = Column(VARBINARY(512), nullable=True, default=None)

    password = Column(VARBINARY(512), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class RiderDevice(BASE):
    """Class defining the mdl_riderdevice table of the database."""

    __tablename__ = 'mdl_riderdevice'
    __table_args__ = (
        UniqueConstraint('id_riderdevice'),
        {
            'mysql_engine': 'InnoDB'
        }
        )

    idx_riderdevice = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_rider = Column(
        BIGINT(unsigned=True), ForeignKey('mdl_rider.idx_rider'),
        nullable=False, server_default='1')

    idx_devicemodel = Column(
        BIGINT(unsigned=True), ForeignKey('mdl_devicemodel.idx_devicemodel'),
        nullable=False, server_default='1')

    id_riderdevice = Column(VARBINARY(512), nullable=True, default=None)

    serial_riderdevice = Column(VARBINARY(512), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class DriverDevice(BASE):
    """Class defining the mdl_driverdevice table of the database."""

    __tablename__ = 'mdl_driverdevice'
    __table_args__ = (
        UniqueConstraint('id_driverdevice'),
        {
            'mysql_engine': 'InnoDB'
        }
        )

    idx_driverdevice = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_driver = Column(
        BIGINT(unsigned=True), ForeignKey('mdl_driver.idx_driver'),
        nullable=False, server_default='1')

    idx_route = Column(
        BIGINT(unsigned=True), ForeignKey('mdl_route.idx_route'),
        nullable=False, server_default='1')

    idx_devicemodel = Column(
        BIGINT(unsigned=True), ForeignKey('mdl_devicemodel.idx_devicemodel'),
        nullable=False, server_default='1')

    id_driverdevice = Column(VARBINARY(512), nullable=True, default=None)

    serial_driverdevice = Column(VARBINARY(512), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Configuration(BASE):
    """Class defining the mdl_configuration table of the database."""

    __tablename__ = 'mdl_configuration'
    __table_args__ = (
        UniqueConstraint(
            'config_key'),
        {
            'mysql_engine': 'InnoDB'
        }
        )

    idx_configuration = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    config_key = Column(VARBINARY(512), nullable=True, default=None)

    config_value = Column(VARBINARY(512), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))
