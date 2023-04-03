from sqlalchemy import Column, Integer, String, DateTime, BigInteger, TIMESTAMP, VARCHAR, Date

from database.connect_mysql import Base


class SaleInfo(Base):
    __tablename__ = "sale_info"

    id = Column(BigInteger, primary_key=False)
    customer_id =Column(BigInteger)
    note_datetime = Column(TIMESTAMP)
    person_in_charge = Column(VARCHAR(length=255))				
    contact_method = Column(VARCHAR(length=255))
    comment = Column(VARCHAR(length=255))
    property_recommend = Column(VARCHAR(length=255))
    created_at =Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


class FollowPriorityCustomers(Base):
    __tablename__ = "follow_priority_customers"

    tdb = Column(Date)
    customer_id = Column(BigInteger)
    delivery_mail_id = Column(BigInteger)			
    priority_score = Column(Integer)						
    following_person_id = Column(BigInteger)				
    created_at = Column(DateTime)		
    updated_at = Column(DateTime)


class ClosedDealsInfo(Base):
    __tablename__ = "closed_deals_info"

    id = Column(BigInteger, primary_key=True)
    property_id = Column(BigInteger)
    property_condominium_id = Column(BigInteger)
    property_name = Column(VARCHAR(length=255))
    user_id = Column(BigInteger)
    tdb = Column(VARCHAR(length=255))
    deal_note = Column(VARCHAR(length=1000))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)