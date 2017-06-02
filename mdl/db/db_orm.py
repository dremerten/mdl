#!/usr/bin/env python3
"""mdl ORM classes.

Manages connection pooling among other things.

"""

# SQLobject stuff
from sqlalchemy import UniqueConstraint, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, VARBINARY
from sqlalchemy.dialects.mysql import FLOAT
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String

BASE = declarative_base()


class CreditCards(BASE):
    """Class defining the mdl_creditcard table of the database."""

    __tablename__ = 'mdl_creditcards'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_creditcard = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class DriverCompanies(BASE):
    """Class defining the mdl_drivercompanies table of the database."""

    __tablename__ = 'mdl_drivercompanies'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_drivercompany = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_address = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_addresses.idx_address'),
        nullable=False, server_default='1')

    idx_billaddress = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_billaddresses.idx_billaddress'),
        nullable=False, server_default='1')

    idx_companycategory = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_companycategories.idx_companycategory'),
        nullable=False, server_default='1')

    drivercompany_name = Column(VARBINARY(128), nullable=True, default=None)

    rating_value = Column(FLOAT, server_default='0')

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class CompanyCategories(BASE):
    """Class defining the mdl_companycategories table of the database."""

    __tablename__ = 'mdl_companycategories'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_companycategory = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    companycategory_name = Column(VARBINARY(128), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class DeviceMakes(BASE):
    """Class defining the mdl_devicemakes table of the database."""

    __tablename__ = 'mdl_devicemakes'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_devicemake = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    make_name = Column(VARBINARY(50), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class DeviceModels(BASE):
    """Class defining the mdl_devicemodels table of the database."""

    __tablename__ = 'mdl_devicemodels'
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
        ForeignKey('mdl_devicemakes.idx_devicemake'),
        nullable=False, server_default='1')

    model_name = Column(VARBINARY(50), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Routes(BASE):
    """Class defining the mdl_routes table of the database."""

    __tablename__ = 'mdl_routes'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_route = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    route_name = Column(VARBINARY(256), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Riders(BASE):
    """Class defining the mdl_riders table of the database."""

    __tablename__ = 'mdl_riders'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_rider = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    first_name = Column(VARBINARY(50), nullable=True, default=None)

    last_name = Column(VARBINARY(50), nullable=True, default=None)

    password = Column(VARBINARY(512), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Drivers(BASE):
    """Class defining the mdl_drivers table of the database."""

    __tablename__ = 'mdl_drivers'
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
        ForeignKey('mdl_drivercompanies.idx_drivercompany'),
        nullable=False, server_default='1')

    idx_address = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_addresses.idx_address'),
        nullable=False, server_default='1')

    idx_billaddress = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_billaddresses.idx_billaddress'),
        nullable=False, server_default='1')

    first_name = Column(VARBINARY(50), nullable=True, default=None)

    last_name = Column(VARBINARY(50), nullable=True, default=None)

    email = Column(String(50), nullable=False)

    password = Column(VARBINARY(512), nullable=True, default=None)

    rating_value = Column(FLOAT, server_default='0')

    off_duty = Column(INTEGER(unsigned=True), server_default='0')

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class RiderDevices(BASE):
    """Class defining the mdl_ridersdevices table of the database."""

    __tablename__ = 'mdl_ridersdevices'
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
        BIGINT(unsigned=True), ForeignKey('mdl_riders.idx_rider'),
        nullable=False, server_default='1')

    idx_devicemodel = Column(
        BIGINT(unsigned=True), ForeignKey('mdl_devicemodels.idx_devicemodel'),
        nullable=False, server_default='1')

    id_riderdevice = Column(VARBINARY(512), nullable=True, default=None)

    serial_riderdevice = Column(VARBINARY(128), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class DriverDevices(BASE):
    """Class defining the mdl_driversdevices table of the database."""

    __tablename__ = 'mdl_driversdevices'
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
        BIGINT(unsigned=True), ForeignKey('mdl_drivers.idx_driver'),
        nullable=False, server_default='1')

    idx_route = Column(
        BIGINT(unsigned=True), ForeignKey('mdl_routes.idx_route'),
        nullable=False, server_default='1')

    idx_devicemodel = Column(
        BIGINT(unsigned=True), ForeignKey('mdl_devicemodels.idx_devicemodel'),
        nullable=False, server_default='1')

    idx_creditcard = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_creditcards.idx_creditcard'),
        nullable=False, server_default='1')

    id_driverdevice = Column(VARBINARY(512), nullable=True, default=None)

    serial_driverdevice = Column(VARBINARY(50), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Vehicles(BASE):
    """Class defining the mdl_vehicles table of the database."""

    __tablename__ = 'mdl_vehicles'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_vehicle = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_vehiclemodel = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_vehiclemodels.idx_vehiclemodel'),
        nullable=False, server_default='1')

    license_plate = Column(VARBINARY(50), nullable=True, default=None)

    vehicle_seats = Column(INTEGER(unsigned=True), server_default='5')

    vehicle_year = Column(INTEGER(unsigned=True), default=None)

    rating_value = Column(FLOAT, server_default='0')

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class VehicleCategories(BASE):
    """Class defining the mdl_vehiclecategories table of the database."""

    __tablename__ = 'mdl_vehiclecategories'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_vehiclecategory = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_vehiclemodel = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_vehiclemodels.idx_vehiclemodel'),
        nullable=False, server_default='1')

    vehiclecategory_name = Column(VARBINARY(256), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class VehicleMakes(BASE):
    """Class defining the mdl_vehiclemakes table of the database."""

    __tablename__ = 'mdl_vehiclemakes'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_vehiclemake = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    make_name = Column(VARBINARY(50), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class VehicleModels(BASE):
    """Class defining the mdl_vehiclemodels table of the database."""

    __tablename__ = 'mdl_vehiclemodels'
    __table_args__ = (
        UniqueConstraint('idx_vehiclemodel', 'idx_vehiclemake'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_vehiclemodel = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_vehiclemake = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_vehiclemakes.idx_vehiclemake'),
        nullable=False, server_default='1')

    model_name = Column(VARBINARY(50), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class DriverCompanyRatings(BASE):
    """Class defining the mdl_companyrating table of the database."""

    __tablename__ = 'mdl_drivercompanyratings'
    __table_args__ = (
        UniqueConstraint('idx_drivercompanyrating', 'rating_timestamp'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_drivercompanyrating = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_drivercompany = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_drivercompanies.idx_drivercompany'),
        nullable=False, server_default='1')

    rating_timestamp = Column(
        BIGINT(unsigned=True), nullable=False, server_default='0')

    rating_value = Column(INTEGER(unsigned=True), server_default='0')

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class VehicleRatings(BASE):
    """Class defining the mdl_vehiclerating table of the database."""

    __tablename__ = 'mdl_vehicleratings'
    __table_args__ = (
        UniqueConstraint('idx_vehiclerating', 'rating_timestamp'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_vehiclerating = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_vehicle = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_vehicles.idx_vehicle'),
        nullable=False, server_default='1')

    rating_timestamp = Column(
        BIGINT(unsigned=True), nullable=False, server_default='0')

    rating_value = Column(INTEGER(unsigned=True), server_default='0')

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class DriverRatings(BASE):
    """Class defining the mdl_driversrating table of the database."""

    __tablename__ = 'mdl_driversratings'
    __table_args__ = (
        UniqueConstraint('idx_driverrating', 'rating_timestamp'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_driverrating = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_driver = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_drivers.idx_driver'),
        nullable=False, server_default='1')

    rating_timestamp = Column(
        BIGINT(unsigned=True), nullable=False, server_default='0')

    rating_value = Column(INTEGER(unsigned=True), server_default='0')

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class GeoRegions(BASE):
    """Class defining the mdl_georegions table of the database."""

    __tablename__ = 'mdl_georegions'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_georegion = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    georegion_name = Column(VARBINARY(128), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class GeoCountries(BASE):
    """Class defining the mdl_geocountries table of the database."""

    __tablename__ = 'mdl_geocountries'
    __table_args__ = (
        UniqueConstraint('idx_geocountry', 'idx_georegion'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_geocountry = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_georegion = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_georegions.idx_georegion'),
        nullable=False, server_default='1')

    geocountry_name = Column(VARBINARY(128), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class GeoCities(BASE):
    """Class defining the mdl_geocities table of the database."""

    __tablename__ = 'mdl_geocities'

    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_geocity = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_georegion = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_georegions.idx_georegion'),
        nullable=False, server_default='1')

    geocity_name = Column(VARBINARY(128), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Addresses(BASE):
    """Class defining the mdl_addresses table of the database."""

    __tablename__ = 'mdl_addresses'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_address = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_geocity = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_geocities.idx_geocity'),
        nullable=False, server_default='1')

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class BillAddresses(BASE):
    """Class defining the mdl_billaddresses table of the database."""

    __tablename__ = 'mdl_billaddresses'
    __table_args__ = (
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_billaddress = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_geocity = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_geocities.idx_geocity'),
        nullable=False, server_default='1')

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class RiderDeviceAgents(BASE):
    """Class defining the mdl_ridersdeviceagents table of the database."""

    __tablename__ = 'mdl_ridersdeviceagents'
    __table_args__ = (
        UniqueConstraint(
            'idx_riderdevice', 'idx_agent'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_riderdeviceagent = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_riderdevice = Column(
        BIGINT(unsigned=True), ForeignKey('mdl_ridersdevices.idx_riderdevice'),
        nullable=False, server_default='1')

    idx_agent = Column(
        BIGINT(unsigned=True), ForeignKey('mdl_agents.idx_agent'),
        nullable=False, server_default='1')

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class DriverDeviceAgents(BASE):
    """Class defining the mdl_driversdeviceagents table of the database."""

    __tablename__ = 'mdl_driversdeviceagents'
    __table_args__ = (
        UniqueConstraint(
            'idx_driverdevice', 'idx_agent'),
        {
            'mysql_engine': 'InnoDB'
        }
    )

    idx_driverdeviceagent = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_driverdevice = Column(
        BIGINT(unsigned=True),
        ForeignKey('mdl_driversdevices.idx_driverdevice'),
        nullable=False, server_default='1')

    idx_agent = Column(
        BIGINT(unsigned=True), ForeignKey('mdl_agents.idx_agent'),
        nullable=False, server_default='1')

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Agents(BASE):
    """Class defining the mdl_agents table of the database."""

    __tablename__ = 'mdl_agents'
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    idx_agent = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    idx_agentname = Column(
        BIGINT(unsigned=True), ForeignKey('mdl_agentnames.idx_agentname'),
        nullable=False, server_default='1')

    id_agent = Column(VARBINARY(512), unique=True, nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class AgentNames(BASE):
    """Class defining the mdl_agent table of the database."""

    __tablename__ = 'mdl_agentnames'
    __table_args__ = {
        'mysql_engine': 'InnoDB'
    }

    idx_agentname = Column(
        BIGINT(unsigned=True), primary_key=True,
        autoincrement=True, nullable=False)

    agent_name = Column(VARBINARY(512), nullable=True, default=None)

    enabled = Column(INTEGER(unsigned=True), server_default='1')

    ts_modified = Column(
        DATETIME, server_default=text(
            'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),)

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))


class Configurations(BASE):
    """Class defining the mdl_configurations table of the database."""

    __tablename__ = 'mdl_configurations'
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
