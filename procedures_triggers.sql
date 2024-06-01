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

create trigger delete_prebookings 
on
inventory after 
insert,update 
as
begin
  declare @quantity int
  declare @id int
  select @id=product_id from inserted
  select @quantity=quantity from inventory where product_id=@id
  if (@quantity>0)
  begin

   delete from prebooking where product_id=@id
  end
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

drop procedure add_cart_items

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
