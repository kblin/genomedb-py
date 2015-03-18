# vim: set fileencoding=utf-8 :

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Domain(Base):
    __tablename__ = 'domains'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ddb_path = Column(String)

    def __repr__(self):
        return "<Domain({name}, {path})>".format(name=self.name, path=self.ddb_path)


class Kingdom(Base):
    __tablename__ = 'kingdoms'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ddb_path = Column(String)
    domain = relationship("Domain", backref=backref('kingdoms', order_by=id))
    domain_id = Column(Integer, ForeignKey('domains.id'))

    def __repr__(self):
        return "<Kingdom({name}, {path})>".format(name=self.name, path=self.ddb_path)


class Phylum(Base):
    __tablename__ = 'phyla'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ddb_path = Column(String)
    domain = relationship("Domain")
    domain_id = Column(Integer, ForeignKey('domains.id'))
    kingdom = relationship("Kingdom", backref=backref('phyla', order_by=id))
    kingdom_id = Column(Integer, ForeignKey('kingdoms.id'))

    def __repr__(self):
        return "<Phylum({name}, {path})>".format(name=self.name, path=self.ddb_path)


class Class(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ddb_path = Column(String)
    domain = relationship("Domain")
    domain_id = Column(Integer, ForeignKey('domains.id'))
    kingdom = relationship("Kingdom")
    kingdom_id = Column(Integer, ForeignKey('kingdoms.id'))
    phylum = relationship("Phylum", backref=backref('classes', order_by=id))
    phylum_id = Column(Integer, ForeignKey('phyla.id'))

    def __repr__(self):
        return "<Class({name}, {path})>".format(name=self.name, path=self.ddb_path)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ddb_path = Column(String)
    domain = relationship("Domain")
    domain_id = Column(Integer, ForeignKey('domains.id'))
    kingdom = relationship("Kingdom")
    kingdom_id = Column(Integer, ForeignKey('kingdoms.id'))
    phylum = relationship("Phylum")
    phylum_id = Column(Integer, ForeignKey('phyla.id'))
    class_ = relationship("Class", backref=backref('orders', order_by=id))
    class_id = Column(Integer, ForeignKey('classes.id'))

    def __repr__(self):
        return "<Order({name}, {path})>".format(name=self.name, path=self.ddb_path)


class Family(Base):
    __tablename__ = 'families'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ddb_path = Column(String)
    domain = relationship("Domain")
    domain_id = Column(Integer, ForeignKey('domains.id'))
    kingdom = relationship("Kingdom")
    kingdom_id = Column(Integer, ForeignKey('kingdoms.id'))
    phylum = relationship("Phylum")
    phylum_id = Column(Integer, ForeignKey('phyla.id'))
    class_ = relationship("Class")
    class_id = Column(Integer, ForeignKey('classes.id'))
    order = relationship("Order", backref=backref('families', order_by=id))
    order_id = Column(Integer, ForeignKey('orders.id'))

    def __repr__(self):
        return "<Family({name}, {path})>".format(name=self.name, path=self.ddb_path)


class Genus(Base):
    __tablename__ = 'genera'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ddb_path = Column(String)
    domain = relationship("Domain")
    domain_id = Column(Integer, ForeignKey('domains.id'))
    kingdom = relationship("Kingdom")
    kingdom_id = Column(Integer, ForeignKey('kingdoms.id'))
    phylum = relationship("Phylum")
    phylum_id = Column(Integer, ForeignKey('phyla.id'))
    class_ = relationship("Class")
    class_id = Column(Integer, ForeignKey('classes.id'))
    order = relationship("Order")
    order_id = Column(Integer, ForeignKey('orders.id'))
    family = relationship("Family", backref=backref('genera', order_by=id))
    family_id = Column(Integer, ForeignKey('families.id'))

    def __repr__(self):
        return "<Genus({name}, {path})>".format(name=self.name, path=self.ddb_path)


class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ddb_path = Column(String)
    domain = relationship("Domain")
    domain_id = Column(Integer, ForeignKey('domains.id'))
    kingdom = relationship("Kingdom")
    kingdom_id = Column(Integer, ForeignKey('kingdoms.id'))
    phylum = relationship("Phylum")
    phylum_id = Column(Integer, ForeignKey('phyla.id'))
    class_ = relationship("Class")
    class_id = Column(Integer, ForeignKey('classes.id'))
    order = relationship("Order")
    order_id = Column(Integer, ForeignKey('orders.id'))
    family = relationship("Family")
    family_id = Column(Integer, ForeignKey('families.id'))
    genus = relationship("Genus", backref=backref('species', order_by=id))
    genus_id = Column(Integer, ForeignKey('genera.id'))

    def __repr__(self):
        return "<Species({name}, {path})>".format(name=self.name, path=self.ddb_path)


class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gbk_path = Column(String)
    draft = Column(Boolean)
    domain = relationship("Domain")
    domain_id = Column(Integer, ForeignKey('domains.id'))
    kingdom = relationship("Kingdom")
    kingdom_id = Column(Integer, ForeignKey('kingdoms.id'))
    phylum = relationship("Phylum")
    phylum_id = Column(Integer, ForeignKey('phyla.id'))
    class_ = relationship("Class")
    class_id = Column(Integer, ForeignKey('classes.id'))
    order = relationship("Order")
    order_id = Column(Integer, ForeignKey('orders.id'))
    family = relationship("Family")
    family_id = Column(Integer, ForeignKey('families.id'))
    genus = relationship("Genus")
    genus_id = Column(Integer, ForeignKey('genera.id'))
    species = relationship("Species", backref=backref('species', order_by=id))
    species_id = Column(Integer, ForeignKey('species.id'))

    def __repr__(self):
        return "<Record({name}, {path})>".format(name=self.name, path=self.ddb_path)


class LocusTag(Base):
    __tablename__ = 'locus_tags'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    record = relationship("Record", backref=backref('locus_tags', order_by=id))
    record_id = Column(Integer, ForeignKey('records.id'))

    def __repr__(self):
        return "<LocusTag({name})>".format(name=self.name)
