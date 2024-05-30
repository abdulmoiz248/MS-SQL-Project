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
