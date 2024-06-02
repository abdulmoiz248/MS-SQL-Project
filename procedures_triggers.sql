create procedure add_retailerbill_fill_inventory
 @product_id int,
 @retailer_id int,
 @quantity int,
 @discount int,
 @date date
as
begin
   if exists (select 1 from inventory where product_id=@product_id)

   begin
    update inventory set quantity=quantity+@quantity,date_modified=@date,retailer_id=@retailer_id where product_id=@product_id
   end  --end of if
   else
   begin
     insert into inventory(product_id,quantity,retailer_id,date_modified) values (@product_id,@quantity,@retailer_id,@date)
   end --else end
   declare @price int,
	@bill int
	select @price=price from products where product_id=@product_id
	set @bill=@price*@quantity
	set @bill=@bill-@bill*@discount/100
	insert into retailers_bill (retailer_id,bill,date,product_id,discount) values (@retailer_id,@bill,@date,@product_id,@discount)

	if exists(select 1 from revenue where date=@date)
	 begin
	  update revenue set expendtiure=expendtiure+@bill,net_amount=net_amount-@bill where date=@date
	 end
    else
	 begin
	   insert into revenue(date,income	,expendtiure,net_amount) values (@date,0,@bill,-@bill)
	 end --end of revenue else
end

create procedure prebookingpro 
  @user_id int,
  @product_id int, 
  @date date
as
begin 
   declare @quantity int
   select @quantity= quantity from inventory where product_id=@product_id
   if @quantity>0  
   begin
      print 'Already Exists'
      return
   end
   insert into prebooking values (@user_id,@product_id,@date)
end


	
create procedure add_cart_items
 @cart_id int,
 @product_id int,
 @quantity int
 as
begin
   declare @amount int,
   @invquantity int,
   @price int
   
   select @invquantity=quantity from inventory where product_id=@product_id
   if(@invquantity=0) 
   begin
   print 'NO items in inventory'
   return
   end

   if(@invquantity-@quantity<0)
   begin
   print 'NOT ENOUGH ITEMS AVAILABLE'
   return
   end

   select @price=price from products where product_id=@product_id
   set @amount=@price*@quantity

   insert into cart_items (cart_id,product_id,qunatity,total) values (@cart_id,@product_id,@quantity,@amount) 
   update cart set total=total+@amount where cart_id=@cart_id
  
end


create procedure insertreviews
  @product_id int,
  @user_id int,
  @rating decimal,
  @review varchar(max)
as begin
  if @rating>5 
  begin
      return
  end
  update products set rating=(@rating+rating)/2 where product_id=@product_id
  insert into reviews (product_id,user_id,rating,review) values (@product_id,@user_id,@rating,@review)
end

create procedure add_order
   @user_id int,
   @date DATE ,
   @shipping_id int,
   @coupon_id int,
   @payment_method varchar(100)
as
begin
   declare    @status varchar(100)
   set @status='IN QUEUE'
   if not exists (select 1 from coupons where coupon_id=@coupon_id)
   begin
    insert into orders (user_id,date,total_amount,payment_method,payment_status,shipping_id)values (@user_id,@date,0,@payment_method,@status,@shipping_id)
   end
   else 
   begin
    insert into orders (user_id,date,total_amount,payment_method,payment_status,shipping_id,coupon_id)values (@user_id,@date,0,@payment_method,@status,@shipping_id,@coupon_id)
   end
  
   insert into order_tracking (order_id,status,date) values (SCOPE_IDENTITY(),@status,@date) 
  
end

create procedure add_order_items

 @order_id int,
 @product_id int,
 @quantity int
 as
begin
   declare @amount int,
   @invquantity int,
   @price int
   
   select @invquantity=quantity from inventory where product_id=@product_id
   if(@invquantity=0) 
   begin
   print 'NO items in inventory'
   return
   end

   if(@invquantity-@quantity<0)
   begin
   print 'NOT ENOUGH ITEMS AVAILABLE'
   return
   end

   select @price=price from products where product_id=@product_id
   set @amount=@price*@quantity

   insert into order_items (order_id,product_id,qunatity,amount) values (@order_id,@product_id,@quantity,@amount) 
   update orders set total_amount=total_amount+@amount where order_id=@order_id
   update inventory set quantity=quantity-@quantity where product_id=@product_id

end

create procedure shift_to_order_from_cart
@userid int,
@shippingid int,
@couponid int,
@paymentmethod varchar(100)

as
begin

   if not exists (select 1 from cart where user_id=@userid)
   begin
   return
   end

  declare @cartid int, @date date

  select @cartid=cart_id,@date=date from cart where user_id=@userid


 exec  add_order
   @user_id =@userid,
   @date =@date,
   @shipping_id= @shippingid,
   @coupon_id=@couponid,
   @payment_method=@paymentmethod
  
  
   delete from cart where cart_id=@cartid
end

CREATE TRIGGER shiftitems
ON orders
AFTER INSERT
AS
BEGIN
    DECLARE @orderid INT, @product INT, @quantity INT, @cartid INT, @userid INT,@amount int

    -- Fetch the inserted order_id and user_id
    SELECT @orderid = order_id, @userid = user_id FROM inserted;

    -- Fetch the corresponding cart_id for the given user_id
    SELECT @cartid = cart_id FROM cart WHERE user_id = @userid;

    -- Loop to shift items from cart_items to order_items
    WHILE EXISTS (SELECT 1 FROM cart_items WHERE cart_id = @cartid)
    BEGIN
        -- Fetch the top item from cart_items
        SELECT TOP 1 @product = product_id, @quantity = qunatity ,@amount=total FROM cart_items WHERE cart_id = @cartid;

        -- Insert the item into order_items
        INSERT INTO order_items (order_id, product_id, qunatity,amount)
        VALUES (@orderid, @product, @quantity,@amount);

		update orders set total_amount=total_amount+@amount where order_id=@orderid

        -- Delete the item from cart_items
        DELETE FROM cart_items WHERE product_id = @product AND cart_id = @cartid AND qunatity = @quantity;
    END
END;

create procedure add_payments
   @order_id int,
   @date date 
as
begin
  declare @total_amount int,
  @afterdiscount decimal,
  @couponid int,
  @discount int,
  @shippingid int,
  @shippingfees int,
  @limit int, @enddate date

   select @total_amount=total_amount,@shippingid=shipping_id,@couponid=coupon_id from orders where order_id=@order_id
   select @shippingfees=fees from shipping where shipping_id=@shippingid
   set @total_amount=@total_amount++@shippingfees
   set @afterdiscount=@total_amount
    
if @couponid!= null 
 begin
  select @discount=discount_percent,@limit=limit,@enddate=end_date from coupons where coupon_id=@couponid
  if  @limit!=0 and @enddate!=@date
 begin
   select @discount from coupons where coupon_id=@couponid
   set @afterdiscount=@total_amount-@total_amount*@discount/100 +@shippingfees
 end
  
 end --if begin end of coupon id

  
  print @afterdiscount 
  insert payments (order_id,date,total_amount,after_discount) values (@order_id,@date,@total_amount,@afterdiscount)
  update order_tracking set status='Delievered',date=@date where order_id=@order_id
  update orders set payment_status='Cleared' where order_id=@order_id

end


create trigger addincome on payments
after insert
as
begin
 declare @income int,
 @date date
 select @income=after_discount,@date=date from inserted
 if exists (select 1 from revenue where date=@date)
 begin
  update revenue set income=income+@income,net_amount=net_amount+@income where date=@date
 end

 else
 begin
  insert into revenue (date,income,expendtiure,net_amount) values (@date,@income,0,@income)
 end
end

create procedure refunds
    @user_id INT,
    @product_id INT, 
	@order_id int,
	@quantity int,
    @reason VARCHAR(MAX),
	@date date
as
begin
   IF NOT EXISTS (SELECT 1 FROM orders WHERE order_id = @order_id) 
   begin
   print 'Order Doesnot Exists in record'
   return
   end
   insert into return_refunds (user_id,product_id,order_id,reason,qunatity,date) values (@user_id,@product_id,@order_id,@reason,@quantity,@date)
   update inventory set quantity=quantity+@quantity where product_id=@product_id
 declare @price int
 select @price=price from products where product_id=@product_id
   update revenue set expendtiure=expendtiure+@quantity*@price where date=@date  
   update order_tracking set status='Refund' where order_id=@order_id
end

