from sqlalchemy import Boolean, Column, Integer, String, DateTime

from database.connect_mysql import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)



class DeliveryMail(Base):
    __tablename__ = "delivery_mail"

    id = Column(Integer, primary_key=True, index=True)					
    sengrid_id = Column(Integer)
    mail_recipient = Column(String(length=255))
    customer_id = Column(Integer)
    plan_delivery_date = Column(DateTime)
    stop_delivery_flg = Column(DateTime)
    sent_datetime = Column(DateTime)
    open_datetime = Column(DateTime)
    recommend_numbers = Column(Integer)
    property_1 = Column(Integer)
    property_2 = Column(Integer)
    property_3 = Column(Integer)							
    created_at = Column(DateTime)			
    updated_at = Column(DateTime)


class PropertyRecommend(Base):
    __tablename__ = "property_recommend"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    property_condominium_id = Column(Integer)
    property_recommend = Column(String(length=255))
    recommend_property_url_pv = Column(Integer)
    recommend_property_access_datetime = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class FollowPriorityCustomers(Base):
    __tablename__ = "follow_priority_customers"

    customer_id = Column(Integer)
    delivery_mail_id = Column(Integer)			
    priority_score = Column(Integer)						
    following_person_id = Column(Integer)				
    created_at = Column(DateTime)		
    updated_at = Column(DateTime)


class SaleInfo(Base):
    __tablename__ = "sale_info"

    id = Column(Integer, primary_key=True, index=True)
    customer_id =Column(Integer)
    note_datetime = Column(DateTime)
    person_in_charge = Column(String(length=1000))				
    contact_method = Column(String(length=1000))
    comment = Column(String(length=1000))
    property_recommend = Column(String(length=1000))
    created_at =Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


class ClosedDealsInfo(Base):
    __tablename__ = "closed_deal_info"

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer)
    property_condominium_id = Column(Integer)
    property_name = Column(String(length=255))
    user_id = Column(Integer)
    tdb = Column(Integer)
    deal_note = Column(String(length=1000))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)