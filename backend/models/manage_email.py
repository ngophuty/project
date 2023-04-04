from sqlalchemy import Column, Integer, DateTime, BigInteger, VARCHAR

from database.connect_mysql import Base


class DeliveryMail(Base):
    __tablename__ = "delivery_mail"

    id = Column(BigInteger, primary_key=True)					
    sengrid_id = Column(BigInteger)
    mail_recipient = Column(VARCHAR)
    customer_id = Column(BigInteger)
    plan_delivery_date = Column(DateTime)
    stop_delivery_flg = Column(DateTime)
    sent_datetime = Column(DateTime)
    open_datetime = Column(DateTime)
    recommend_numbers = Column(Integer, default=0)
    property_1 = Column(BigInteger)
    property_2 = Column(BigInteger)
    property_3 = Column(BigInteger)							
    created_at = Column(DateTime)			
    updated_at = Column(DateTime)


class PropertyRecommend(Base):
    __tablename__ = "property_recommend"

    id = Column(BigInteger, primary_key=True)
    customer_id = Column(BigInteger)
    property_id = Column(BigInteger)
    property_condominium_id = Column(BigInteger)
    property_recommend = Column(VARCHAR(length=255))
    recommend_property_url_pv = Column(Integer)
    recommend_property_access_datetime = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
