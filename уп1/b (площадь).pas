var a,b,c,d,e1,e2,p:int64;
begin
  read (a,b,c);
  
 
   if a mod c =0 then
    begin
    d:= a div c
   end
   else
    begin
    d:= ((a div c)+1);
   end;
    if b mod c =0 then
    begin
    p:= b div c
   end
   else
    begin
    p:= ((b div c)+1);
   end;
 

  write(d*p);
end.